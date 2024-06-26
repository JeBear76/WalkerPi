from joint import Joint
import constants as const

class Leg:

    def __init__(self, shoulder, knee, hock, side):
        self.shoulder = shoulder
        self.knee = knee
        self.hock = hock
        self.side = side
        self.action = False
        self.Reset()

    def Reset(self):
        if self.shoulder is not None:
            self.shoulder.setPulse()
        if self.knee is not None:
            self.knee.setPulse()
        if self.hock is not None:
            self.hock.setPulse()

    def Move(self, direction):
        if direction == const.FORWARD:
            if not self.action:
                if self.side == const.RIGHT:
                    desiredPulse = int(self.shoulder.maxPulse*.850)
                    print (f'(d: {desiredPulse}, o: {self.shoulder.oldPulse})')
                    self.shoulder.setPulse(desiredPulse)
                elif self.side == const.LEFT:
                    desiredPulse = int(self.shoulder.minPulse/.85)
                    self.shoulder.setPulse(desiredPulse)
                if desiredPulse <= self.shoulder.oldPulse:
                    self.action = not self.action
            else:
                if self.side == const.RIGHT:
                    desiredPulse = int(self.shoulder.minPulse)
                    print (f'(d: {desiredPulse}, o: {self.shoulder.oldPulse})')
                    self.shoulder.setPulse(desiredPulse)
                elif self.side == const.LEFT:
                    desiredPulse = int(self.shoulder.maxPulse)
                    self.shoulder.setPulse(desiredPulse)
                if desiredPulse >= self.shoulder.oldPulse:
                    self.action = not self.action


    