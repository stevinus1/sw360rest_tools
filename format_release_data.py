import GET

# Putting release data in dictionary structure
def format_release_data (release, component):
    Component_Id = GET.get_id(component['name'], 'component')
    default_dict = {
        "componentId": Component_Id,
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





