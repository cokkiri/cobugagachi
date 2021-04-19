

'''
    direction

    0 : north
    1 : east
    2 : south
    3 : west
'''

class GameCharacter():
    def __init__(self, pos_x, pos_y, direction):

        self.pos_x = pos_x
        self.pos_y = pos_y
        self.fwd_pos_x = pos_x
        self.fwd_pos_y = pos_y
        self.bwd_pos_x = pos_x
        self.bwd_pos_y = pos_y
        self.direction = direction
        self.visited = [(pos_x, pos_y)]

        return

    def init_fwd_pos(self):

        self.fwd_pos_x = self.pos_x
        self.fwd_pos_y = self.pos_y

        return

    def turn_left(self): 

        self.direction = (self.direction - 1) % 4

        return

    def get_left_position(self):

        if self.direction == 0:
            self.fwd_pos_y -= 1
        elif self.direction == 1:
            self.fwd_pos_x -= 1
        elif self.direction == 2:
            self.fwd_pos_y += 1
        elif self.direction == 3:
            self.fwd_pos_x += 1

        return

    def get_backward_position(self):

        if self.direction == 0:
            self.bwd_pos_x += 1
        elif self.direction == 1:
            self.bwd_pos_y += 1
        elif self.direction == 2:
            self.bwd_pos_x -= 1 
        elif self.direction == 3:
            self.bwd_pos_y -= 1

        return

    def go_forward(self):

        self.pos_x = self.fwd_pos_x
        self.pos_y = self.fwd_pos_y

        return
    
    def go_backward(self):

        self.pos_x = self.bwd_pos_x
        self.pos_y = self.bwd_pos_y

        return
    
    def save_memory(self, position):

        self.visited.append(position)

        return
