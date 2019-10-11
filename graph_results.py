#! /usr/bin/python3.5

import os
import sys
import time
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime
from twython import Twython
from auth import (consumer_key, consumer_secret, access_token, access_token_secret)

# Empty lists to read in values from files and later used to calculate averages
maxSpeed = np.full(48, 74, dtype=float)
minSpeed = np.full(48, 34, dtype=float)
minUpload = np.full(48, 20, dtype=float)
last4HoursDownloads = []
last4HoursUploads = []

# Initialise twitter
twitter = Twython(consumer_key, consumer_secret, access_token, access_token_secret)

# Graph Method
def graph_results():

    # Create a timestamp
    timeStamp = time.time()
    dateShort = datetime.fromtimestamp(timeStamp).strftime("%y-%m-%d %H:%M")

    # Average Download Speed
    with open("/home/pi/speedcomplainer/v1/downloadResults.log", "r+") as downloadFile:
        for line in (downloadFile.readlines()[-48:]):
            downloadFloat = float(line)
            last4HoursDownloads.append(downloadFloat)

    # Average Upload Speed
    with open("/home/pi/speedcomplainer/v1/uploadResults.log", "r+") as uploadFile:
        for line in (uploadFile.readlines()[-48:]):
            uploadFloat = float(line)
            last4HoursUploads.append(uploadFloat)

    # Set grid
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)

    # Major ticks every 10, minor ticks every 5 (for y)
    major_ticks = np.arange(0, 116, 10)
    minor_ticks = np.arange(0, 116, 5)

    # Ticks for x
    x_minor_ticks = np.arange(0, 101, 12)

    ax.set_xticks(x_minor_ticks, minor=True)
    ax.set_yticks(major_ticks)
    ax.set_yticks(minor_ticks, minor=True)

    # And a corresponding grid
    ax.grid(which='both')
    plt.title("Actual Download Speed VS. Expected Download Speed")

    # Axes labels
    plt.xlabel("4 Hours Of Results\nTest Runs Every 5 Minutes")
    plt.xticks([])

    plt.ylabel("Mb/s")
    plt.ylim(0, 115)

    # Plot Values
    plt.plot(maxSpeed, label="Max: 74Mb/s", color="g")
    plt.plot(last4HoursDownloads, label="Actual DL Speed", marker=".", color="b")
    plt.plot(last4HoursUploads, label="Actual UL Speed", marker=".", color="y")
    plt.plot(minSpeed, label="DL guarantee: 34Mb/s", color="r")
    plt.plot(minUpload, label="UL Guarantee: 20Mb/s", color="m")

    plt.grid(True, which="major", axis="y")
    plt.legend(loc='upper right')

    fileToSave = "results" + dateShort + ".jpg"

    plt.savefig("/home/pi/speedcomplainer/v1/GraphResults/" + fileToSave)

    photo = open("/home/pi/speedcomplainer/v1/GraphResults/" + fileToSave, "rb")
    response = twitter.upload_media(media=photo)
    tweet = """#Python #RaspberryPi #SpeedTest #Matplotlib"""
    twitter.update_status(status=tweet, media_ids=[response["media_id"]])

graph_results()
