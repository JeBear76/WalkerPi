#!/usr/bin/python

import time
from joint import Joint
from PCA9685 import JointController

if __name__=='__main__':
  pwm = JointController(0x40, debug=False)
  pwm.setPWMFreq(50)

  FRSjoint = Joint(0, 700, 1900, controller=pwm)
  FRSjoint.setPosition()
  time.sleep(0.02)
  BRSjoint = Joint(1, 700, 2400, controller=pwm)
  BRSjoint.setPosition()
  time.sleep(0.02)
  BLSjoint = Joint(2, 1000, 2400, controller=pwm)
  BLSjoint.setPosition()
  time.sleep(0.02)
  FLSjoint = Joint(3, 700, 2000, controller=pwm)
  FLSjoint.setPosition()
  time.sleep(0.02)

  minPulse = 500
  maxPulse = 2700
  input("Waiting...")

  # while True:
  #   for servo in [BRSjoint]: #FRSjoint, , BLSjoint, FLSjoint
  #     for i in range(servo.minPulse, servo.maxPulse, 10):
  #       servo.setPosition(i)
  #       time.sleep(0.02)

  #     for i in range(servo.maxPulse, servo.minPulse, -10):
  #       servo.setPosition(i)
  #       time.sleep(0.02)
      
  #     print(f"servo {servo.channel}")
  #     try:
  #       val = int(input(f"minPulse value: {servo.minPulse}"))
  #       servo.minPulse = val
  #     except:
  #       pass
    
  #     try:
  #       val = int(input(f"maxPulse value: {servo.maxPulse}"))
  #       servo.maxPulse = val
  #     except:
  #       pass
    
  #   val = input("next round?")
  #   if val == "":
  #     break
    
  for servo in [FRSjoint, BRSjoint, BLSjoint, FLSjoint]:
    print(f"servo: {servo.channel}")
    print(f"minPulse: {servo.minPulse}")
    print(f"maxPulse: {servo.maxPulse}")
    servo.setPosition(-1)