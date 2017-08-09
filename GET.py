import requests, re, sys, json, ast

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
    if (not global_vars.type_ids.has_key(type)):
        print "Please enter a valid type."
        return None
    url = "http://localhost:8091/api/" + type.lower() + "s"
    r = requests.get(url, headers=global_vars.headers)
    if (r.status_code != 200):
        print "GET method was unsuccessful.\n" + r.text
        return None

    # Obtaining results
    results = []
    objects = json.JSONDecoder.decode(global_vars.decoder, r.text)
    for obj in objects['_embedded']['sw360:'+type+'s']:
        if (name_fragment.lower() in obj[global_vars.type_ids[type]].lower()):
            result_obj = get_object(obj[global_vars.type_ids[type]], type)
            if (result_obj is not None):
                results.append(result_obj)
    return results

# Returns a single object in dictionary form of a given name that matches a given type
def get_object (name, type, version = None):
    
    # Getting id of that object
    if (not global_vars.type_format_classes.has_key(type)):
        print "Please enter a valid type."
        return None
    id = get_id(name, type, version)
    if (id is None):
        return None

    # Making GET request
    url = "http://localhost:8091/api/" + type.lower() + "s/" + id
    r = requests.get(url, headers=global_vars.headers)
    if (r.status_code != 200):
        message = name + " (" + type + "): " + "GET method was unsuccessful.\n" + r.text
        print message
        return None

    # Returning object
    return global_vars.type_format_classes[type].format_get(r.text)

    
# Returns the Id of an object of given type that matches a given name
def get_id (name, type, version = None):
    
    # Getting list of objects of that type
    if (not global_vars.type_format_classes.has_key(type)):
        print "Please enter a valid type."
        return None
    url = "http://localhost:8091/api/" + type.lower() + "s"
    r = requests.get(url, headers=global_vars.headers)
    if (r.status_code != 200):
        message = name + " (" + type + "): " + "GET method was unsuccessful.\n" + r.text
        print message
        return None

    # Finding specified object
    dictionaries = json.JSONDecoder.decode(global_vars.decoder,r.text)
    dictionaries = dictionaries['_embedded']['sw360:'+type+'s']
    self = ""
    for dictionary in dictionaries:
        if (type.lower() == 'release'):
            if (version is None):
                version = raw_input("Please specify the version of your release: ")
            if(dictionary['name'].lower() == name.lower()) and (dictionary['version'].lower() == version.lower()):
                self = str(dictionary['_links'])
        else:
            if(dictionary[global_vars.type_ids[type]].lower() == name.lower()):
                self = str(dictionary['_links'])

    #Getting id
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

        
        
