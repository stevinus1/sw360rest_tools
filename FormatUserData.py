class FormatUserData:

    # Interpreting GET request text
    def get_format(self, dictionary):
        del dictionary['_links']
        return dictionary
    
