class FormatVendorData:
    
    def __init__(self, rest_connector):
        self.connector = rest_connector

    # Filling in fields in dictionary structure
    def post_format (self, vendor):
        if (not vendor.has_key("shortName")):
            print "Please specify a shortName for your vendor.\n\n"
            return 0
        elif (not vendor.has_key("fullName")):
            print "Please specify a fullName for your vendor.\n\n"
            return 0
        elif (not vendor.has_key("url")):
            print "Please specify an url for your vendor.\n\n"
            return 0
        elif (self.connector.get_object_by_name(vendor['fullName'], 'vendor') is not None):
            print vendor['fullName'] + " (vendor): There is already a vendor with that name\n" 
            return 0
        else:
            return 1

    # Interpreting GET request text
    def get_format(self, dictionary):
        del dictionary['_links']
        return dictionary
