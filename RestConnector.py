import re, json, requests, sys, ast
from FormatLicenseData import FormatLicenseData
from FormatVendorData import FormatVendorData
from FormatUserData import FormatUserData
from FormatComponentData import FormatComponentData
from FormatReleaseData import FormatReleaseData
from FormatProjectData import FormatProjectData

class RestConnector:

    global regex_id
    regex_id = '''["|']http://.*/([^\s\{\}]*)["|']'''
    global decoder
    decoder = json.JSONDecoder()
    
    global type_identifiers
    type_identifiers = {'license': 'fullName', 'vendor': 'fullName', 'component': 'name', 'release': 'name', 'project': 'name', 'user': 'email'}


    def __init__(self, url, headers):
        self.url = url
        self.headers = headers
        self.type_formatters = {'license': FormatLicenseData(),
                       'vendor': FormatVendorData(self),
                       'component': FormatComponentData(),
                       'release': FormatReleaseData(self),
                       'project': FormatProjectData(),
                       'user': FormatUserData()
                       }
        
    # Returns list of dictionaries of all objects of a type
    def get_all_objects(self, obj_type):

        # Getting list of ids
        if (not type_identifiers.has_key(obj_type)):
            print obj_type + " is not a valid type.\n"
            return None
        get_url = self.url + obj_type.lower() + "s"
        r = requests.get(get_url, headers=self.headers)
        if (r.status_code != 200):
            message = name + " (" + obj_type + "): " + "GET method was unsuccessful.\n" + r.text
            print message
            return None
        obj_ids = re.findall(regex_id, r.text)

        # Getting list of objects with all data
        objects = []
        for obj_id in obj_ids:
            obj = self.get_object_by_id(obj_id, obj_type)
            if (obj is not None):
                objects.append(obj)
        return objects

    # Returns dictionary of object w/ given name
    def get_object_by_name(self, name, obj_type, version = None):

        # Getting id of that object
        if (not type_identifiers.has_key(obj_type)):
            print obj_type + " is not a valid type.\n"
            return None
        obj_id = self.get_id_by_name(name, obj_type, version)
        if (obj_id is None):
            return None

        # Returning object
        return self.get_object_by_id(obj_id, obj_type)
    
    # Returns dictionary of object w/ given id
    def get_object_by_id (self, obj_id, obj_type):
        
        # Making GET request
        if (not type_identifiers.has_key(obj_type)):
            print obj_type + " is not a valid type.\n"
            return None
        get_url = self.url + obj_type.lower() + "s/" + obj_id
        r = requests.get(get_url, headers=self.headers)
        if (r.status_code != 200):
            message = obj_id + " (" + obj_type + "): " + "GET method was unsuccessful.\n" + r.text
            print message
            return None

        # Returning object
        dictionary = json.JSONDecoder.decode(decoder, r.text)
        return self.type_formatters[obj_type].get_format(dictionary)

    # Returning string id of object w/ given name
    def get_id_by_name(self, name, obj_type, version = None):
        
        # Getting list of objects of that type
        if (not type_identifiers.has_key(obj_type)):
            print obj_type + " is not a valid type."
            return None
        get_url = self.url + obj_type.lower() + "s"
        r = requests.get(get_url, headers=self.headers)
        if (r.status_code != 200):
            message = name + " (" + obj_type + "): " + "GET method was unsuccessful.\n" + r.text
            print message
            return None
        dictionaries = json.JSONDecoder.decode(decoder,r.text)
        dictionaries = dictionaries['_embedded']['sw360:'+obj_type+'s']

        # Finding specified object
        sw360_object = None
        for dictionary in dictionaries:
            if (obj_type.lower() == 'release'):
                if (version is None):
                    version = raw_input("Please specify the version of your release: ")
                if(dictionary['name'].lower() == name.lower()) and (dictionary['version'].lower() == version.lower()):
                    sw360_object = str(dictionary['_links'])
            else:
                if(dictionary[type_identifiers[obj_type]].lower() == name.lower()):
                    sw360_object = str(dictionary['_links'])

        # Getting id
        if (sw360_object is not None):
            idMatch = re.search(regex_id, sw360_object)
            obj_id = idMatch.group(1)
            return obj_id
        else:
            return None

    # Reads in file of valid JSON, returns list of dictionaries
    def format_objects_from_file (self, filepath):

        # Reading in information
        file = open(filepath, "r")
        info = file.read()
        
        # Making lists of objects
        dictionaries = []
        items = re.split('\}\s*\{|\}\s*$|^\{', info)
        for item in items[1:len(items)-1]:
            dictionary = ast.literal_eval("{" + item + "}")
            if (not dictionary.has_key('type')):
                print "You have not specified a type for all of your objects.\n"
                sys.exit()
            elif (not type_identifiers.has_key(dictionary['type'].lower())):
                print dictionary['type'] + " is not a valid type. The corresponding object will not be posted.\n"
            else:
                dictionaries.append(dictionary)
        if (dictionaries == []):
            print("You haven't provided any valid objects to POST.")
            return None
        return dictionaries

    # Takes list of dictionaries and makes POST requests
    def post_objects (self, POST_objects):

        # Sorting list by type means components will be posted before their corresponding releases - bit of a hack
        POST_objects = sorted(POST_objects, key=lambda k: k['type'])

        # Making post requests
        for obj in POST_objects:
            obj_type = obj['type'].lower()
            post_url = self.url + obj_type + "s"
            if (self.type_formatters[obj_type].post_format(obj) == 1):
                r = requests.post(post_url, headers=self.headers, json=obj)
                if (r.status_code == 201):
                    message = obj[type_identifiers[obj_type]] + " (" + obj_type + ")" + ": POST method was successful\n\n"
                    print message
                else:
                    message = obj[type_identifiers[obj_type]] + " (" + obj_type + ")" + ": POST method was unsuccessful\n" + r.text + "\n\n"
                    print message
