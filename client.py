import xmlrpclib
import client.settings

# initializing XML-RPC client
xmlrpc_connection = xmlrpclib.Server('http://%s:%d' % (client.settings.connection_host, client.settings.connection_port))

if __name__ == "__main__":
    # todo: not completed
    print xmlrpc_connection.parse_signature('test test test')
