import sys, os, json
from RestAuthenticator import RestAuthenticator
from RestConnector import RestConnector

authenticator = RestAuthenticator('/home/matt/sw360/sw360rest')
if (authenticator.get_headers() == 1):
    connector = RestConnector('http://localhost:8091/api/', authenticator.headers)
else:
    sys.exit()


sw360_objects = []
for obj_type in connector.type_formatters.keys():
    for obj in connector.get_all_objects(obj_type):
        sw360_objects.append(obj)

encoder = json.JSONEncoder()
dump_file = open('sw360db_dump', 'w+')
dump_file.write(json.JSONEncoder.encode(encoder, sw360_objects))
dump_file.close()
