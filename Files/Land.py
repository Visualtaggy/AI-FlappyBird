from Files.Constants import *

class Land:

    speed = 5
    width = land_img.get_width()
    img = land_img

    def __init__(self, y):

        self.y = y
        self.x1 = 0
        self.x2 = self.width

    def move(self):
        self.x1 -= self.speed
        self.x2 -= self.speed
        if self.x1 + self.width < 0:
            self.x1 = self.x2 + self.width

        if self.x2 + self.width < 0:
            self.x2 = self.x1 + self.width

    def draw(self, win):

        win.blit(self.img, (self.x1, self.y))
        win.blit(self.img, (self.x2, self.y))
