import sys, os
from RestAuthenticator import RestAuthenticator
from RestConnector import RestConnector

authenticator = RestAuthenticator('/home/matt/sw360/sw360rest')
if (authenticator.get_headers() == 1):
    connector = RestConnector('http://localhost:8091/api/', authenticator.headers)
else:
    sys.exit()

dump_file = open('sw360db_dump', 'w+')
for obj_type in connector.type_formatters.keys():
    for obj in connector.get_all_objects(obj_type):
        dump_file.write(str(obj)+'\n')
dump_file.close()
