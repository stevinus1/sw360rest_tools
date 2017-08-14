import sys, argparse, os
from RestAuthenticator import RestAuthenticator
from RestConnector import RestConnector

parser = argparse.ArgumentParser()
help_message1 = 'paths to files containing objects to be uploaded'
parser.add_argument('filepaths', nargs='*', help=help_message1)
paths = parser.parse_args().filepaths

authenticator = RestAuthenticator('/home/matt/sw360/sw360rest')
if (authenticator.get_headers() == 1):
    connector = RestConnector('http://localhost:8091/api/', authenticator.headers)
else:
    sys.exit()

print '\n'
if (paths != []):
    for path in paths:
        dictionaries = connector.format_objects_from_file(path)
        connector.post_objects(dictionaries)
