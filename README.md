These scripts require the sw360 REST interface to run.
They also require the python requests module.

Templates for adding different types, with required fields labelled:

Component
{
  "type": "component (required)",
  "name": "COMPONENT_NAME (required)",
  "description": "Component description",
  "componentType": "OSS/COTS/INTERNAL/INNER_SOURCE/FREESOFTWARE/SERVICE",
  "vendors": ["VENDOR_ID1", "VENDOR_ID2"],
  "ownerAccountingUnit": "OWNER_ACCOUNTING_UNIT",
  "ownerGroup": "OWNER_GROUP"
}

Project
{
  "type": "project (required)",
  "name": "PROJECT_NAME (required)",
  "version": "PROJECT_VERSION",
  "description": "Project description",
  "projectType": "CUSTOMER/INTERNAL/PRODUCT/SERVICE",
  "businessUnit": "BUSINESS_UNIT",
  "externalIds": {"DESCRIPTION1": "ID1", "DESCRIPTION2": "ID2"},
  "releaseIdToUsage": {}
}

Release
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
}

License
{
  "type": "license" (required),
  "fullName": "LICENSE_NAME" (required),
  "shortName": "L_N" (required),
  "text": "License text"
}

Vendor
{
  "type": "vendor" (required),
  "fullName": "VENDOR_NAME" (required),
  "shortName": "V_N" (required),
  "url": "www.vendor.com" (required)
}

