import GET
# Putting project data in dictionary structure
def format_vendor_data (vendor):
    if (not vendor.has_key("shortName")):
        print "Please specify a shortName for your vendor.\n\n"
        return 0
    elif (not vendor.has_key("fullName")):
        print "Please specify a fullName for your vendor.\n\n"
        return 0
    elif (not vendor.has_key("url")):
        print "Please specify an url for your vendor.\n\n"
        return 0
    for existing_vendor in GET.GETAll("", 'vendor'):
        if (existing_vendor['fullName'] == vendor['fullName']):
            print "There is already a vendor with that name.\n\n"
            return 0
    else:
        return 1
