import os, subprocess, re

class RestAuthenticator:
    
    def __init__(self, rest_filepath):
        self.headers = ""
        self.rest_filepath = rest_filepath
        
    def get_headers(self):
        
        # Moving to correct directory
        original_dir = os.getcwd()
        try:
            os.chdir(self.rest_filepath)
        except OSError as err:
            err.message = "OS Error: " + err.strerror
            raise OSError(err.message)
        
        # Getting access token
        p = subprocess.Popen('./gradlew printAccessToken -Psw360args="http://localhost:8090,admin@sw360.org,sw360-admin-password"', stdout=subprocess.PIPE, shell=True)
        (output, err) = p.communicate()
        if (output != ""):
            accessTokenMatch = re.search('Bearer (.*)\n', output)
            accessToken = accessTokenMatch.group(1)
        else:
            print "Failed to retrieve access token."
            os.chdir(original_dir)
            return 0

        # Creating header dictionary
        self.headers = {"Content-Type": "application/json", "Authorization": "Bearer " + accessToken, "Accept": "application/hal+json, application/json, */*; q=0.01"}
        os.chdir(original_dir)
        return 1
