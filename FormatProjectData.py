
# Putting project data in dictionary structure
def FormatProjectData (project):
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
