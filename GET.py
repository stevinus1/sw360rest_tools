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
    objects = re.findall('\[\s+(([^\]]*?\n+[^\]]*?)*)\]', objects)[0][0]
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

    # Finding Id of specified object
    for dictionary in dictionaries:
        if (dictionary.has_key('fullName')):
            if(dictionary['fullName'].lower() == name.lower()):
                self = str(dictionary['_links'])
        if (dictionary.has_key('name')):
            if(dictionary['name'].lower() == name.lower()):
                self = str(dictionary['_links'])
    id = re.findall('''["|']http://.*/(.*)["|']''', self)[0]
    return id
        
        
