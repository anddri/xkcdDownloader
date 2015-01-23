import urllib2
import re
from sys import argv

script, urlNumber = argv

def getImage(idNumber):
		
	for i in range(idNumber, 1, -1):

		if i == 404: # By some reason, the subpage 404 is not found :-)
			i = 403

		patternImg = r"imgs.xkcd.com/comics/\w*.png"
			
		response = urllib2.urlopen('http://xkcd.com/' + str(i))
		
		html = response.read()
		
		match = re.search(patternImg, html)
		
		if match:
			print "Found"
			fileUrl = str(match.group())
			print fileUrl 
		else:
			print "Did not found"
			print match
		
		f = urllib2.urlopen('http://' + fileUrl)
		
		data = f.read()
		
		with open(str(i) + '.png', 'wb') as code:
			code.write(data)

getImage(int(urlNumber))