from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declared_attr
from framework import HPotterDB
from env import logger
import socket
import socketserver
import threading

# remember to put name in __init__.py

# https://hg.python.org/cpython/file/2.7/Lib/SocketServer.py

class GenericTable(HPotterDB.Base):
    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()

    id =  Column(Integer, primary_key=True)
    echo = Column(String)

    hpotterdb_id = Column(Integer, ForeignKey('hpotterdb.id'))
    hpotterdb = relationship("HPotterDB")

class GenericTCPHandler(socketserver.BaseRequestHandler):
    def setup(self):
        session = sessionmaker(bind=self.server.engine)
        self.session = session()

    def handle(self):
        data = self.request.recv(1024)

        entry = HPotterDB.HPotterDB (
            sourceIP=self.client_address[0], \
            sourcePort=self.client_address[1], \
            destIP=self.server.mysocket.getsockname()[0], \
            destPort=self.server.mysocket.getsockname()[1], \
            proto=HPotterDB.TCP)
        generic = GenericTable(echo=data)
        generic.hpotterdb = entry
        self.session.add(generic)

        # add to the DB
        '''
        self.session.add(GenericTable(echo=data, \
            sourceIP=self.client_address[0], \
            sourcePort=self.client_address[1], \
            destIP=self.server.mysocket.getsockname()[0], \
            destPort=self.server.mysocket.getsockname()[1], \
            proto=HPotterDB.TCP))
        '''

        # reply to request
        self.request.sendall(data.upper())

    def finish(self):
        self.session.commit()
        self.session.close()

# help from
# http://cheesehead-techblog.blogspot.com/2013/12/python-socketserver-and-upstart-socket.html
# http://stackoverflow.com/questions/8549177/is-there-a-way-for-baserequesthandler-classes-to-be-statful

class GenericServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    allow_reuse_address = True

    def __init__(self, mysocket, engine):
        # save socket for use in server_bind and handler
        self.mysocket = mysocket

        # save engine for creating sessions in the handler
        self.engine = engine

        # must be called after setting mysocket as __init__ calls server_bind
        socketserver.TCPServer.__init__(self, None, GenericTCPHandler)

    def server_bind(self):
        self.socket = self.mysocket

# listen to both IPv4 and v6
def get_addresses():
    return ([(socket.AF_INET, '127.0.0.1', 2000), \
        (socket.AF_INET6, '::1', 2000)])

def start_server(my_socket, engine):
    server = GenericServer(my_socket, engine)
    server_thread = threading.Thread(target=server.serve_forever)
    server_thread.start()

    return server
