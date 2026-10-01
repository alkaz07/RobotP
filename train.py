class Box:

    def __init__(self, a: int):
        self.a = a

    def inc(self):
        self.a+=1
    def dec(self):
        self.a-=1

    def set_a(self, new_a):
        self.a = new_a
    def get_a(self):
        return self.a
    def add(self, x):
        self.a += x

box1 = Box(111)
box1.dec()

box2 = Box(box1.a)
for i in range(4):
    box2.inc()
    box1.a +=2
print(box1.a, box2.a)

def magic(box: Box):
    if box.a %3 == 0:
        box.a -= 100
    elif box.a %3 == 1:
        box.inc()
    else:
        box.dec()

def magic2(box: Box):
    if box.get_a() %3 == 0:
        box.add(-100)
    elif box.get_a() %3 == 1:
        box.inc()
    else:
        box.dec()

magic(box1)
magic(box2)
print(box1.a, box2.a)