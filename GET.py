import requests, ast, re
import header

# Returns a list of all objects of a given type that contain a given name fragment
def GETAll (name_fragment, type):

    # Making GET request
    url = "http://localhost:8091/api/" + type.lower() + "s"
    r = requests.get(url, headers=header.headers)
    objects = r.text

    # Obtaining results
    dictionaries = []
    results = []
    objects = re.findall('\[\s+(([^\]]*\n*)*)\]', objects)[0][0]
    for object in objects.split(', '):
        dictionaries.append(ast.literal_eval(object))
    for dictionary in dictionaries:
        if (dictionary.has_key('name')):
            if (name_fragment.lower() in dictionary['name'].lower()):
                results.append(dictionary)
        elif (dictionary.has_key('fullName')):
            if (name_fragment.lower() in dictionary['fullName'].lower()):
                results.append(dictionary)
    return results

# Returns the Id of an object of given type that matches a given name
def GETId (name, type):
    
    # Getting list of objects of that type in dict form
    dictionaries = GETAll("", type)
    self = ""

    # Finding specified object
    if (type == ('license' or 'vendor')):
        for dictionary in dictionaries:
            if(dictionary['fullName'].lower() == name.lower()):
                self = str(dictionary['_links'])
    elif (type == 'release'):
        version = raw_input("Please specify the version of your release: ")
        for dictionary in dictionaries:
            if(dictionary['name'].lower() == name.lower()) and (dictionary['version'].lower() == version.lower()):
                self = str(dictionary['_links'])
    elif (type == ('component' or 'project')):   
        for dictionary in dictionaries:
            if(dictionary['name'].lower() == name.lower()):
                self = str(dictionary['_links'])

    #Getting Id
    if (self != ""):
        print self
        print idMatch
        idMatch = re.search('''["|']http://.*/(.*)["|']''', self)
        id = idMatch.group(1)
        return id

# Returns a given field from an object of given type that matches a given name
def GETField (name, type, field):

    # Getting list of objects of that type in dict form
    dictionaries = GETAll("", type)
    self = ""

    # Finding specified object and field
    if (type == ('license' or 'vendor')):
        for dictionary in dictionaries:
            if(dictionary['fullName'].lower() == name.lower()):
                try:
                    field = dictionary[field]
                except KeyError:
                    print "The specified field could not be found."
                    return
    elif (type == 'release'):
        version = raw_input("Please specify the version of your release. ")
        for dictionary in dictionaries:
            if(dictionary['name'].lower() == name.lower()) and (dictionary['version'].lower() == version.lower()):
                try:
                    field = dictionary[field]
                except KeyError:
                    print "The specified field could not be found."
                    return
    elif (type == ('component' or 'project')):   
        for dictionary in dictionaries:
            if(dictionary[field].lower() == name.lower()):
                try:
                    field = dictionary[field]
                except KeyError:
                    print "The specified field could not be found."
                    return
    return field

        
        
