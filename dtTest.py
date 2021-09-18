#!/usr/bin/python3


import time
import datetime
import requests
import dateparser


def convertUnix(epochTime):
	localTime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(epochTime))
	return localTime


def datetimeToUnix(ogDatetime):
	ogDatetime=datetime.datetime.strptime(ogDatetime, "%Y-%m-%d %H:%M:%S")
	unixTime = ogDatetime.strftime('%s')
	return unixTime


def addDays(ogDatetime, nDays):
	ogDtTypeStr = str(type(ogDatetime))
	if 'str' in ogDtTypeStr:	ogDatetime = dateparser.parse(ogDatetime)
	newDate = ogDatetime + datetime.timedelta(days=nDays)
	return newDate


def subtractDays(ogDatetime, nDays):
	ogDtTypeStr = str(type(ogDatetime))
	if 'str' in ogDtTypeStr:	ogDatetime = dateparser.parse(ogDatetime)
	newDate = ogDatetime - datetime.timedelta(days=nDays)
	return newDate



todayFull = datetime.datetime.now()
todaySplit = str(todayFull).split(".")
today = todaySplit[0]
print("Todays date: " + str(today))

unixTodayTest = datetimeToUnix(today)
print("\nTodays date in unix time: " + str(unixTodayTest))


addDaysTest = addDays(today, 14)
print("\nTwo weeks from now date: " + str(addDaysTest))

subtractDaysTest = subtractDays(today, 14)
print("\nTwo weeks ago date: " + str(subtractDaysTest))

