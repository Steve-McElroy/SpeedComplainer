#! /usr/bin/python3.5

import os
import sys
import time
from datetime import datetime
from twython import Twython
from auth import (consumer_key, consumer_secret, access_token, access_token_secret)

def every15minutes():

    twitter = Twython(consumer_key, consumer_secret, access_token, access_token_secret)

    downloadResults = []
    uploadResults = []
    pingResults = []

    dTweet = "Worst values from last 3 tests run\nTests run every five minutes\n"

    with open("/home/pi/speedcomplainer/v1/downloadResults.log", "r+") as downloadFile:
        for line in (downloadFile.readlines()[-3:]):
            downloadFloat = float(line)
            downloadResults.append(downloadFloat)

    with open("/home/pi/speedcomplainer/v1/uploadResults.log", "r+") as uploadFile:
        for line in (uploadFile.readlines()[-3:]):
            uploadFloat = float(line)
            uploadResults.append(uploadFloat)

    with open("/home/pi/speedcomplainer/v1/pingResults.log", "r+") as pingFile:
        for line in (pingFile.readlines()[-3:]):
            pingFloat = float(line)
            pingResults.append(pingFloat)

    minDownload = min(downloadResults)

    if minDownload >= 45.00:
        d1 = "\nDownload speed looking good: %.2f\n" % minDownload
        dTweet+=d1
    elif minDownload  >= 35.00:
        d2 = "\nDownload speed could be better: %.2fMb/s\n" % minDownload
        dTweet+=d2
    elif minDownload >= 25.00:
        d3 = "\nDownload speed looking weak: %.2fMb/s\n" % minDownload
        dTweet+=d3
    elif minDownload >= 0.00:
        d4 = "\nDownload speed abysmal: %.2fMb/s\n" % minDownload
        dTweet+=d4

    minUpload = min(uploadResults)

    if minUpload >= 13.00:
        u1 = "Upload speed looking good: %.2fMb/s\n" % minUpload
        dTweet+=u1
    elif minDownload  >= 8.00:
        u2 = "Upload speed could be better: %.2fMb/s\n" % minUpload
        dTweet+=u2
    elif minDownload >= 4.00:
        u3 = "Upload speed looking weak: %.2fMb/s\n" % minUpload
        dTweet+=u3
    elif minDownload >= 0.00:
        u4 = "Upload speed abysmal: %.2fMb/s\n" % minUpload
        dTweet+=u4

    minPing = min(pingResults)

    if minPing >= 200.00:
        p1 = "Ping is terrible: %.2fms\n" % minPing
        dTweet+=p1
    elif minPing >= 100.00:
        p2 = "Ping is pretty weak: %.2fms\n" % minPing
        dTweet+=p2
    elif minPing >= 50.00:
        p3 = "Ping is decent: %.2fms\n" % minPing
        dTweet+=p3
    elif minPing >= 25.00:
        p4 = "Ping is good: %.2fms\n" % minPing
        dTweet+=p2
    elif minPing >= 0.00:
        p5 = "Ping is awseome: %.2fms\n" % minPing
        dTweet+=p5

    dTweet+="\n#Python #RaspberryPi #SpeedTest"

    twitter.update_status(status=dTweet)
    #print(dTweet)

every15minutes()
