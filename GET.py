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
    if ((type.lower() == 'component') or (type.lower() == 'project')):
        for sw360_object in objects['_embedded']['sw360:'+type+'s']:
            if (name_fragment.lower() in sw360_object['name'].lower()):
                results.append(get_object(sw360_object['name'], type))
    elif (type.lower() == 'releases'):
        for sw360_object in objects['_embedded']['sw360:'+type+'s']:
            if (name_fragment.lower() in sw360_object['name'].lower()):
                results.append(get_object(sw360_object['name'], type, sw360_object['version']))
    if ((type.lower() == 'license') or (type.lower() == 'vendor')):
        for sw360_object in objects['_embedded']['sw360:'+type+'s']:
            if (name_fragment.lower() in sw360_object['fullName'].lower()):
                results.append(get_object(sw360_object['fullName'], type))
    elif (type.lower() == 'user'):
        for sw360_object in objects['_embedded']['sw360:'+type+'s']:
            if (name_fragment.lower() in sw360_object['email'].lower()):
                results.append(get_object(sw360_object['email'], type))
    return results

# Returns a single object in dictionary form of a given name that matches a given type
def get_object (name, type, version = None):
    
    # Getting id of that object and making GET request
    id = get_id(name, type, version)
    if (id is None):
        return None
    url = "http://localhost:8091/api/" + type.lower() + "s/" + id
    r = requests.get(url, headers=global_vars.headers)
    if (r.status_code != 200):
        print "GET method was unsuccessful.\n" + r.text
        return None
    if (type.lower() == 'license'):
        return format_license_data.format_get(r.text)
    elif (type.lower() == 'vendor'):
        return format_vendor_data.format_get(r.text)
    elif (type.lower() == 'release'):
        return format_release_data.format_get(r.text)
    elif (type.lower() == 'project'):
        return format_project_data.format_get(r.text)
    elif (type.lower() == 'component'):
        return format_component_data.format_get(r.text)
    elif (type.lower() == 'user'):
        return format_user_data.format_get(r.text)
    else:
        print "Please enter a valid type."
        return None
    
# Returns the Id of an object of given type that matches a given name
def get_id (name, type, version = None):
    
    # Getting list of objects of that type
    url = "http://localhost:8091/api/" + type.lower() + "s"
    r = requests.get(url, headers=global_vars.headers)
    if (r.status_code != 200):
        print "GET method was unsuccessful.\n" + r.text
        return None
    dictionaries = json.JSONDecoder.decode(global_vars.decoder,r.text)
    dictionaries = dictionaries['_embedded']['sw360:'+type+'s']
    self = ""

    # Finding specified object
    if ((type.lower() == 'license') or (type.lower() == 'vendor')):
        for dictionary in dictionaries:
            if(dictionary['fullName'].lower() == name.lower()):
                self = str(dictionary['_links'])
    elif (type.lower() == 'release'):
        if (version is None):
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
def get_field (name, type, field, version = None):

    # Getting object as dictionary
    object = get_object(name, type, version)

    # Get field
    try:
        field_value = object[field]
    except KeyError:
        print "Specified field does not exist."
        return None
    return field_value

        
        
