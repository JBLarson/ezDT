#!/usr/bin/python3

import time
import datetime
import requests


def convertUnix(epochTime):
	localTime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(epochTime))
	return localTime


def datetimeToEpoch(ogDatetime):
	ogDatetime=datetime.datetime.strptime(ogDatetime, "%Y-%m-%d %H:%M:%S")
	epochTime = ogDatetime.strftime('%s')

	return epochTime


todayFull = datetime.datetime.now()
todaySplit = str(todayFull).split(".")
today = todaySplit[0]

print(today)


unixToday = convertUnix(today)
print(unixToday)



