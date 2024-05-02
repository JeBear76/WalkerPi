from PCA9685 import JointController

class Joint:
    def __init__(self, channel, minPulse=500, maxPulse=2750, controller = JointController(0x40, debug=True)):
        self.Controller = controller
        self.channel = channel
        self.minPulse = minPulse
        self.maxPulse = maxPulse
    
    def setPosition(self, position):
        pulse = position
        if pulse > self.maxPulse:
            pulse = self.maxPulse
        if pulse < self.minPulse:
            pulse = self.minPulse
        self.Controller.setServoPulse(self.channel, pulse)