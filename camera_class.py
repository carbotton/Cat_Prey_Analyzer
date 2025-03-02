import RPi.GPIO as GPIO
#from picamera.array import PiRGBArray
#from picamera import PiCamera
from gpiozero import CPUTemperature

from collections import deque
import pytz
from datetime import datetime
from threading import Thread
import time
import sys
import cv2
import numpy as np
import io, gc

class Camera:
    def __init__(self, ip_camera_url):
        self.ip_camera_url = ip_camera_url  # URL for the IP camera stream
        self.cap = cv2.VideoCapture(self.ip_camera_url)
        if not self.cap.isOpened():
            raise Exception("Could not connect to IP camera")
        
        time.sleep(2)
    
    def fill_queue(self, deque):
        while True:
            gc.collect()
            
            ret, frame = self.cap.read()
            if not ret:
                print("Failed to retrieve frame from IP camera")
                continue
            
            timestamp = datetime.now(pytz.timezone('Europe/Zurich')).strftime("%Y_%m_%d_%H-%M-%S.%f")
            deque.append((timestamp, frame))
            
            print("Quelength:", len(deque), "Streamsize:", sys.getsizeof(frame))
            
            time.sleep(1 / 3)  # Maintain ~3 FPS like the original script
    
    def close(self):
        self.cap.release()
        cv2.destroyAllWindows()
