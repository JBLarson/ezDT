#!/usr/bin/python3

import time
import datetime
import requests


def convertUnix(epochTime):
	localTime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(epochTime))
	return localTime


def datetimeToUnix(ogDatetime):
	ogDatetime=datetime.datetime.strptime(ogDatetime, "%Y-%m-%d %H:%M:%S")
	unixTime = ogDatetime.strftime('%s')

	return unixTime


todayFull = datetime.datetime.now()
todaySplit = str(todayFull).split(".")
today = todaySplit[0]

print(today)


unixToday = datetimeToUnix(today)
print(unixToday)



