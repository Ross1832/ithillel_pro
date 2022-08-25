class DigitalCounter:
    def __init__(self, start=0, end=100, current=None):
        self.start = start
        self.end = end
        self.current = start if current is None else current

    def increase(self):
        if self.current >= self.end:
            raise ValueError('You already reached the max value')
        self.current += 1

    def get_current_value(self):
        return self.current


a = DigitalCounter(start=0, end=5)
for _ in range(6):
    print(a.get_current_value())
    a.increase()



