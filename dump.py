import sys
from RestAuthenticator import RestAuthenticator
from RestConnector import RestConnector

authenticator = RestAuthenticator('/home/matt/sw360/sw360rest')
if (authenticator.get_headers() == 1):
    connector = RestConnector('http://localhost:8091/api/', authenticator.headers)
else:
    sys.exit()

data_dump = ""

for obj_type in RestConnector.type_identifiers.keys():
    data_dump = data_dump + str(connector.get_all_objects(connector, obj_type))
