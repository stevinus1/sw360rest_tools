import subprocess, requests, sys, ast, os, re
import FormatProjectData, FormatComponentData, FormatVendorData, FormatReleaseData, FormatLicenseData
import GET, header

# Reading in information
info_filepath = raw_input("What is the filepath for the information? ")
print "\n"
file = open(info_filepath, "r")
info = file.read()

# Making lists of components and projects
items = []
dicts = []
components = []
projects = []
vendors = []
releases = []
licenses = []
items = p = re.findall('(\{\s+(([^\}]*?\n+[^\}]*?)*)\})', info)
for item in items:
    dicts.append(ast.literal_eval(item[0]))
for di in dicts:
    if di['type'].lower() == 'project':
        projects.append(di)
    elif di['type'].lower() == 'component':
        components.append(di)
    elif di['type'].lower() == 'vendor':
        vendors.append(di)
    elif di['type'].lower() == 'release':
        releases.append(di)
    elif di['type'].lower() == 'license':
        licenses.append(di)
    else:
        print("Please specify valid types for all your objects.")
        sys.exit()
if (dicts == []):
    print("You haven't provided any objects to POST.")
    sys.exit()
    
# Adding in any missing fields to dictionaries and making POST requests for projects
for project in projects:
    url = "http://localhost:8091/api/projects"
    if (FormatProjectData.FormatProjectData(project) == 1):
        r = requests.post(url, headers=header.headers, json=project)
        if (r.status_code == 201):
            print project['name'] + " (Project)" + ": POST method was successful\n\n"
        else:
            print project['name'] + " (Project)" + ": POST method was unsuccessful\n" + r.text + "\n\n"

# Adding in any missing fields to dictionaries and making POST requests for vendors
for vendor in vendors:
    url = "http://localhost:8091/api/vendors"
    if (FormatVendorData.FormatVendorData(vendor) == 1):
        r = requests.post(url, headers=header.headers, json=vendor)
        if (r.status_code == 201):
            print vendor['shortName'] + " (Vendor)" + ": POST method was successful\n\n"
        else:
            print vendor['shortName'] + " (Vendor)" + ": POST method was unsuccessful\n" + r.text + "\n\n"

# Adding in any missing fields to dictionaries and making POST requests for components
for component in components:
    url = "http://localhost:8091/api/components"
    if (FormatComponentData.FormatComponentData(component) == 1):
        r = requests.post(url, headers=header.headers, json=component)
        if (r.status_code == 201):
            print component['name'] + " (Component)" + ": POST method was successful\n\n"
        else:
            print component['name'] + " (Component)" +  ": POST method was unsuccessful\n" + r.text + "\n\n"

# Adding in any missing fields to dictionaries and making POST requests for releases
if (releases != []):
    stored_components = GET.GETAll('', 'component')
for release in releases:
    url = "http://localhost:8091/api/releases"
    has_component = 0
    for component in stored_components:
        if (component['name'] == release['name']):
            this_component = component
            has_component = 1
    if (has_component == 0):
        print "A release cannot exist independently of a component of the same name.\n\n"
        break
    if (FormatReleaseData.FormatReleaseData(release, this_component) == 1):
        r = requests.post(url, headers=header.headers, json=release)
        if (r.status_code == 201):
            print release['name'] + " (Release)" + ": POST method was successful\n\n"
        else:
            print release['name'] + " (Release)" + ": POST method was unsuccessful\n" + r.text + "\n\n"

# Adding in any missing fields to dictionaries and making POST requests for licenses
for license in licenses:
    url = "http://localhost:8091/api/licenses"
    if (FormatLicenseData.FormatLicenseData(license) == 1):
        r = requests.post(url, headers=header.headers, json=license)
        if (r.status_code == 201):
            print license['shortName'] + " (License)" +  ": POST method was successful\n\n"
        else:
            print license['shortName'] + " (License)" + ": POST method was unsuccessful\n" + r.text + "\n\n"
