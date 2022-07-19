import urllib.request, urllib.parse, urllib.error
import json
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input("Enter URL : ")
print('Retrieving : ', url)
uh = urllib.request.urlopen(url, context=ctx)

data = uh.read()
print('Retrieved', len(data), 'characters')
info = json.loads(data)
print('Count : ', len(info['comments']))
sum=0
for i in range(0, len(info['comments'])):
    sum = sum + int(info['comments'][i]["count"])
print("Sum : ",sum)
