#!/usr/bin/python

import time
from joint import Joint
from PCA9685 import JointController

if __name__=='__main__':
  pwm = JointController(0x40, debug=True)
  pwm.setPWMFreq(50)

  joints = [
    Joint(0,600,2500,pwm),
    Joint(1,600,2500,pwm),
    Joint(2,600,2500,pwm),
    Joint(3,600,2500,pwm),
    Joint(4,600,2500,pwm),
    Joint(5,600,2500,pwm),
    Joint(6,600,2500,pwm),
    Joint(7,600,2500,pwm),
    Joint(8,600,2500,pwm),
    Joint(9,600,2500,pwm),
    Joint(10,600,2500,pwm),
    Joint(11,600,2500,pwm),
    Joint(12,600,2500,pwm)
  ]
  
  while True:
   # setServoPulse(2,2500)
    for joint in range(0,12):  
      pwm.setServoPulse(joint,600)   
      time.sleep(0.02)     
    
    