import GET, json, global_vars

# Putting project data in dictionary structure
def format_post (vendor):
    if (not vendor.has_key("shortName")):
        print "Please specify a shortName for your vendor.\n\n"
        return 0
    elif (not vendor.has_key("fullName")):
        print "Please specify a fullName for your vendor.\n\n"
        return 0
    elif (not vendor.has_key("url")):
        print "Please specify an url for your vendor.\n\n"
        return 0
    if (GET.get_object(vendor['fullName'], 'vendor') is not None):
        print vendor['fullName'] + " (Vendor): There is already a vendor with that name.\n\n"
        return 0
    else:
        return 1

# Interpreting GET request text
def format_get(text):
    dictionary = json.JSONDecoder.decode(global_vars.decoder, text)
    del dictionary['_links']
    return dictionary
