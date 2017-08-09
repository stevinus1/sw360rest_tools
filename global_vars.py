import re, json, sys
import format_project_data, format_component_data, format_vendor_data, format_release_data, format_license_data, format_user_data

successful_import = 0
while successful_import == 0:
    try:
        import header
        successful_import = 1
    except OSError as err:
        print err.message + "\n"
        try:
            print "Press enter to try again, CTRL-C to exit."
            sys.stdin.readline()
        except KeyboardInterrupt:
            sys.exit()
    except IOError as err:
        print err.message + "\n"
        try:
            print "Press enter to try again, CTRL-C to exit."
            sys.stdin.readline()
        except KeyboardInterrupt:
            sys.exit()
            
# Useful global variables

global id_pattern
id_pattern = '''["|']http://.*/([^\s]*)["|']'''

global headers
headers = header.headers
global decoder
decoder = json.JSONDecoder()

global type_ids
type_ids = {'license': 'fullName', 'vendor': 'fullName', 'component': 'name', 'release': 'name', 'project': 'name', 'user': 'email'}
global type_format_classes
type_format_classes = {'license': format_license_data, 'vendor': format_vendor_data, 'component': format_component_data, 'release': format_release_data, 'project': format_project_data, 'user': format_user_data}
