
# Putting license data in dictionary structure
def format_license_data (license):
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
