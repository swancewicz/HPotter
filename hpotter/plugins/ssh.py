from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declared_attr
from hpotter.hpotter import HPotterDB
from hpotter.hpotter.command_response import command_response
from paramiko.py3compat import u, decodebytes
from hpotter.hpotter import consolidated
import socket
import paramiko
import threading
from binascii import hexlify
import sys
import re
from hpotter.hpotter.__main__ import _response_container


class SSHServer(paramiko.ServerInterface):
    undertest = False
    data = (
        b"AAAAB3NzaC1yc2EAAAABIwAAAIEAyO4it3fHlmGZWJaGrfeHOVY7RWO3P9M7hp"
        b"fAu7jJ2d7eothvfeuoRFtJwhUmZDluRdFyhFY/hFAh76PJKGAusIqIQKlkJxMC"
        b"KDqIexkgHAfID/6mqvmnSJf0b5W8v5h2pI/stOSwTQ+pxVhwJ9ctYDhRSlF0iT"
        b"UWT10hcuO4Ks8="
    )
    good_pub_key = paramiko.RSAKey(data=decodebytes(data))

    def __init__(self, mysocket, engine, addr):
        self.mysocket = mysocket
        self.engine = engine
        self.addr = addr
        self.event = threading.Event()

        s = sessionmaker(bind=self.engine)
        self.session = s()

    def check_channel_request(self, kind, chanid):
        if kind == "session":
            return paramiko.OPEN_SUCCEEDED
        return paramiko.OPEN_FAILED_ADMINISTRATIVELY_PROHIBITED

    def check_auth_password(self, username, password):
        # changed so that any username/password can be used
        if username and password:
            self.entry = HPotterDB.HPotterDB(
                sourceIP=self.addr[0],
                sourcePort=self.addr[1],
                destIP=self.mysocket.getsockname()[0],
                destPort=self.mysocket.getsockname()[1],
                proto=HPotterDB.TCP)
            login = consolidated.LoginTable(username=username, password=password)
            login.hpotterdb = self.entry
            self.session.add(login)

            return paramiko.AUTH_SUCCESSFUL
        return paramiko.AUTH_FAILED

    def check_auth_publickey(self, username, key):
        print("Auth attempt with key: " + u(hexlify(key.get_fingerprint())))
        if username == 'exit':
            sys.exit(1)
        if(username == "user") and (key == self.good_pub_key):
            return paramiko.AUTH_SUCCESSFUL
        return paramiko.AUTH_FAILED

    def check_auth_gssapi_with_mic(self, username, gss_authenticated=paramiko.AUTH_FAILED, cc_file=None):
        if gss_authenticated == paramiko.AUTH_SUCCESSFUL:
            return paramiko.AUTH_SUCCESSFUL
        return paramiko.AUTH_FAILED

    def check_auth_gssapi_keyex(self, username, gss_authenticated=paramiko.AUTH_FAILED, cc_file=None):
        if gss_authenticated == paramiko.AUTH_SUCCESSFUL:
            return paramiko.AUTH_SUCCESSFUL
        return paramiko.AUTH_FAILED

    # Turned off, causing problems
    def enable_auth_gssapi(self):
        return False

    def get_allowed_auths(self, username):
        return "gssapi-keyex,gssapi-with-mic,password,publickey"

    def check_channel_shell_request(self, channel):
        self.event.set()
        return True

    def check_channel_pty_request(
            self, channel, term, width, height, pixelwidth, pixelheight,
            modes):
        return True

    # help from:
    # https://stackoverflow.com/questions/24125182/how-does-paramiko-channel-recv-exactly-work
    def receive_client_data(self, chan):
        command_count = 0
        workdir = ''

        threading.Timer(120, chan.close).start()

        while command_count < 4:
            command = ""
            chan.send("\r\n# ")

            while True:
                character = chan.recv(1024).decode("utf-8")
                if character == ("\r" or "\r\n" or ""):
                    break
                command += character
                chan.send(character)
            command_count += 1

            if command == '':
                continue

            if command.startswith('cd'):
                directory = command.split(' ')
                if len(directory) == 1:
                    continue
                directory = directory[1]

                if directory == '.':
                    continue

                if directory == '..':
                    workdir = re.sub(r'/[^/]*/?$', '', workdir)
                    continue

                if directory[0] != '/':
                    workdir += '/'
                workdir += directory

                continue

            if command == 'exit':
                break

            cmd = consolidated.CommandTable(command=command)
            cmd.hpotterdb = self.entry
            self.session.add(cmd)

            print(workdir)
            exit_code, output = \
                _response_container.exec_run('timeout -t 1 ' + command,
                                             workdir=workdir)

            if exit_code == 126:
                chan.send(b'\r\n' + command.encode("utf-8") +
                          b': command not found\n')
            else:
                if output.__contains__(b"\n"):
                    output = output.replace(b"\n", b"\r\n")
                chan.send(output)

    def finish(self):
        # ugly ugly ugly
        # i need to figure out how to properly mock sessionmaker
        if not self.undertest:
            self.session.commit()
            self.session.close()


# listen to both IPv4 and v6
# quad 0 allows for docker port exposure
def get_addresses():
    return [(socket.AF_INET, '0.0.0.0', 22)]


def start_server(socket, engine):
    socket.listen(4)

    while True:
        client, addr = socket.accept()

        transport = paramiko.Transport(client)
        transport.load_server_moduli()

        # Experiment with different key sizes at:
        # http://travistidwell.com/jsencrypt/demo/
        host_key = paramiko.RSAKey(filename="RSAKey.cfg")
        transport.add_server_key(host_key)

        server = SSHServer(socket, engine, addr)
        transport.start_server(server=server)
        chan = transport.accept()
        if not chan:
            print('no chan')
            continue

        chan.send("\r\nLast login: Whatever you want it to be")
        server.receive_client_data(chan)
        chan.close()


def stop_server():
    pass
