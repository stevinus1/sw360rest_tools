import os, subprocess, re

# Getting request header
REST_filepath = raw_input("What is the filepath for the REST interface? ")
print "\n"
os.chdir(REST_filepath)
p = subprocess.Popen('./gradlew printAccessToken -Psw360args="http://localhost:8090,admin@sw360.org,sw360-admin-password"', stdout=subprocess.PIPE, shell=True)
(output, err) = p.communicate()
if (output != ""):
    accessToken = re.findall('Bearer (.*)\n', output)[0]
else:
    accessToken = "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJhdWQiOlsic3czNjAtUkVTVC1BUEkiXSwidXNlcl9uYW1lIjoiYWRtaW5Ac3czNjAub3JnIiwic2NvcGUiOlsic3czNjAucmVhZCIsInN3MzYwLndyaXRlIl0sImV4cCI6MTUxNDg4NDkzOSwiYXV0aG9yaXRpZXMiOlsiUk9MRV9TVzM2MF9VU0VSIl0sImp0aSI6IjE1MGQyZjY1LThmZGUtNGZmNi04MWZlLTE2MjkzMTAyMzQxZSIsImNsaWVudF9pZCI6InRydXN0ZWQtc3czNjAtY2xpZW50In0.H1QtpZXGZpzZiBNjM8-ac7n-ttXBJ1vJCU40SQk9MQt4ChOds6IKRDxk7TpTsMlTcgYJz6pDdce14EPXYtys_mf78AxJjkSCjTMjinf8Dm_yqj4_vpPao4AyvxGyEm3P75Wnsgaq9u82t7BYVsIuK_S_cUnTmnEEkYUO8lk_InHbXC3QPm64UN6s201lIV40rmt1iQGsqmieBIqhqdiHgvJHwyEyIEF3QjkC2OJth7fJRqEPVwEGvElNYIMjUFloViFRSkq8CiYmxZEshaG31UdCH0C8shujltGs2iM5v5ks0FpwxL3GSrXCN5MY6aJA-YW0-5vb1KOGpzLtXx7qAQ"
global headers
headers = {"Content-Type": "application/json", "Authorization": "Bearer " + accessToken, "Accept": "application/hal+json, application/json, */*; q=0.01"}