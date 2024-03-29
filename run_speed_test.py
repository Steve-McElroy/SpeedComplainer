#! /usr/bin/python3.5

import os
import sys
import time
from datetime import datetime
from twython import Twython
from auth import (consumer_key, consumer_secret, access_token, access_token_secret)

# Expected download speed
expected = float(55.00)

# Initialise twitter
twitter = Twython(consumer_key, consumer_secret, access_token, access_token_secret)

# Method
def speedTest():

    # Create a timestamp
    timeStamp = time.time()
    date = datetime.fromtimestamp(timeStamp).strftime("%Y-%m-%d %H:%M:%S")

    # Run speed test
    speedTest = os.popen("python /usr/local/bin/speedtest-cli --simple --no-pre-allocate").read()

    # Parse values
    results = speedTest.split("\n")
    ping = results[0][6:11]
    downloadSpeed = results[1][10:14]
    uploadSpeed = results[2][8:12]

    # Format the results so they can be saved to a log
    formattedResult = """###### %s ######

 Ping (ms): %s
 Download Speed (Mb/s): %s
 Upload Speed (Mb/s): %s

############ TEST END ############\n
""" % (date, ping, downloadSpeed, uploadSpeed)

    # Save the results to a log called testResults.log
    with open("/home/pi/speedcomplainer/v1/testResults.log", "a") as resultFile:
        resultFile.write(formattedResult)
        resultFile.close()

    # Save each of the PING values to a list
    with open("/home/pi/speedcomplainer/v1/pingResults.log", "a") as pingFile:
        pingFile.write("%s\n" % ping)
        pingFile.close()

    # Save each of the DOWNLOAD values to a list
    with open("/home/pi/speedcomplainer/v1/downloadResults.log", "a") as downloadFile:
        downloadFile.write("%s\n" % downloadSpeed)
        downloadFile.close()

    # Save each of the UPLOAD values to a list
    with open("/home/pi/speedcomplainer/v1/uploadResults.log", "a") as uploadFile:
        uploadFile.write("%s\n" % uploadSpeed)
        uploadFile.close()

speedTest()
