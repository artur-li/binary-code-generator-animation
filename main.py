import pygame, sys, random
pygame.init()

# general variables
screen = pygame.display.set_mode((600,600))
clock = pygame.time.Clock()
font = pygame.font.Font("font.ttf", 20)

class Binary_code(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = font.render(self.binary_code_generator(), False, "Green")
        self.rect = self.image.get_rect()
        self.random_location()
        self.timer = 0

    def binary_code_generator(self):
        # returns generated binary code 
        bits = []
        for i in range(8,57,8):
            bits.append(i)
        random_num = random.choice(bits)
        random_binary_code = ""
        for i in range(random_num):
            random_binary_code += random.choice(["0","1"])
        return random_binary_code
    
    def random_location(self):
        # place the generated binary code randomly
        y_axis_options = [i for i in range(0,601,25)]
        self.rect.centery = random.choice(y_axis_options)
        self.rect.centerx = random.randint(10,590)

    def disapear(self):
        # makes the binary code disapear in 2 sec 
        if self.timer % 20 == 0:
            self.kill()

    def update(self):
        # do this... (each frame)
        self.timer += 1
        self.disapear()

# binary code group
binary_group = pygame.sprite.Group()

def spawn_binary_code():
# instanciates Binary class
    keys = pygame.key.get_pressed() 
    if keys[pygame.K_SPACE]:
        binary1 = Binary_code()
        binary_group.add(binary1)

while True:

    for event in pygame.event.get():
        # close if 'x' pressed
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill("black")

    spawn_binary_code()
    binary_group.draw(screen)
    binary_group.update()

    pygame.display.update()
    clock.tick(60)
