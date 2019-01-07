import pygame

class InputHandler(object):
    def __init__(self):
        self.joyList = []
        for i in range(pygame.joystick.get_count()):
            self.joyList.append(pygame.joystick.Joystick(i))
            self.joyList[i].init()
        self.horiz = 0.0
        self.vert = 0.0

    def update(self):
        self.horiz = 0.0
        self.vert = 0.0

        print("button =", self.joyList[0].get_button(0))
        print("hat =", self.joyList[0].get_hat(0))

        eList = pygame.event.get()
        for e in eList:
            if e.type == pygame.JOYBUTTONDOWN:
                print("JOYBUTTONDOWN", e.joy, e.button)
            elif e.type == pygame.JOYBUTTONUP:
                print("JOYBUTTONUP", e.joy, e.button)
            elif e.type == pygame.JOYAXISMOTION:
                print("JOYAXISMOTION", e.joy, e.axis, e.value)
            elif e.type == pygame.JOYBALLMOTION:
                print("JOYBALLMOTION", e.joy, e.ball, e.rel)
            elif e.type == pygame.JOYHATMOTION:
                print("JOYHATMOTION", e.joy, e.hat, e.value)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:         self.horiz -= 1.0
        if keys[pygame.K_RIGHT]:        self.horiz += 1.0
        if keys[pygame.K_UP]:           self.vert -= 1.0
        if keys[pygame.K_DOWN]:         self.vert += 1.0
        if len(self.joyList) > 0:
            if abs(self.joyList[0].get_axis(0)) > 0.05:
                self.horiz = self.joyList[0].get_axis(0)
            if abs(self.joyList[0].get_axis(1)) > 0.05:
                self.vert = self.joyList[0].get_axis(1)
        if keys[pygame.K_ESCAPE]:
            return True
        #if mainJoy:
            #print(mainJoy.get_axis(0))     # Left-analong horizontal
            #print(mainJoy.get_axis(1))      # Left-analong vertical
            #print(mainJoy.get_button(0))     # A
        return False

pygame.display.init()
pygame.joystick.init()
screen = pygame.display.set_mode((800,600))
clock = pygame.time.Clock()
done = False

IH = InputHandler()
x = 400
y = 300
speed = 100


while not done:
    dt = clock.tick() / 1000.0
    if IH.update():
        done = True

    x += IH.horiz * speed * dt
    y += IH.vert * speed * dt

    screen.fill((0,0,0))
    pygame.draw.circle(screen, (255,0,0), (int(x), int(y)), 20)
    pygame.display.flip()

pygame.joystick.quit()
pygame.display.quit()
