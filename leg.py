from joint import Joint

class Leg:
    def __init__(self, shoulder, knee, hock):
        self.shoulder = shoulder
        self.knee = knee
        self.hock = hock
        self.Reset()

    def Reset(self):
        if self.shoulder is not None:
            self.shoulder.setPosition()
        if self.knee is not None:
            self.knee.setPosition()
        if self.hock is not None:
            self.hock.setPosition()