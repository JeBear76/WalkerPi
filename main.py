#!/usr/bin/python

import time
from PCA9685 import Joint

if __name__=='__main__':
 
  pwm = Joint(0x40, debug=True, minPulse=600, maxPulse=2500)
  pwm.setPWMFreq(50)
  while True:
   # setServoPulse(2,2500)
    for i in range(500,2500,10):  
      pwm.setServoPulse(0,i)   
      time.sleep(0.02)     
    
    for i in range(2500,500,-10):
      pwm.setServoPulse(0,i) 
      time.sleep(0.02)  
