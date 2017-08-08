import json, re, global_vars

# Putting release data in dictionary structure for POST
def format_post (release, component_id):
    default_dict = {
        "componentId": component_id,
        "vendorId": "",
        "externalIds": {},
        "mainLicenseIds": [],
        "clearingState": "NEW_CLEARING"
        }
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
        return 1

# Interpreting GET request text
def format_get(text):
    dictionary = json.JSONDecoder.decode(global_vars.decoder, text)
    component_id_match = re.search(global_vars.id_pattern,
    str(dictionary['_links']['sw360:component']))
    dictionary['componentId'] = component_id_match.group(1)
    if (dictionary.has_key('_embedded')):
        vendor_id_match = re.search(global_vars.id_pattern,
        str(dictionary['_embedded']['vendor']))
        dictionary['vendorId'] = vendor_id_match.group(1)
    del dictionary['_links']
    del dictionary['_embedded']
    return dictionary
    




