import pygame
pygame.init()
BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE  = (0,0,255)
GREEN = (0,255,0)
RED   = (255,0,0)
textB = f'Brice'
size  = (600,400)
screen= pygame.display.set_mode(size)
pygame.display.set_caption(f'Binary Conversion')
done  = False
clockB= pygame.time.Clock()
textRotateDegrees = 0
outBinary = (' '.join(format(ord(x), 'b') for x in textB))
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    screen.fill(WHITE)
    font = pygame.font.SysFont('Calibri',25,True,False)
    textA = font.render(outBinary,True,RED)
    textC= pygame.transform.rotate(textA, textRotateDegrees)
    textRotateDegrees += 1
    screen.blit(textC, [100,50])
    pygame.display.flip()
    clockB.tick(60)
pygame.quit()
print(f"Brice = {outBinary}")