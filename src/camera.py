from picamera import PiCamera
from time import sleep
camera = PiCamera()
camera.rotation = 180
camera.resolution = (2592, 1944)
camera.framerate = 15
camera.start_recording('/home/pi/Documents/Camera/video.h264')
sleep(10)
camera.stop_recording()

camera.start_preview()
for i in range(1):
    sleep(5)
    camera.capture('/home/pi/Documents/Camera/image%s.jpg' % i)
camera.stop_preview()
