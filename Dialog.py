# update the way we do choices
import pygame

pygame.init()

class Dialog:
    def __init__(self,file):
        self.file=open(file )
        self.list = []
        for line in self.file:
            line=line.strip()
            if line[2] == "-":
                dialist=line.split("-")
                self.list.append(dialist[1])
                
    def blitthis (self,screen,dia,pos=(75, 600)):
        #temp font
        my_font = pygame.font.SysFont("Comic Sans", 40)
        pygame.draw.rect(screen,(0,0,0),(50,590,700,150),0)
        pygame.draw.rect(screen, (255, 255, 255), (55, 595, 690, 140), 1)
        diasurf = my_font.render(dia,False,(255,255,255))
        screen.blit(diasurf,pos)

    def choice(self, screen, answer1=1, answer2=2, answer3=3, *options):

        my_font = pygame.font.SysFont("Comic Sans", 40)
        x=75

        a=0
        while a == 0:
            key = pygame.key.get_pressed()
            pygame.event.pump()
            y = 600
            for i in range( len(options)):
                self.blitthis(screen,options[i],(x,y))
                pygame.display.update()

            if key[pygame.K_KP1] or key[pygame.K_1] :
                a= 1
            if key[pygame.K_KP2] or key[pygame.K_2]:
                a= 2
            if key[pygame.K_KP3]or key[pygame.K_3]:
                a= 3

        while True:
            pygame.draw.rect(screen, (0, 0, 0), (50, 590, 700, 150), 0)
            pygame.draw.rect(screen, (255, 255, 255), (55, 595, 690, 140), 1)
            pygame.event.pump()
            key = pygame.key.get_pressed()
            if key[pygame.K_KP1] or key[pygame.K_1] :
                a= 1
            if key[pygame.K_KP2] or key[pygame.K_2]:
                a= 2
            if key[pygame.K_KP3]or key[pygame.K_3] :
                a= 3
            if a> len(options):

                self.blitthis(screen,"...")
            elif a<= len(options):
                pygame.event.pump()
                if a==1:
                    self.blitthis(screen,answer1)

                elif a ==2:
                    self.blitthis(screen,answer2)

                elif a ==3:
                    self.blitthis(screen,answer3)

            if key[pygame.K_KP_ENTER] or key[pygame.K_RETURN]:
                break
                return a
            pygame.display.update()






if __name__ == "__main__":
    screen= pygame.display.set_mode((800,600))
    pygame.event.pump()


    test=Dialog("DialogStart")


    screen.fill((255,0,0))
    test.choice(screen, test.Jason_dialog[1],2,3,test.Paul_dialog[0])

        # test.blit(screen, test.Jason_dialog[0])
        # test.blit(screen, test.Paul_dialog[0])
        # if keydown [pygame.K_1]:
        #     pass
        # elif keydown[pygame.k_2]:
        #      pass

    # print(test.Paul_dialog[0])
    # print(test.Jason_dialog[1])
    # print(test.Travis_dialog[0])

    pygame.display.update()
