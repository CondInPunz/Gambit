import random


class Puppet:
    routs = [[3, 2, 8, 9, 10], [4, 5, 6, 7, 8, 2, 1, 0], [4, 5, 7, 6, 5, 3, 2, 1, 0], [4, 3, 2, 7, 8, 9, 10]]

    def __init__(self):
        self.room = 4
        self.create_rout()
        self.is_attacking = False
        self.left_door = None
        self.right_door = None

    def create_rout(self):
        self.rout = random.choice(Puppet.routs)
        print(self.rout)
        self.rout_stage = 0

    def change_room(self):
        print(self.room)
        print(self.is_attacking)
        self.rout_stage += 1
        self.room = self.rout[self.rout_stage]
        if self.room == 0:
            if self.check_is_closed(self.left_door):
                self.is_attacking = True
        if self.room == 10:
            if self.check_is_closed(self.right_door):
                self.is_attacking = True

    def check_is_closed(self, door):
        return True
