import subprocess, requests, sys, ast, os, re
import format_project_data, format_component_data, format_vendor_data, format_release_data, format_license_data
import GET, global_vars

# Reading in information
try:
    info_filepath = raw_input("What is the filepath for the information? ")
    print "\n"
except IOError as err:
    err.message = "IO Error: " + err.strerror
    raise IOError(err.message)
try:
    file = open(info_filepath, "r")
    info = file.read()
except OSError as err:
    err.message = "OS Error: " + err.strerror
    raise OSError(err.message)
except IOError as err:
    err.message = "IO Error: " + err.strerror
    raise IOError(err.message)

# Making lists of objects
dictionaries = []
releases = []
POST_objects = []
items = re.findall('(\{([^\}]*?\n+[^\}]*?)*\})', info)
for item in items:
    dictionaries.append(ast.literal_eval(item[0]))
if (dictionaries == []):
    print("You haven't provided any valid objects to POST.")
    sys.exit()
for di in dictionaries:
    if (not global_vars.type_format_classes.has_key(di['type'].lower())):
        print "Please specify valid types for all your objects."
        sys.exit()
    elif (di['type'].lower() == 'release'):
        releases.append(di)
    else:
        POST_objects.append(di)

# Adding in any missing fields to dictionaries and making POST requests
if (releases != []):
    stored_components = GET.get_all('', 'component')
for release in releases:
    url = "http://localhost:8091/api/releases"
    has_component = 0
    for component in stored_components:
        if (component['name'] == release['name']):
            component_id = GET.get_id(component['name'], 'component')
            has_component = 1
    if (has_component == 0):
        print "A release cannot exist independently of a component of the same name.\n\n"
        break
    if (global_vars.type_format_classes['release'].format_post(release, component_id) == 1):
        r = requests.post(url, headers=global_vars.headers, json=release)
        if (r.status_code == 201):
            print release['name'] + " (Release)" + ": POST method was successful\n\n"
        else:
            print release['name'] + " (Release)" + ": POST method was unsuccessful\n" + r.text + "\n\n"

for obj in POST_objects:
    type = obj['type'].lower()
    url = "http://localhost:8091/api/" + type + "s"
    if (global_vars.type_format_classes[type].format_post(obj) == 1):
        r = requests.post(url, headers=global_vars.headers, json=obj)
        else:
        if (r.status_code == 201):
            message = obj[global_vars.type_ids[type]] + " (" + type + ")" + ": POST method was successful\n\n"
            print message
        else:
            message = obj[global_vars.type_ids[type]] + " (" + type + ")" + ": POST method was unsuccessful\n" + r.text + "\n\n"
            print message
