import json
import RPi.GPIO as gpio
gpio.setmode(gpio.BCM)
gpio.setwarnings(False)
gpio.setup(17,gpio.OUT)
from picamera import PiCamera
from watson_develpoer_cloud import VisualRecognitionV3
import datetime
from time import sleep
cam = PiCamera()
visualrecog = VisualRecognitionV3( 
  '2020-07-06',
  iam_apikey='vPLBEsM1Cr3gcozMtXwovrZDqOPENtUP4XZmK1qGGafn')
cam.start_preview(alpha=150)
gpio.output(17,gpio.LOW)
while True:
  a = 'y' #input("y for click and check, q for exit:")
  if a == 'y':
    instant = str(datetime.datetime.now())
    cam.capture('/home/pi/Project Headlight/image'+instant+'.jpg')
    with open() as images_file:
      classes = visualrecog.classify(
        images_file,
        threshold='0.6'
        classifier_ids='').get_result()
    output = json.dumps(classes, indent=2)
    if "Street light" in output:
      print("adequate lighting")
      gpio.output(17,gpio.HIGH)
      print("LED ON")
    else:
      print("inadequate lighting")
      gpio.output(17,gpio.LOW)
  elif a == 'q':
    break
  else:
    pass
cam.stop_preview()      
