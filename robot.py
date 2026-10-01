class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Point ({self.x}; {self.y})"

class Robot:
    def __init__(self, x: int, y: int, direction: int):
        self.direction = direction
        self.pos = Point(x, y)
    def __repr__(self):
        return f"Robot <pos = {self.pos}, direction = {self.direction}>"
    def turn_right(self):
        self.direction -= 90
        if self.direction < 0:
            self.direction += 360
        if self.direction >= 360:
            self.direction -= 360
    def turn_left(self):
        self.direction += 90
        if self.direction < 0:
            self.direction += 360
        if self.direction >= 360:
            self.direction -= 360
    def move_forward(self):
        if self.direction == 0:
            self.pos.x +=1
        elif self.direction == 90:
            self.pos.y +=1
        elif self.direction == 180:
            self.pos.x -=1
        elif self.direction == 270:
            self.pos.y -=1
        else:
            print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
    def do_command(self, cmd):
        if cmd == 'S':
            self.move_forward()
        elif cmd == 'L':
            self.turn_left()
        elif cmd == 'R':
            self.turn_right()
    def run_program(self, prg: str):
        for cmd in prg:
            self.do_command(cmd)
            print(self)


rob = Robot(2, 4, 180)
# rob.move_forward()
rob.run_program('SLS')
print(rob)

print('==================================================')

robby = Robot(0, 0, 0)
robby.run_program('SSLSLSLSSRSRS')

robo_list = [
    rob, robby, Robot(-7, -8, 90), Robot(30, 30, 270)
]
print('\n------------------ список роботов -------------------')
print(robo_list)
for r in robo_list:
    r.do_command('S')
print(robo_list)

print('----------------------')
print(rob)
rob.direction = 'Vasya'
rob.move_forward()
rob.turn_left()
print(rob)