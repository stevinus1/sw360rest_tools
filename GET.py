import requests, re, sys, json, ast
import format_project_data, format_component_data, format_vendor_data, format_release_data, format_license_data

successful_import = 0
while successful_import == 0:
    try:
        import header, global_vars
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

# Returns a list of all objects of a given type that contain a given name fragment
def get_all (name_fragment, type):

    # Making GET request
    url = "http://localhost:8091/api/" + type.lower() + "s"
    r = requests.get(url, headers=global_vars.headers)
    if (r.status_code != 200):
        print "GET method was unsuccessful.\n" + r.text
        return None

    # Obtaining results
    results = []
    objects = json.JSONDecoder.decode(global_vars.decoder, r.text)
    if ((type.lower() == 'component') or (type.lower() == 'project') or (type.lower() == 'release')):
        for object in objects['_embedded']['sw360:'+type+'s']:
            if (name_fragment.lower() in object['name'].lower()):
                results.append(object)
    if ((type.lower() == 'license') or (type.lower() == 'vendor')):
        for object in objects['_embedded']['sw360:'+type+'s']:
            if (name_fragment.lower() in object['fullName'].lower()):
                results.append(object)
    elif (type.lower() == 'user'):
        for object in objects['_embedded']['sw360:'+type+'s']:
            if (name_fragment.lower() in object['email'].lower()):
                results.append(object)
    return results

# Returns a single object in dictionary form of a given name that matches a given type
def get_object (name, type):
    
    # Getting id of that object and making GET request
    id = get_id(name, type)
    if (id is None):
        return None
    url = "http://localhost:8091/api/" + type.lower() + "s/" + id
    r = requests.get(url, headers=global_vars.headers)
    if (r.status_code == 200):
        get_text = r.text
    else:
        print "GET method was unsuccessful.\n" + r.text
        return
    if (type.lower() == 'license'):
        return format_license_data.format_get(get_text)
    elif (type.lower() == 'vendor'):
        return format_vendor_data.format_get(get_text)
    elif (type.lower() == 'release'):
        return format_release_data.format_get(get_text)
    elif (type.lower() == 'project'):
        return format_project_data.format_get(get_text)
    elif (type.lower() == 'component'):
        return format_component_data.format_get(get_text)
    else:
        print "Please enter a valid type."
        return None
    
# Returns the Id of an object of given type that matches a given name
def get_id (name, type):
    
    # Getting list of objects of that type in dict form
    dictionaries = get_all("", type)
    self = ""

    # Finding specified object
    if ((type.lower() == 'license') or (type.lower() == 'vendor')):
        for dictionary in dictionaries:
            if(dictionary['fullName'].lower() == name.lower()):
                self = str(dictionary['_links'])
    elif (type.lower() == 'release'):
        version = raw_input("Please specify the version of your release: ")
        for dictionary in dictionaries:
            if(dictionary['name'].lower() == name.lower()) and (dictionary['version'].lower() == version.lower()):
                self = str(dictionary['_links'])
    elif ((type.lower() == 'component') or (type.lower() == 'project')):   
        for dictionary in dictionaries:
            if(dictionary['name'].lower() == name.lower()):
                self = str(dictionary['_links'])
    elif (type.lower() == 'user'):   
        for dictionary in dictionaries:
            if(dictionary['email'].lower() == name.lower()):
                self = str(dictionary['_links'])
    else:
        print "Please enter a valid type."
        return None

    #Getting Id
    if (self != ""):
        idMatch = re.search(global_vars.id_pattern, self)
        id = idMatch.group(1)
        return id

# Returns a given field from an object of given type that matches a given name
def get_field (name, type, field):

    # Getting object as dictionary
    object = get_object(name, type)

    # Get field
    try:
        field_value = object[field]
    except KeyError:
        print "Specified field does not exist."
        return None
    return field_value

        
        
