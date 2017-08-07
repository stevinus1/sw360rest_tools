
# Putting component data in dictionary structure
def FormatComponentData (component):
    default_dict = {
      "componentType": "OSS",
      "ownerAccountingUnit": "",
      "ownerGroup": "",
      "roles": {},
      "vendors": [],
      "releases": [],
      "moderators": []
    }
    if (component.has_key("name")):
        for key in default_dict.keys():
            component.setdefault(key, default_dict[key])
        return 1
    else:
        print "Please specify a name for your component."
        return 0