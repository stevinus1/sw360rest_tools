# sw360 REST Example Client

These are scripts intended to be used to automate workflow when using the sw360 REST interface. The scripts require the sw360 REST interface to run, as well as the python requests module.

### POST:

- post_objects: Takes a list of formatted dictionaries and posts all the objects contained therein.

For successful POST methods, the following template must be followed, with all required fields included:

[{  
  "type": "component (required)",  
  "name": "COMPONENT_NAME (required)",  
  "description": "Component description",  
  "componentType": "OSS/COTS/INTERNAL/INNER_SOURCE/FREESOFTWARE/SERVICE",  
  "vendors": ["VENDOR_ID1", "VENDOR_ID2"],  
  "ownerAccountingUnit": "OWNER_ACCOUNTING_UNIT",  
  "ownerGroup": "OWNER_GROUP"  
},
{  
  "type": "project (required)",  
  "name": "PROJECT_NAME (required)",  
  "version": "PROJECT_VERSION",  
  "description": "Project description",  
  "projectType": "CUSTOMER/INTERNAL/PRODUCT/SERVICE",  
  "businessUnit": "BUSINESS_UNIT",  
  "externalIds": {"DESCRIPTION1": "ID1", "DESCRIPTION2": "ID2"},  
  "releaseIdToUsage": {}  
},  
{  
  "type": "release" (required),  
  "name": "RELEASE_NAME" (required),  
  "version": "RELEASE_VERSION" (required),  
  "componentId": "COMPONENT_ID" (required),  
  "cpeId": "cpeId" (required),  
  "vendorId": "VENDOR_ID",  
  "externalIds": {"DESCRIPTION1": "ID1", "DESCRIPTION2": "ID2"},  
  "mainLicenseIds": ["ID1", "ID2"],  
  "clearingState": "CLEARING_STATE"  
},  
{  
  "type": "license" (required),  
  "fullName": "LICENSE_NAME" (required),  
  "shortName": "L_N" (required),  
  "text": "License text"  
},  
{  
  "type": "vendor" (required),  
  "fullName": "VENDOR_NAME" (required),  
  "shortName": "V_N" (required),  
  "url": "VENDOR_URL" (required)  
}]

Users can't be added via the REST interface.

### GET:

All GET methods are only capable of returning the information shown in the templates above. All searches by name are case insensitive. All get methods also have optional fields to allow you to specify whether or not to write the data to file, and where to write it to.

- get_all: Takes a type as a string, and returns a list of dictionaries containing short summary data about all objects of that type.

- get_objects_by_name_fragment: Takes a name fragment as a string and returns list of dictionaries corresponding to all objects of any type that contain that fragment

- get_object_by_name: Takes a name/fullName/email and type as strings, and returns a dictionary for the corresponding object (for releases, the script will also request version).

- get_object_by_id: Takes an Id and type as strings, and returns a dictionary for the corresponding object (for releases, the script will also request version).

- get_id_by_name: Takes a name/fullName/email and a type as strings, and returns the string Id of that object (for releases, the script will also request version).

### Helper Methods

- format_objects_from_file: Takes a local file path containing valid JSON and formats it to sw360 postable python dictionaries.

- write_objects_to_file: Takes a list of dictionaries/single dictionary and a filepath and writes the data to that file in valid JSON. The objects can then be re-uploaded via the post methods.


