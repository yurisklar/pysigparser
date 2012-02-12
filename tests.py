"""
Tests for Signature parser
"""
import unittest
import os
import json
import xmlrpclib
import client.settings

class TestSignaturesParser(unittest.TestCase):
    """
    Class to test Signature parser
    """

    def testSignaturesParser(self):
        """
        Test Signature parser with predefined signatures.
        The directory tests/signatures has pairs of .sig and .json files.
        The test sends each .sig file to server and compare with corresponding expected .json file.
        The server must be running at this moment.
        """

        signatures_dir = os.path.abspath(os.path.dirname(__file__)) + os.sep + "tests" + os.sep + "signatures"
        signatures = [ filename.replace(".sig", "") for filename in os.listdir(signatures_dir) if filename.endswith(".sig")]

        # initializing XML-RPC client
        xmlrpc_connection = xmlrpclib.Server('http://%s:%d' % (client.settings.connection_host, client.settings.connection_port))

        self.maxDiff = None
        for signature in signatures:
            sig_filename = signatures_dir + os.sep + signature + ".sig"
            json_filename = signatures_dir + os.sep + signature + ".json"

            expected_dict = json.load(open(json_filename, "r"))
            received_dict = json.loads(xmlrpc_connection.parse_signature(open(sig_filename, "r").read()))

            print("signature: %s" % (signature, ))

            #todo: make case in-sensitive comparison
            self.assertDictEqual(expected_dict, received_dict)


if __name__ == "__main__":
    unittest.main()