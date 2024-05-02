from joint import Joint

class Leg:
    def __init__(self, shoulder, knee, hock):
        self.shoulder = shoulder
        self.knee = knee
        self.hock = hock
        self.Reset()

    def Reset(self):
        self.shoulder.setPosition()
        self.knee.setPosition()
        self.hock.setPosition()