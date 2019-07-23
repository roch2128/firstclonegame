import pygame
import sys

pygame.init()

clock = pygame.time.Clock()
#------------------ resolution ------------------------
display_width = 640
display_height = 480

# ------------------- Colors ------------------------

white = (255, 255, 255)
black = (0, 0, 0)

# ------------------------ gamedisplay -------------------

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("pong")


class Rec:
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.width = w
        self.height = h
        self.r = pygame.Rect(x, y, w, h)
        self.xchange = 8
        self.ychange = 7


class Ball(Rec):
    def __init__(self, x, y, w, h):
        super().__init__(x, y, w, h)

    def draw(self):
        pygame.draw.rect(gameDisplay, white, self.r)

    def move(self):
        self.r.x -= self.xchange
        self.r.y -= self.ychange

    def collision(self):
        if self.r.x >= display_width - 20 or self.r.x < 0:
            self.xchange = self.xchange * -1
        elif self.r.y >= display_height - 20 or self.r.y < 0:
            self.ychange = self.ychange * -1
        elif self.r.colliderect(paddle.r):
            self.xchange = self.xchange * -1


# --- MainLoop ---
up_pressed = False
down_pressed = False

paddle = Rec(10, display_height / 2, 20, 89)
block = Rec(0, -3, display_width, 6)
block2 = Rec(0, display_height - 2, display_width, 10)
b1 = Ball(display_width/2, display_height/2, 15, 15)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                up_pressed = True
            if event.key == pygame.K_DOWN:
                down_pressed = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                up_pressed = False
            if event.key == pygame.K_DOWN:
                down_pressed = False
    b1.move()
    b1.collision()

    if up_pressed:
        paddle.r.y -= 10
    elif down_pressed:
        paddle.r.y += 10

    if paddle.r.y <= 0:
        up_pressed = False
    elif paddle.r.y + paddle.y >= display_width:
        down_pressed = False

    gameDisplay.fill(black)
    pygame.draw.rect(gameDisplay, white, paddle.r)
    pygame.draw.rect(gameDisplay, white, block.r)
    pygame.draw.rect(gameDisplay, white, block2.r)
    b1.draw()
    pygame.display.flip()
    clock.tick(30)