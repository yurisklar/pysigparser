"""
XML-RPC client
"""
import sys
import getopt
import xmlrpclib
import client.settings

def usage():
    """ Prints the usage information """

    t_usage = """Usage: python %(filename)s -f <filename.sig>

 The script connects to XML-RPC server
sending the data from <filename.sig>
and prints received JSON

 Example: python %(filename)s -f <path-to>/tests/1.sig
""" % {"filename": sys.argv[0]}
    print(t_usage)


if __name__ == "__main__":

    if len(sys.argv) == 1:
        usage()
        sys.exit(2)

    try:
        opts, args = getopt.getopt(sys.argv[1:], 'hf:', ['help','file='])
    except getopt.GetoptError, e:
        print(e)
        usage()
        sys.exit(2)

    sig_filename = None

    for o, a in opts:
        if o in ("-h", "--help"):
            usage()
            sys.exit(0)
        elif o in ("-f", "--file"):
            sig_filename = a
        else:
            assert False, "unhandled option"

    if sig_filename is None:
        usage()
        sys.exit(2)

    try:
        signature = open(sig_filename, "r").read()
    except IOError:
        print("Cannot open %s for reading" % (sig_filename,))
        sys.exit(1)

    # initializing XML-RPC client
    xmlrpc_connection = xmlrpclib.Server('http://%s:%d' % (client.settings.connection_host, client.settings.connection_port))

    print("Signature:\n\n%s\n" % (signature, ))
    print("Parsed data:\n%r" % (xmlrpc_connection.parse_signature(signature), ))
