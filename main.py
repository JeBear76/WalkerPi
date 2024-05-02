#!/usr/bin/python

import time
from joint import Joint
from PCA9685 import JointController

if __name__=='__main__':
  pwm = JointController(0x40, debug=False)
  pwm.setPWMFreq(50)

  joint3 = Joint(3, controller=pwm)
  
  joint3.setPosition(520)
  pwm.setPWM(3, 0xFF, 0x00)

  FRSjoint = Joint(0, 500, 2700, controller=pwm)
  FRSjoint.setPosition(500)
  pwm.setPWM(FRSjoint.channel, 0x0F, 0x00)
  BRSjoint = Joint(1, 500, 2700, controller=pwm)
  BRSjoint.setPosition(500)
  pwm.setPWM(BRSjoint.channel, 0x0F, 0x00)
  BLSjoint = Joint(2, 500, 2700, controller=pwm)
  BLSjoint.setPosition(2000)
  pwm.setPWM(BLSjoint.channel, 0x0F, 0x00)
  FLSjoint = Joint(3, 500, 2700, controller=pwm)
  FLSjoint.setPosition(500)
  pwm.setPWM(FLSjoint.channel, 0x0F, 0x00)

  joint.setPosition(510)
  minPulse = 500
  maxPulse = 2700
  input("Waiting...")

  while True:
    for servo in [FRSjoint, BRSjoint, BLSjoint, FLSjoint]
		for i in range(servo.minPulse, servo.maxPulse, 10):
		  joint.setPosition(i)
		  time.sleep(0.02)

		for i in range(servo.maxPulse, servo.minPulse, -10):
		  joint.setPosition(i)
		  time.sleep(0.02)
		  
		print("servo {servo.channel}")
		try:
			val = int(input(f"minPulse value: "))
			servo.minPulse = val
		except:
			pass
		
		try:
			val = int(input("maxPulse value: "))
			servo.maxPulse = val
		except:
			pass
			
	val = input("next round?")
	if val == ""
		break
		
  for servo in [FRSjoint, BRSjoint, BLSjoint, FLSjoint]
    print(f"servo: {servo.channel}")
    print(f"minPulse: {servo.minPulse}")
    print(f"maxPulse: {servo.maxPulse}")
    pwm.setPWM(joint.channel, 0xFF, 0x00)