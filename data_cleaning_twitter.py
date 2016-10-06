import re
import numpy as np
import pandas as pd
from bs4 import BeautifulSoup


tweetsDictionary = dict()

file = open('/Users/michaelmartin/Desktop/isis.txt', 'r')

for line in file:
	#replaces all the beginning tags with nothing
	line = line.replace('<TWEET>', '')
	line = line.replace('<TERM>', '')
	line = line.replace('<HANDLE>', '')
	line = line.replace('<ID>', '')
	line = line.replace('<TIME>', '')
	line = line.replace('<TEXT>', '')

	#replaces all the end tags with semi-colons to seperate the data easily
	line = line.replace('</TWEET>', '')
	line = line.replace('</TERM>', ';')
	line = line.replace('</HANDLE>', ';')
	line = line.replace('</ID>', ';')
	line = line.replace('</TIME>', ';')
	line = line.replace('</TEXT>', ';')

	textFields = line.split(';')

	hashTag = textFields[0]
	userHandle = textFields[1]
	tweetID = textFields[2]
	timeStamp = textFields[3]
	tweetText = textFields[4]

	tweetsDictionary[tweetID] = [hashTag, userHandle, timeStamp, tweetText]

myDataFrame = pd.DataFrame.from_dict(tweetsDictionary, orient='index')

print(myDataFrame)

					
