from tkinter import *
from time import sleep as s
from random import randint as r

XI = 224
YI = 418
speed = 6
jump = True
persona = [[]]
attack = [[]]
floor = [[]]
zombie = [[]]
contFloor = 0
lop1 = True
XZ = 50
contSpawnZombie = 0
life = 3
alive = True
points = 0


def VerifyLifeandDamage():
    global life
    global pers
    global alive
    global XZ
    global XI
    global nlife

    if XI - 15 <= XZ <= XI + 16 and alive == True:
        life -= 1
        nlife.destroy()
        nlife = Label(tela, text='LIFE = {}'.format(life))
        nlife['bg'] = 'black'
        nlife['fg'] = 'white'
        nlife.place(x=15, y=15)

    if life <= 0:
        pers['bg'] = 'red'
        pers['fg'] = 'red'
        pers.place(x=XI, y=YI)
        alive = False


def ZombieAttack():
    global zombie
    global pers
    global zombieattack
    global XZ
    global ZombieLife
    global life
    global XI

    ZombieLife = 3
    zombieattack = Label(tela, text=zombie)
    zombieattack['bg'] = 'red'
    zombieattack['fg'] = 'red'
    zombieattack.place(x=XZ, y=418)

    tela.update()


def ZombieMovement():
    global XI
    global zombieattack
    global XZ
    global ZombieLife
    global alive
    global points
    global npoints

    if alive:
        if XZ > XI:
            XZ -= 2
        if XZ < XI:
            XZ += 2
        zombieattack.place(x=XZ, y=418)
        if ZombieLife <= 0:
            if r(1, 2) == 1:
                XZ = -18
                zombieattack.place(x=XZ, y=418)
            else:
                XZ = 466
                zombieattack.place(x=XZ, y=418)
            points += 1
            npoints.destroy()
            npoints = Label(tela, text='SCORE = {}'.format(points))
            npoints['bg'] = 'black'
            npoints['fg'] = 'white'
            npoints.place(x=15, y=35)
            ZombieLife = 3
    tela.update()
    s(0.026)


# ===========FAZER-PULO==========#
def Ir_up(Key):
    global XI
    global YI
    global speed
    global pers
    global jump
    global zombieattack
    global XZ
    global frame
    global alive

    if jump:
        jump = False
        speed = 16
        for c in range(0, 12):
            YI -= 6
            pers.place(x=XI, y=YI)
            if alive:
                if XZ > XI:
                    XZ -= 1
                if XZ < XI:
                    XZ += 1
                zombieattack.place(x=XZ, y=418)
            s(0.026)
            tela.update()
        for c in range(0, 12):
            YI += 6
            pers.place(x=XI, y=YI)
            if alive:
                if XZ > XI:
                    XZ -= 1
                if XZ < XI:
                    XZ += 1
                zombieattack.place(x=XZ, y=418)
            s(0.026)
            tela.update()
        speed = 6
        jump = True


# ==========FAZER-RECARGA========#

def Ir_down(Key):
    global XI
    global YI
    global pers
    YI += 6
    if YI > 437:
        YI = 437
    pers.place(x=XI, y=YI)


# ===========MOVIMENTO============#

def Ir_left(Key):
    global XI
    global YI
    global pers
    global speed

    XI -= speed
    if XI < 0:
        XI = 0
    pers.place(x=XI, y=YI)


def Ir_right(Key):
    global XI
    global YI
    global pers
    global speed

    XI += speed
    if XI > 432:
        XI = 433
    pers.place(x=XI, y=YI)


def Attack_above(Key):
    global XI
    global YI
    global pers
    global attack1
    attack1.place(x=XI + 1, y=YI - 19)
    tela.update()
    attack1.place(x=-30, y=-30)


def Attack_over(Key):
    global XI
    global YI
    global pers
    global attack1
    attack1.place(x=XI + 1, y=YI + 19)
    tela.update()
    attack1.place(x=-30, y=-30)


def Attack_left(Key):
    global XI
    global YI
    global pers
    global attack1
    global ZombieLife
    global XZ

    attack1.place(x=XI - 16, y=YI)
    if XI - 35 <= XZ < XI:
        ZombieLife -= 1

    tela.update()
    s(0.026)
    attack1.place(x=-30, y=-30)


def Attack_right(Key):
    global XI
    global YI
    global pers
    global attack1
    global ZombieLife
    global XZ

    attack1.place(x=XI + 16, y=YI)
    if XI + 35 >= XZ > XI:
        ZombieLife -= 1
    tela.update()
    s(0.026)
    attack1.place(x=-30, y=-30)


def main():
    global XI
    global YI
    global pers
    global attack1
    global contFloor
    global frame
    global nlife
    global life
    global npoints
    global points

    pers = Label(tela, text=persona)
    pers['bg'] = 'blue'
    pers['fg'] = 'blue'
    pers.place(x=XI, y=YI)

    attack1 = Label(tela, text=attack)
    attack1['fg'] = 'orange'
    attack1['bg'] = 'orange'

    nlife = Label(tela, text='VIDA = {}'.format(life))
    nlife['bg'] = 'black'
    nlife['fg'] = 'white'
    nlife.place(x=15, y=15)

    npoints = Label(tela, text='SCORE = {}'.format(points))
    npoints['bg'] = 'black'
    npoints['fg'] = 'white'
    npoints.place(x=15, y=35)

    frame = Frame(tela)
    frame.bind("<d>", Ir_right)
    frame.bind("<a>", Ir_left)
    frame.bind("<w>", Ir_up)

    frame.bind("<j>", Attack_left)
    frame.bind("<l>", Attack_right)
    frame.focus_set()
    frame.place(x=-30, y=-30)

    for z in range(0, 28):
        grass = Label(tela, text=floor)
        grass['bg'] = 'green'
        grass['fg'] = 'green'
        grass.place(x=contFloor, y=437)
        contFloor += 16


tela = Tk()
tela.geometry('448x456+200+200')
tela.title('Zombie Killer')
tela['bg'] = 'black'

while __name__ == "__main__":

    if lop1:
        main()
        ZombieAttack()
        lop1 = False
    try:
        ZombieMovement()
        VerifyLifeandDamage()
        tela.update()
    except:
        break
    s(0.026)
try:
    tela.main()
except:
    pass
