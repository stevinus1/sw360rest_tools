import requests, ast, re, sys

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

# Returns a list of all objects of a given type that contain a given name fragment
def GETAll (name_fragment, type):

    # Making GET request
    url = "http://localhost:8091/api/" + type.lower() + "s"
    r = requests.get(url, headers=header.headers)
    if (r.status_code == 200):
        objects = r.text
    else:
        print "GET method was unsuccessful.\n" + r.text
    

    # Obtaining results
    dictionaries = []
    results = []
    objects = re.findall('\[\s+(([^\]]*\n*)*)\]', objects)[0][0]
    for object in objects.split(', '):
        dictionaries.append(ast.literal_eval(object))
    if ((type.lower() == 'component') or (type.lower() == 'project') or (type.lower() == 'release')):
        for dictionary in dictionaries:
            if (name_fragment.lower() in dictionary['name'].lower()):
                results.append(dictionary)
    if ((type.lower() == 'license') or (type.lower() == 'vendor')):
        for dictionary in dictionaries:
            if (name_fragment.lower() in dictionary['fullName'].lower()):
                results.append(dictionary)
    elif (type.lower() == 'user'):
        for dictionary in dictionaries:
            if (name_fragment.lower() in dictionary['email'].lower()):
                results.append(dictionary)
    return results

# Returns the Id of an object of given type that matches a given name
def GETId (name, type):
    
    # Getting list of objects of that type in dict form
    dictionaries = GETAll("", type)
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
        return

    #Getting Id
    if (self != ""):
        idMatch = re.search('''["|']http://.*/(.*)["|']''', self)
        id = idMatch.group(1)
        return id

# Returns a given field from an object of given type that matches a given name
def GETField (name, type, field):

    # Getting list of objects of that type in dict form
    dictionaries = GETAll("", type)
    self = ""

    # Finding specified object and field
    if ((type.lower() == 'license') or (type.lower() == 'vendor')):
        for dictionary in dictionaries:
            if(dictionary['fullName'].lower() == name.lower()):
                try:
                    field = dictionary[field]
                except KeyError:
                    print "The specified field could not be found."
                    return
    elif (type.lower() == 'release'):
        version = raw_input("Please specify the version of your release: ")
        for dictionary in dictionaries:
            if(dictionary['name'].lower() == name.lower()) and (dictionary['version'].lower() == version.lower()):
                try:
                    field = dictionary[field]
                except KeyError:
                    print "The specified field could not be found."
                    return
    elif ((type.lower() == 'component') or (type.lower() == 'project')):
        for dictionary in dictionaries:
            if(dictionary['name'].lower() == name.lower()):
                try:
                    field = dictionary[field]
                except KeyError:
                    print "The specified field could not be found."
                    return
    elif (type.lower() == 'user'):   
        for dictionary in dictionaries:
            if(dictionary['email'].lower() == name.lower()):
                try:
                    field = dictionary[field]
                except KeyError:
                    print "The specified field could not be found."
                    return
    else:
        print "Please enter a valid type."
        return
    return field

        
        
