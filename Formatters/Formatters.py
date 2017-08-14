from FormatTypeData import FormatTypeData
import re

class FormatLicenseData(FormatTypeData, object):

    def __init__ (self):
        self.default_dict = {"text": ""}
        self.object_type = 'license'

class FormatUserData(FormatTypeData, object):

    # Preventing POST request
    def post_format(self, dictionary):
        print dictionary['email'] + "(user): Users cannot be posted\n"
        return 0

class FormatVendorData(FormatTypeData, object):
    
    def __init__(self, rest_connector):
        self.connector = rest_connector
        self.default_dict = {}
        self.object_type = 'vendor'

    def post_format (self, vendor):
        if (super(FormatVendorData, self).post_format(vendor) == 0):
            return 0
        if (self.connector.get_object_by_name(vendor['fullName'], 'vendor') is not None):
            print vendor['fullName'] + " (vendor): There is already a vendor with that name\n" 
            return 0
        return super(FormatVendorData, self).post_format(vendor)

class FormatProjectData(FormatTypeData, object):
    
    def __init__(self):
        self.default_dict = {
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
            "externalIds": {}
            }
        self.object_type = 'project'

    def get_format(self, dictionary):
        dictionary['createdBy'] = dictionary['_embedded']['createdBy']['email']
        del dictionary['_embedded']
        del dictionary['_links']
        return dictionary

class FormatComponentData(FormatTypeData, object):

    global regex_id
    regex_id = '''["|']http://.*/([^\s]*)["|']'''
    
    def __init__(self):
        self.default_dict = {
        "componentType": "OSS",
        "description": "",
        "ownerAccountingUnit": "",
        "ownerGroup": "",
        "roles": {},
        "vendors": []
        }
        self.object_type = 'component'

    def get_format(self, dictionary):
        dictionary['createdBy'] = dictionary['_embedded']['createdBy']['email']
        if dictionary.has_key('releases'):
            release_ids = []
            for release in dictionary['_embedded']['releases']:
                release_id = re.search(regex_id, str(release))
                release_ids.append(release_id.group(1))
            dictionary['releases'] = release_ids
        del dictionary['_embedded']
        del dictionary['_links']
        return dictionary
            

class FormatReleaseData(FormatTypeData, object):

    global regex_id
    regex_id = '''["|']http://.*/([^\s]*)["|']'''
    
    def __init__(self, rest_connector):
        self.connector = rest_connector
        self.default_dict = {
        "componentId": "",
        "vendorId": "",
        "externalIds": {},
        "mainLicenseIds": [],
        "clearingState": "NEW_CLEARING"
        }
        self.object_type = 'release'

    def post_format(self, release):
        has_component = False
        for component in self.connector.get_all_objects('component'):
            if (release['name'] == component['name']):
                release['componentId'] = self.connector.get_id_by_name(component['name'], 'component')
                has_component = True
        if (has_component == False):
            print release['name'] + " (release): A release must have a corresponding component\n"
            return 0
        return super(FormatReleaseData, self).post_format(release)
        
    def get_format(self, dictionary):
        component_id_match = re.search(regex_id, str(dictionary['_links']['sw360:component']))
        dictionary['componentId'] = component_id_match.group(1)
        if (dictionary.has_key('_embedded')):
            vendor_id_match = re.search(regex_id, str(dictionary['_embedded']['vendor']))
            dictionary['vendorId'] = vendor_id_match.group(1)
        if dictionary.has_key('_embedded'):
            del dictionary['_embedded']
        del dictionary['_links']
        return dictionary
            


        
