#!/usr/bin/python

import time
from joint import Joint
from leg import Leg
from PCA9685 import JointController

if __name__=='__main__':
  pwm = JointController(0x40, debug=False)
  pwm.setPWMFreq(50)

  #Shoulders
  FRSjoint = Joint(0, 700, 1900, controller=pwm)
  BRSjoint = Joint(1, 700, 2400, controller=pwm)
  BLSjoint = Joint(2, 1000, 2400, controller=pwm)
  FLSjoint = Joint(3, 700, 2000, controller=pwm)

  #Knees
  FRKjoint = Joint(4, 700, 1900, controller=pwm)
  BRKjoint = Joint(5, 700, 2400, controller=pwm)
  BLKjoint = Joint(6, 1000, 2400, controller=pwm)
  FLKjoint = Joint(7, 700, 2000, controller=pwm)

  #Hock
  FRHjoint = Joint(8, 700, 1900, controller=pwm)
  BRHjoint = Joint(9, 700, 2400, controller=pwm)
  BLHjoint = Joint(10, 1000, 2400, controller=pwm)
  FLHjoint = Joint(11, 700, 2000, controller=pwm)

  FRLeg = Leg(FRSjoint, FRKjoint, FRHjoint)
  BRLeg = Leg(BRSjoint, BRKjoint, BRHjoint)
  BLLeg = Leg(BLSjoint, BLKjoint, BLHjoint)
  FLLeg = Leg(FLSjoint, FLKjoint, FLHjoint)

  FRSjoint.setPosition()
  time.sleep(0.02)
  BRSjoint.setPosition()
  time.sleep(0.02)
  BLSjoint.setPosition()
  time.sleep(0.02)
  FLSjoint.setPosition()
  time.sleep(0.02)

  minPulse = 500
  maxPulse = 2700
  input("Waiting...")

  while True:
    for servo in [FRKjoint, BRKjoint, BLKjoint, FLKjoint]: # Use #Knees
      for i in range(servo.minPulse, servo.maxPulse, 10):
        servo.setPosition(i)
        time.sleep(0.02)

      for i in range(servo.maxPulse, servo.minPulse, -10):
        servo.setPosition(i)
        time.sleep(0.02)
      
      print(f"servo {servo.channel}")
      try:
        val = int(input(f"minPulse value: {servo.minPulse}"))
        servo.minPulse = val
      except:
        pass
    
      try:
        val = int(input(f"maxPulse value: {servo.maxPulse}"))
        servo.maxPulse = val
      except:
        pass
    
    val = input("next round?")
    if val == "":
      break
    
  for servo in [FRSjoint, BRSjoint, BLSjoint, FLSjoint]:
    print(f"servo: {servo.channel}")
    print(f"minPulse: {servo.minPulse}")
    print(f"maxPulse: {servo.maxPulse}")
    servo.setPosition(-1)