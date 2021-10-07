
import time
import datetime


def unixToDatetime(epochTime):
	epochTime = int(epochTime)
	localTime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(epochTime))
	return localTime


def datetimeToUnix(ogDatetime):
	if '/' in ogDatetime:
		ogDatetime = ogDatetime.replace("/", "-")

	try:	ogDatetime=datetime.datetime.strptime(ogDatetime, "%Y-%m-%d %H:%M:%S")
	except Exception as e:
		exception0 = str("1st Error with datetimeToUnix: " + str(e))

		try:	ogDatetime=datetime.datetime.strptime(ogDatetime, "%Y-%m-%d")
		except Exception as e:
			exception1 = str("2nd Error with datetimeToUnix: " + str(e))

			try:	ogDatetime=datetime.datetime.strptime(ogDatetime, "%m-%d-%Y")
			except Exception as e:
				exception2 = str("3rd Error with datetimeToUnix: " + str(e))
				print(exception0 + "\n" + exception1 + "\n" + exception2)

	unixTime = ogDatetime.strftime('%s')
	return unixTime



def strToDT(ogDTstr):
	format = "%Y-%m-%d %H:%M:%S"
	dt_object = datetime.datetime.strptime(ogDTstr, format)
	return dt_object


def addDays(ogDatetime, nDays):
	ogDtTypeStr = str(type(ogDatetime))
	if 'str' in ogDtTypeStr:	
		ogDatetime = strToDT(ogDatetime)
	newDate = ogDatetime + datetime.timedelta(days=nDays)
	return newDate


def subtractDays(ogDatetime, nDays):
	ogDtTypeStr = str(type(ogDatetime))
	if 'str' in ogDtTypeStr:
		ogDatetime = strToDT(ogDatetime)
	newDate = ogDatetime - datetime.timedelta(days=nDays)
	return newDate


def today():
	todayFull = datetime.datetime.now()
	todaySplit = str(todayFull).split(".")
	today = todaySplit[0]
	return today



