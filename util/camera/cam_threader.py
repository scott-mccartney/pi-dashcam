#!/usr/bin/python
from datetime import date
from picamera import PiCamera
import time
from time import sleep
import threading

camera = PiCamera()

# Dashcam recorder thread
class Dashcam (threading.Thread):    
    def __init__(self):
        threading.Thread.__init__(self)
        camera.resolution = (1920, 1080)
        camera.framerate = 15

    def record(self):
        localtime = time.asctime(time.localtime(time.time()))
        
        camera.annotate_text = str(localtime)
        print("Starting recording")
        # TODO format "Aug-10-2017 1:35PM.h264"
        camera.start_recording('test/videos/' + localtime + '.h264')
        
        sleep(8)
        camera.stop_recording()

        print("Finishing recording")

    def run(self):
        self.record()
        sleep(2)
        self.record()
        
scanner = Dashcam()
scanner.start()
