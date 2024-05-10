from PCA9685 import JointController

class Joint:
    def __init__(self, channel, minPulse, maxPulse, initPulse, controller = JointController(0x40, debug=True)):
        self.Controller = controller
        self.channel = channel
        self.minPulse = minPulse
        self.maxPulse = maxPulse
        self.oldPulse = initPulse
        self.initPulse = initPulse

    def setPulse(self, pulse=None): 
        if pulse is None:
            pulse = self.initPulse
        if pulse > self.maxPulse:
            pulse = self.maxPulse
        if pulse < self.minPulse:
            pulse = self.minPulse
        mvPulse = int(((500 * pulse) + (9500 * self.oldPulse))/10000)
        self.oldPulse = mvPulse
        self.Controller.setServoPulse(self.channel, mvPulse)