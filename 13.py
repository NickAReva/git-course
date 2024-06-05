import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# Detached HEAD

while True:
    address = input('Enter location: ')
    if len(address) < 1: break

    url = address
    print('Retrieving', url)
    uh = urllib.request.urlopen(url, context=ctx)

    data = uh.read()
    print('Retrieved', len(data), 'characters')
    tree = ET.fromstring(data)

    results = tree.findall('comments/comment')
    print('Count:', len(results))
    
    count = 0
    for item in results:
        count = count + int(item.find('count').text)
    print('Sum:', count)