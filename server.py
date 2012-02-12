"""
XML-RPC server
"""
import sys
import signal
import SimpleXMLRPCServer
import server.settings
from server.controller import RequestHandler

def handle_os_signal(signalNumber, frameObj):
    """
    handling os signal for keyboard interrupt
    or in case the signal to stop was received
    """
    if signalNumber == signal.SIGINT:
        print("Stopping the server")
        sys.exit(0)

if __name__ == "__main__":

    # register the handle for INT signal
    signal.signal(signal.SIGINT, handle_os_signal)

    # initialization of Simple XML-RPC Server
    server = SimpleXMLRPCServer.SimpleXMLRPCServer((server.settings.bind_host, server.settings.bind_port))
    # registering controller
    server.register_instance(RequestHandler())
    # starting it to serve requests
    server.serve_forever()
