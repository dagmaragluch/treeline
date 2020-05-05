class Actor:

    def __init__(self):
        self.position = None

    def onEvent(self, event):
        # Called by engine if event (e.g. key pressed) happened
        # Must be registered for particular event first by calling Engine.registerForEvent
        pass