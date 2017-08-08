import re, json, sys

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
