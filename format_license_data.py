import json, global_vars

# Putting license data in dictionary structure
def format_post (license):
    default_dict = {
        "text": ""
        }
    if (not license.has_key("shortName")):
        print "Please specify a shortName for your license.\n\n"
        return 0
    elif (not license.has_key("fullName")):
        print "Please specify a fullName for your license.\n\n"
        return 0
    else:
        for key in default_dict.keys():
            license.setdefault(key, default_dict[key])
        return 1

# Interpreting GET request text
def format_get(text):
    decoder = json.JSONDecoder()
    dictionary = json.JSONDecoder.decode(global_vars.decoder, text)
    del dictionary['_links']
    return dictionary
