#!/usr/bin/python
from pynput import keyboard
from joint import Joint
from leg import Leg
from PCA9685 import JointController

if __name__=='__main__':
  pwm = JointController(0x40, debug=False)
  pwm.setPWMFreq(50)

  #Shoulders
  FRSjoint = Joint(0, 600, 1900, 1300, controller=pwm)
  BRSjoint = Joint(1, 600, 1900, 1300, controller=pwm)
  BLSjoint = Joint(2, 600, 1900, 1300, controller=pwm)
  FLSjoint = Joint(3, 600, 1900, 1300, controller=pwm)

  #Knees
  FRKjoint = Joint(4, 500, 2100, 2100, controller=pwm)
  BRKjoint = Joint(5, 500, 2100, 600, controller=pwm)
  FLKjoint = Joint(7, 500, 2100, 2100, controller=pwm)
  BLKjoint = Joint(6, 500, 2100, 600, controller=pwm)

  #Hock
  FRHjoint = Joint(8, 500, 2100, 1900, controller=pwm)
  BRHjoint = Joint(9, 500, 2100, 600, controller=pwm)
  BLHjoint = Joint(10, 500, 2100, 1900, controller=pwm)
  FLHjoint = Joint(11, 500, 2100, 600, controller=pwm)

  FRLeg = Leg(FRSjoint, FRKjoint, FRHjoint)
  BRLeg = Leg(BRSjoint, BRKjoint, BRHjoint)
  BLLeg = Leg(BLSjoint, BLKjoint, BLHjoint)
  FLLeg = Leg(FLSjoint, FLKjoint, FLHjoint)

  from pynput import keyboard

  def on_activate_h():
      print('<ctrl>+<alt>+h pressed')

  def on_activate_i():
      print('<ctrl>+<alt>+i pressed')

  controls = keyboard.GlobalHotKeys({
          '<ctrl>+<alt>+h': on_activate_h,
          '<ctrl>+<alt>+i': on_activate_i})
  
  controls.start()

  while True:
    try:
       pass
    except KeyboardInterrupt:
       break
    
  controls.stop()