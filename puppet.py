import random


class Puppet:
    routs = [[3, 2, 8, 9, 10], [4, 5, 6, 7, 8, 2, 1, 0], [4, 5, 7, 6, 5, 3, 2, 1, 0], [4, 3, 2, 7, 8, 9, 10]]

    def __init__(self):
        self.room = 4
        self.create_rout()
        self.is_attacking = False

    def create_rout(self):
        self.rout = random.choice(Puppet.routs)
        self.rout_stage = 0

    def change_room(self):
        if self.rout:
            self.rout_stage += 1
            self.room = self.rout[self.rout_stage]
        else:
            if self.room == 0:
                self.is_attacking = True
            if self.room == 10:
                self.is_attacking = True
            self.rout_stage = 0
