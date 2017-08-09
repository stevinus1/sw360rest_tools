class FormatProjectData:

    global default_dict
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

    # Filling in fields in dictionary structure
    def post_format (self, project):
        if (project.has_key("name")):
            for key in default_dict.keys():
                project.setdefault(key, default_dict[key])
                return 1
        else:
            print "Please specify a name for your project."
            return 0

    # Interpreting GET request text
    def get_format(self, dictionary):
        dictionary['createdBy'] = dictionary['_embedded']['createdBy']['email']
        del dictionary['_embedded']
        del dictionary['_links']
        return dictionary
    
