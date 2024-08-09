class Creature:
    def __init__(self, name):
        self.name = name


class Horse(Creature):
    def __init__(self, name):
        super().__init__(name)
        self.xDistance = 0
        self.sound = 'Frrr'

    def run(self, dx):
        self.xDistance += dx


class Eagle(Creature):
    def __init__(self, name):
        super().__init__(name)
        self.yDistance = 0
        self.sound = 'I train, eat, sleep, and repeat'

    def fly(self, dy):
        self.yDistance += dy


class Pegasus(Horse, Eagle):
    def __init__(self, name):
        super().__init__(name)

    def move(self, dx, dy):
        self.fly(dy)
        self.run(dx)

    def getPos(self):
        return (self.xDistance, self.yDistance)

    def voice(self, name):
        print(Eagle(name).sound)


if __name__ == '__main__':
    print(Pegasus.mro())

    p1 = Pegasus('peg')
    print(p1.getPos())
    p1.move(10, 15)
    print(p1.getPos())
    p1.move(-5, 20)
    print(p1.getPos())

    p1.voice('peg')

    a = 10
