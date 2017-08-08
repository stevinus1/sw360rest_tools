import global_vars, json

# Putting project data in dictionary structure
def format_post (project):
    default_dict = {
        "description": "",
        "version": "",
        "businessUnit": "DEPARTMENT",
        "projectType": "CUSTOMER",
        "clearingState": "OPEN",
        "roles": {},
        "releaseIdToUsage": {},
        "projectOwner": "",
        "ownerAccountingUnit": "",
        "ownerGroup": "",
        "externalIds": {},
        }
    if (project.has_key("name")):
        for key in default_dict.keys():
            project.setdefault(key, default_dict[key])
            return 1
    else:
        print "Please specify a name for your project."
        return 0

# Interpreting GET request text
def format_get(text):
    dictionary = json.JSONDecoder.decode(global_vars.decoder, text)
    dictionary['createdBy'] = dictionary['_embedded']['createdBy']['email']
    del dictionary['_embedded']
    del dictionary['_links']
    return dictionary
    
