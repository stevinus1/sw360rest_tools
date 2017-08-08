import json, global_vars

# Interpreting GET request text
def format_get(text):
    dictionary = json.JSONDecoder.decode(global_vars.decoder, text)
    del dictionary['_links']
    return dictionary
    
