class FormatLicenseData:

    global default_dict
    default_dict = {
        "text": ""
        }

    # Filling in fields in dictionary structure
    def post_format (self, license):

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
    def get_format(self, dictionary):
        del dictionary['_links']
        return dictionary
