import sys, argparse, os
from RestAuthenticator import RestAuthenticator
from RestConnector import RestConnector

parser = argparse.ArgumentParser()
help_message = 'paths to files containing objects to be uploaded'
parser.add_argument('filepaths', nargs='*', help=help_message)
filepaths = parser.parse_args().filepaths

authenticator = RestAuthenticator('/home/matt/sw360/sw360rest')
if (authenticator.get_headers() == 1):
    connector = RestConnector('http://localhost:8091/api/', authenticator.headers)
else:
    sys.exit()

if (filepaths != []):
    for filepath in filepaths:
        dictionaries = connector.format_objects_from_file(filepath)
        connector.post_objects(dictionaries)
