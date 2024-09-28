import urllib
url = 'https://data.hii.or.th/sv/api/3/action/datastore_search?limit=5&resource_id=e45c665d-8389-4bf1-889b-37c42ca200ee&q=title:jones'  
fileobj = urllib.urlopen(url)
print(fileobj.read())