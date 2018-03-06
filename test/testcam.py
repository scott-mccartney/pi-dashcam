# Dashcam test
from picamera import PiCamera
from time import sleep

with PiCamera() as camera:
    camera.start_preview()
    sleep(5)
    camera.capture('images/test1.jpg')
    camera.stop_preview()
