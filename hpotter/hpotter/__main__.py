import hpotter.plugins
import importlib

from sqlalchemy import create_engine
from hpotter.env import logger, db
from hpotter.hpotter.HPotterDB import Base

import socket
import signal
import docker

# start docker container
client = docker.from_env()
_response_container = client.containers.run('alpine', command=['/bin/ash'],
                                            tty=True, detach=True, read_only=True)

network = client.networks.get('bridge')
network.disconnect(_response_container)


def shutdown_servers(signum, frame):
    _response_container.stop()
    _response_container.remove()
    plugins_dict = hpotter.plugins.__dict__
    for plugin_name in plugins_dict['__all__']:
        importlib.import_module('hpotter.plugins.' + plugin_name)
        plugin = plugins_dict[plugin_name]
        plugin.stop_server()


if "__main__" == __name__:
    signal.signal(signal.SIGINT, shutdown_servers)

    # fire up the db
    engine = create_engine(db, echo=True)
    Base.metadata.create_all(engine)

    plugins_dict = hpotter.plugins.__dict__
    for plugin_name in plugins_dict['__all__']:
        importlib.import_module('hpotter.plugins.' + plugin_name)
        plugin = plugins_dict[plugin_name]
        for address in plugin.get_addresses():
            mysocket = socket.socket(address[0])
            try:
                mysocket.bind((address[1], address[2]))
                plugin.start_server(mysocket, engine)
            except OSError as e:
                print("bind to", address[1], address[2], e.strerror)
