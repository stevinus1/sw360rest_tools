# sw360 rest Example Client

These are scripts intended to be used to automate workflow when using the sw360 REST interface. The scripts require the sw360 REST interface to run, as well as the python requests module.

### POST:

POST requests can be made by creating a file containing formatted data for all the objects you want to add to sw360. Templates for adding different types, with required fields labelled, are below.

- Component  
```{  
  "type": "component (required)",  
  "name": "COMPONENT_NAME (required)",  
  "description": "Component description",  
  "componentType": "OSS/COTS/INTERNAL/INNER_SOURCE/FREESOFTWARE/SERVICE",  
  "vendors": ["VENDOR_ID1", "VENDOR_ID2"],  
  "ownerAccountingUnit": "OWNER_ACCOUNTING_UNIT",  
  "ownerGroup": "OWNER_GROUP"  
}```

- Project  
```{  
  "type": "project (required)",  
  "name": "PROJECT_NAME (required)",  
  "version": "PROJECT_VERSION",  
  "description": "Project description",  
  "projectType": "CUSTOMER/INTERNAL/PRODUCT/SERVICE",  
  "businessUnit": "BUSINESS_UNIT",  
  "externalIds": {"DESCRIPTION1": "ID1", "DESCRIPTION2": "ID2"},  
  "releaseIdToUsage": {}  
}```

- Release  
```{  
  "type": "release" (required),  
  "name": "RELEASE_NAME" (required),  
  "version": "RELEASE_VERSION" (required),  
  "componentId": "COMPONENT_ID" (required),  
  "cpeId": "cpeId" (required),  
  "vendorId": "VENDOR_ID",  
  "externalIds": {"DESCRIPTION1": "ID1", "DESCRIPTION2": "ID2"},  
  "mainLicenseIds": ["ID1", "ID2"],  
  "clearingState": "CLEARING_STATE"  
}```

- License  
```{  
  "type": "license" (required),  
  "fullName": "LICENSE_NAME" (required),  
  "shortName": "L_N" (required),  
  "text": "License text"  
}```

- Vendor  
```{  
  "type": "vendor" (required),  
  "fullName": "VENDOR_NAME" (required),  
  "shortName": "V_N" (required),  
  "url": "VENDOR_URL" (required)  
}```

Users can't be added via the REST interface.

### GET:

All GET methods are only capable of returning the information shown in the templates above.

- get_all: Takes a name fragment and type as strings, and returns a list of dictionaries containing short summary data about all objects of that type that contain that name fragment.

- get_object: Takes a name/fullName/email and type as strings, and returns a dictionary for the corresponding object containing all available data (for releases, the script will also request version).

- get_id: Takes a name/fullName/email and a type as strings, and returns the string Id of that object (for releases, the script will also request version).

- get_field: Takes a name/fullName/email, a field and a type as strings, and returns the specified field of that object (for releases, the script will also request version). The return type will be the type of that field.


