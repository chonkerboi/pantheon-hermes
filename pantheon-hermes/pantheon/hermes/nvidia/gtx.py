class Nvidia1070:
    model = 'GeForce GTX 1070'

    def __init__(self, uid, bus):
        self.uid = uid
        self.bus = bus
        self.temperature = None

    def __str__(self):
        return '{}<{}, uid: {}, bus: {}>'.format(self.__class__.__name__, self.model, self.uid, self.bus)
