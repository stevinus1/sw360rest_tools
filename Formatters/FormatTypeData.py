class FormatTypeData:
    
    required_fields = {'license': ['fullName', 'shortName'],
                       'vendor': ['fullName', 'shortName', 'url'],
                       'component': ['name'],
                       'release': ['name', 'cpeId', 'version'],
                       'project': ['name']
                       }

    def __init__ (self):
        self.default_dict = {}
        self.object_type = ''

    # Filling in fields in dictionary structure
    def post_format (self, dictionary):
        for field in self.required_fields[self.object_type]:
            if (not dictionary.has_key(field)):
                print 'Please specify a ' + field + ' for your ' + self.object_type + '.'
                return 0
        for key in self.default_dict.keys():
            dictionary.setdefault(key, self.default_dict[key])
        return 1

    # Interpreting GET request text
    def get_format(self, dictionary):
        if (dictionary.has_key('_embedded')):
            del dictionary['_embedded']
        del dictionary['_links']
        return dictionary
