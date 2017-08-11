import re

class FormatReleaseData:

    global default_dict
    default_dict = {
        "componentId": "",
        "vendorId": "",
        "externalIds": {},
        "mainLicenseIds": [],
        "clearingState": "NEW_CLEARING"
        }
    
    global regex_id
    regex_id = '''["|']http://.*/([^\s]*)["|']'''

    def __init__(self, rest_connector):
        self.connector = rest_connector
        
    # Filling in fields in dictionary structure
    def post_format (self, release):
        if (not release.has_key("name")):
            print "Please specify a name for your release."
            return 0
        elif (not release.has_key("cpeId")):
            print "Please specify a cpeId for your release."
            return 0
        elif (not release.has_key("version")):
            print "Please specify a version for your release."
            return 0
        else:
            for key in default_dict.keys():
                release.setdefault(key, default_dict[key])
            for component in self.connector.get_all_objects('component'):
                if (release['name'] == component['name']):
                   release['componentId'] = self.connector.get_id_by_name(component['name'], 'component')
        return 1
        
    # Interpreting GET request text
    def get_format(self, dictionary):
        component_id_match = re.search(regex_id, str(dictionary['_links']['sw360:component']))
        dictionary['componentId'] = component_id_match.group(1)
        if (dictionary.has_key('_embedded')):
            vendor_id_match = re.search(regex_id, str(dictionary['_embedded']['vendor']))
            dictionary['vendorId'] = vendor_id_match.group(1)
        if dictionary.has_key('_embedded'):
            del dictionary['_embedded']
        del dictionary['_links']
        return dictionary
    




