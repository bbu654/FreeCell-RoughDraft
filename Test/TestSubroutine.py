import pygame, time, subprocess
pygame.init()
screen= pygame.display.set_mode((800,250))
clock = pygame.time.Clock()
font  = pygame.font.Font(None,25)
pygame.time.set_timer(pygame.USEREVENT,200)
def text_generator(text):
    tmp=''
    for letter in text:
        tmp +=letter
        if letter!=' ':
            yield tmp

class DynamicText(object):
    def __init__(self,font,text,pos, autoreset=False) -> None:
        self.done = False
        self.font = font
        self.text = text
        self._gen = text_generator(self.text)
        self.pos  = pos
        self.autoreset = autoreset
        self.update()

    def reset(self):
        self._gen = text_generator(self.text)
        self.done = False
        self.update()

    def update(self):
        if not self.done:
            try: self.rendered = self.font.render(next(self._gen),True,(0,128,0))
            except StopIteration:
                self.done = True
                time.sleep(10)
                subprocess.Popen("python C:/Users/Brice/source/repos/LearningPy/TestCopilot/testPygame.py 1", shell=True)

    def draw(self, screen):
        screen.blit(self.rendered, self.pos)

text = (f"A long time ago in a galaxy far, far away, a barbarian strode from the frozen north. Sword in hand...")
message = DynamicText(font, text, (65, 120), autoreset=True)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: break
        if event.type == pygame.USEREVENT: message.update()
    else:
        screen.fill(pygame.color.Color('black'))
        message.draw(screen)
        pygame.display.flip()
        clock.tick(60)
        continue
    break
pygame.quit()