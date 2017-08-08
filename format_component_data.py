import global_vars, json, re

# Putting component data in dictionary structure
def format_post (component):
    default_dict = {
      "componentType": "OSS",
      "description": "",
      "ownerAccountingUnit": "",
      "ownerGroup": "",
      "roles": {},
      "vendors": []
    }
    if (component.has_key("name")):
        for key in default_dict.keys():
            component.setdefault(key, default_dict[key])
        return 1
    else:
        print "Please specify a name for your component."
        return 0

# Interpreting GET request text
def format_get(text):
    dictionary = json.JSONDecoder.decode(global_vars.decoder, text)
    dictionary['createdBy'] = dictionary['_embedded']['createdBy']['email']
    release_ids = []
    for release in dictionary['_embedded']['releases']:
        release_id = re.search(global_vars.id_pattern, str(release))
        release_ids.append(release_id.group(1))
    dictionary['releases'] = release_ids
    del dictionary['_embedded']
    del dictionary['_links']
    return dictionary
    
