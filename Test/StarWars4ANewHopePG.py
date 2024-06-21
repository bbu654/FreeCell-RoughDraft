import pygame as pg
from   pygame.locals import *
pg.init()

StarWars4 = '''
Star Wars IV
A New Hope

It is a period of civil war.
Rebel spaceships, striking
from a hidden base, have won
their first victory against
the evil Galactic Empire.

During the battle, Rebel
spies managed to steal secret
plans to the Empire's
ultimate weapon, the DEATH
STAR, an armored space
station with enough power to
destroy an entire planet.

Pursued by the Empire's
sinister agents, Princess
Leia races home aboard her
starship, custodian of the
stolen plans that can save
her people and restore
freedom to the galaxy....


Episode V
THE EMPIRE STRIKES BACK
It is a dark time for the
Rebellion. Although the Death
Star has been destroyed,
Imperial troops have driven the
Rebel forces from their hidden
base and pursued them across
the galaxy.

Evading the dreaded Imperial
Starfleet, a group of freedom
fighters led by Luke Skywalker
has established a new secret
base on the remote ice world
of Hoth.

The evil lord Darth Vader,
obsessed with finding young
Skywalker, has dispatched
thousands of remote probes into
the far reaches of space....


Episode VI
RETURN OF THE JEDI
Luke Skywalker has returned to
his home planet of Tatooine in
an attempt to rescue his
friend Han Solo from the
clutches of the vile gangster
Jabba the Hutt.

Little does Luke know that the
GALACTIC EMPIRE has secretly
begun construction on a new
armored space station even
more powerful than the first
dreaded Death Star.

When completed, this ultimate
weapon will spell certain doom
for the small band of rebels
struggling to restore freedom
to the galaxy...


Episode VII
THE FORCE AWAKENS
Luke Skywalker has vanished.
In his absence, the sinister
FIRST ORDER has risen from
the ashes of the Empire
and will not rest until
Skywalker, the last Jedi,
has been destroyed.

With the support of the
REPUBLIC, General Leia Organa
leads a brave RESISTANCE.
She is desperate to find her
brother Luke and gain his
help in restoring peace
and justice to the galaxy.

Leia has sent her most daring
pilot on a secret mission
to Jakku, where an old ally
has discovered a clue to
Luke's whereabouts....


Episode VIII
THE LAST JEDI
The FIRST ORDER reigns.
Having decimated the peaceful
Republic, Supreme Leader Snoke
now deploys his merciless
legions to seize military
control of the galaxy.

Only General Leia Organa's
band of RESISTANCE fighters
stand against the rising
tyranny, certain that Jedi
Master Luke Skywalker will
return and restore a spark of
hope to the fight.

But the Resistance has been
exposed. As the First Order
speeds toward the rebel base,
the brave heroes mount a
desperate escape....


Episode IX
THE RISE OF SKYWALKER
The dead speak! The galaxy has
heard a mysterious broadcast,
a threat of REVENGE in the
sinister voice of the late
EMPEROR PALPATINE.

GENERAL LEIA ORGANA
dispatches secret agents to
gather intelligence, while REY,
the last hope of the Jedi, trains
for battle against the diabolical
FIRST ORDER.

Meanwhile, Supreme Leader
KYLO REN rages in search
of the phantom Emperor,
determined to destroy any
threat to his power....
'''.split('\n')


class Credits:
    def __init__(self, screenRect, lst) -> None:
        self.srect = screenRect
        self.lst   = lst
        self.size  = 42
        self.color = (255,255,0)
        self.buffCentery = self.srect.height/2 + 5
        self.buffLines   = 50
        self.timer = 0.0
        self.delay = 0
        self.makeSurfaces()

    def makeText(self, message):
        font = pg.font.SysFont('Arial', self.size)
        text = font.render(message, True, self.color)
        rect = text.get_rect(center = (self.srect.centerx, self.srect.centery + self.buffCentery))
        return text, rect
    
    def makeSurfaces(self):
        self.text = []
        for i, line in enumerate(self.lst):
            l = self.makeText(line)
            l[1].y += i * self.buffLines
            self.text.append(l)

    def update(self):
        if pg.time.get_ticks() - self.timer > self.delay:
            self.timer = pg.time.get_ticks()
            for text, rect in self.text:
                rect.y -= 1

    def render(self, surf):
        for text, rect in self.text:
            surf.blit(text, rect)

screen = pg.display.set_mode((800,600))
screenRect = screen.get_rect()
clock = pg.time.Clock()
running = True
cred = Credits(screenRect, StarWars4)

while running:
    for event in pg.event.get():
        if event.type == QUIT:
            running = False
    screen.fill((0,0,0))
    cred.update()
    cred.render(screen)
    pg.display.update()
    clock.tick(60)
    
