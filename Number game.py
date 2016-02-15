import urllib.request
htmlsource, headers = urllib.request.urlretrieve('https://www.google.com/')
htmlsourcetext = open(htmlsource)
print (htmlsourcetext)

