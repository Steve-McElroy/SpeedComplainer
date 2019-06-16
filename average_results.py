#! /usr/bin/python3.5

import os
import sys
import time
from datetime import datetime

# Empty lists to read in values from files and later used to calculate averages
pingResults = []
downloadResults = []
uploadResults = []

# Averages Method
def averages():

    # Create a timestamp
    timeStamp = time.time()
    date = datetime.fromtimestamp(timeStamp).strftime("%Y-%m-%d %H:%M:%S")

    # Average Ping
    with open("/home/pi/speedcomplainer/v1/pingResults.log", "r+") as pingFile:
        line = pingFile.readline()
        for line in pingFile:
            pingFloat = float(line)
            pingResults.append(pingFloat)

    lastHoursPings = pingResults[-12:]

    sumOfHourlyPings = sum(lastHoursPings)

    numOfPings = len(pingResults)
    sumOfPings = sum(pingResults)

    averagePing = sumOfPings / numOfPings
    averageHourlyPing = sumOfHourlyPings / 12

    # Average Download Speed
    with open("/home/pi/speedcomplainer/v1/downloadResults.log", "r+") as downloadFile:
        line = downloadFile.readline()
        for line in downloadFile:
            downloadFloat = float(line)
            downloadResults.append(downloadFloat)

    lastHoursDownloads = downloadResults[-12:]

    sumOfHourlyDownloads = sum(lastHoursDownloads)

    numOfDownloads = len(downloadResults)
    sumOfDownloads = sum(downloadResults)

    averageDownload = sumOfDownloads / numOfDownloads
    averageHourlyDownload = sumOfHourlyDownloads / 12

    # Average Upload Speed
    with open("/home/pi/speedcomplainer/v1/uploadResults.log", "r+") as uploadFile:
        line = uploadFile.readline()
        for line in uploadFile:
            uploadFloat = float(line)
            uploadResults.append(uploadFloat)

    lastHoursUploads = uploadResults[-12:]
    sumOfHourlyUploads = sum(lastHoursUploads)

    numOfUploads = len(uploadResults)
    sumOfUploads = sum(uploadResults)

    averageUpload = sumOfUploads / numOfUploads
    averageHourlyUpload = sumOfHourlyUploads / 12

    formattedResult = """######### %s #########

 Total number of tests completed: %d

 Total average ping: %.3f
 Average hourly ping: %.3f

 Total average download: %.3f
 Average hourly download: %.3f

 Total average upload: %.3f
 Average hourly upload: %.3f

#######################################\n
""" % (date, numOfUploads, averagePing, averageHourlyPing, averageDownload, averageHourlyDownload, averageUpload, averageHourlyUpload)

    print(formattedResult)

    with open("/home/pi/speedcomplainer/v1/averageTestResults.log", "a") as resultFile:
        resultFile.write(formattedResult)
        resultFile.close()

averages()
