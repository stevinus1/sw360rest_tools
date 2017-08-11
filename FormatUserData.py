class FormatUserData:

    # Preventing POST request
    def post_format(self, dictionary):
        print dictionary['email'] + "(user): Users cannot be posted\n"
        return 0
    
    # Interpreting GET request text
    def get_format(self, dictionary):
        del dictionary['_links']
        return dictionary
    
