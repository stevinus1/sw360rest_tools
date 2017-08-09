import re

class FormatComponentData:

    global default_dict
    default_dict = {
        "componentType": "OSS",
        "description": "",
        "ownerAccountingUnit": "",
        "ownerGroup": "",
        "roles": {},
        "vendors": []
        }

    global regex_id
    regex_id = '''["|']http://.*/([^\s]*)["|']'''

    # Filling in fields in dictionary structure
    def post_format (self, component):
        if (component.has_key("name")):
            for key in default_dict.keys():
                component.setdefault(key, default_dict[key])
            return 1
        else:
            print "Please specify a name for your component."
            return 0

    # Interpreting GET request text
    def get_format(self, dictionary):
        dictionary['createdBy'] = dictionary['_embedded']['createdBy']['email']
        if dictionary.has_key('releases'):
            release_ids = []
            for release in dictionary['_embedded']['releases']:
                release_id = re.search(regex_id, str(release))
                release_ids.append(release_id.group(1))
            dictionary['releases'] = release_ids
        del dictionary['_embedded']
        del dictionary['_links']
        return dictionary
    
