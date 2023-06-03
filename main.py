import pygame
pygame.init()
window = pygame.display.set_mode((700,500))
fps = pygame.time.Clock()

def gameOver(screen, text):
    myfont = pygame.font.Font(None, 36).render(text, True, (0, 0, 0))
    clock = pygame.time.Clock()
    run = True
    while run:
        #події
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                run = False
                pygame.quit()
        screen.blit(myfont, [250, 250])
        pygame.display.update()
        clock.tick(60)

class Sprite:
    def __init__(self, x, y, filename, speed, w, h):
        self.image = pygame.transform.scale(pygame.image.load(filename), (w, h))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def draw(self, window):
        window.blit(self.image, (self.rect.x, self.rect.y))
class Walls():
    def __init__(self,color,x, y, w, h):
        self.rect = pygame.Rect(x,y,w,h)
        self.color = color
    def draw(self,window):
        pygame.draw.rect(window,self.color,self.rect)
class BALL(Sprite):
    def update(self):
        self.rect.y += self.speed
class PLATFORM1(Sprite):
    def update(self):
        self.rect.y += self.speed
    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.rect.y -= self.speed
        if keys[pygame.K_s]:
            self.rect.y += self.speed
class PLATFORM2(Sprite):
    def update(self):
        self.rect.y += self.speed
    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN]:
            self.rect.y += self.speed

ball = BALL(310,200,"tenis_ball.png",5,50,50)
platform1 = PLATFORM1(40,180,"platform.png",5,30,110)
platform2 = PLATFORM2(630,180,"platform.png",5,30,110)

game_over = False
ri = False
lt = False
move_right = False
move_left = False
dx = 3
dy = 3

walls = []
walls.append(Walls((250,0,0),650,0,50,700))
walls.append(Walls((0,0,250),0,0,50,700))
walls.append(Walls((250,250,250),350,0,5,1000))

game = True
while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    if move_right:
        PLATFORM1.rect.x += 3
    if move_left:
        PLATFORM1.rect.x -= 3

    ball.rect.x += dx
    ball.rect.y += dy

    if ball.rect.y < 0 or ball.rect.y > 450:
        dy *= -1
    if ball.rect.x > 650 or ball.rect.x < 0:
        dx *= -1

    if ball.rect.colliderect(platform1.rect):
        dy *= -1
        dx *= -1
    if ball.rect.colliderect(platform2.rect):
        dy *= -1
        dx *= -1
    if ball.rect.x < 0:
        gameOver(window, "ЧЕРВОНИЙ ВИГРАВ!!")
    if ball.rect.x > 650:
        gameOver(window, "СИНІЙ  ВИГРАВ!!")

    window.fill([110,150, 110])
    for i in range(3):
        walls[i].draw(window)
    ball.draw(window)
    platform1.draw(window)
    platform2.draw(window)
    platform1.update()
    platform2.update()

    pygame.display.flip()
    fps.tick(60)