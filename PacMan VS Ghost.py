'''
Game Name: PacMan VS Ghost
Team Makers: Joscelyn Alonso, Erica Cai, Rachel Asprilla, Kevin Gomez
Objectives: A Friendly Battle Between PacMan And Ghost To Determine
A Winner Between Two Friends/Rivals
'''
#Imports
from gamelib import*
game = Game(800,780,"PacMan VS Ghost")

#Create Variables
f = Font(white,26,green,"Comice Sans MS")
F = Font(white,36,cyan,"Comice Sans MS")
NF = Font(white,18)

#Create BackGround Variables
bk = Image("PacMan VS Ghost\\Background.png",game)

l1bk = Image("PacMan VS Ghost\\level 1.png",game)
l1bk.resizeTo(game.width,game.height)

l2bk = Image("PacMan VS Ghost\\level 2.png",game)
l2bk.resizeTo(game.width,game.height)

l3bk = Image("PacMan VS Ghost\\level 3.png",game)
l3bk.resizeTo(game.width,game.height)

#Create Objects
pmr = Image("PacMan VS Ghost\\PacMan Rom.png",game)
pmr.resizeBy(-50)
pmr.moveTo(390,300)

pb = Image("PacMan VS Ghost\\Play Button.gif",game)
pb.resizeBy(-25)
pb.moveTo(390,495)

bksound = Sound("PacMan VS Ghost\\Pacman.wav",1)

#Fruit Objects
grape = Image("PacMan VS Ghost\\Grape.gif",game)
grape.resizeBy(-50)

apple = Image("PacMan VS Ghost\\Apple.gif",game)
apple.resizeBy(-50)

cherry = Image("PacMan VS Ghost\\Cherry.gif",game)
cherry.resizeBy(-25)

#Points Setup (Beans)
beans1 = []
for index in range(15):
    beans1.append(Image("PacMan VS Ghost\\Repeat\\beans1.png",game))

x = 50
for index in range(15):
    beans1[index].moveTo(x,155)
    beans1[index].resizeBy(-50)
    x +=50

beans2 = []
for index in range(10):
    beans2.append(Image("PacMan VS Ghost\\Repeat\\beans2.png",game))
    
y = 190
for index in range(10):
    beans2[index].moveTo(200,y)
    beans2[index].resizeBy(-50)
    y +=50

beans3 = []
for index in range(10):
    beans3.append(Image("PacMan VS Ghost\\Repeat\\beans3.png",game))
    
y = 190
for index in range(10):
    beans3[index].moveTo(600,y)
    beans3[index].resizeBy(-50)
    y +=50

beans4 = []
for index in range(15):
    beans4.append(Image("PacMan VS Ghost\\Repeat\\beans4.png",game))
    
x = 50
for index in range(15):
    beans4[index].moveTo(x,740)
    beans4[index].resizeBy(-50)
    x +=50

beans5 = []
for index in range(7):
    beans5.append(Image("PacMan VS Ghost\\Repeat\\beans5.png",game))

x = 50
for index in range(7):
    beans5[index].moveTo(x,45)
    beans5[index].resizeBy(-50)
    x +=50

beans6 = []
for index in range(7):
    beans6.append(Image("PacMan VS Ghost\\Repeat\\beans6.png",game))

x = 450
for index in range(7):
    beans6[index].moveTo(x,45)
    beans6[index].resizeBy(-50)
    x +=50

beans7 = []
for index in range(4):
    beans7.append(Image("PacMan VS Ghost\\Repeat\\beans7.png",game))

x = 50
for index in range(4):
    beans7[index].moveTo(x,690)
    beans7[index].resizeBy(-50)
    x +=50

beans8 = [] 
for index in range(4):
    beans8.append(Image("PacMan VS Ghost\\Repeat\\beans8.png",game))

x = 600
for index in range(4):
    beans8[index].moveTo(x,690)
    beans8[index].resizeBy(-50)
    x +=50

beans9 = []
for index in range(3):
    beans9.append(Image("PacMan VS Ghost\\Repeat\\beans9.png",game))

x = 50
for index in range(3):
    beans9[index].moveTo(x,240)
    beans9[index].resizeBy(-50)
    x +=50

beans10 = []
for index in range(2):
    beans10.append(Image("PacMan VS Ghost\\Repeat\\beans10.png",game))

x = 300
for index in range(2):
    beans10[index].moveTo(x,240)
    beans10[index].resizeBy(-50)
    x +=50

beans11 = []
for index in range(2):
    beans11.append(Image("PacMan VS Ghost\\Repeat\\beans11.png",game))

x = 450
for index in range(2):
    beans11[index].moveTo(x,240)
    beans11[index].resizeBy(-50)
    x +=50

beans12 = []
for index in range(3):
    beans12.append(Image("PacMan VS Ghost\\Repeat\\beans12.png",game))

x = 650
for index in range(3):
    beans12[index].moveTo(x,240)
    beans12[index].resizeBy(-50)
    x +=50

beans13 = []
for index in range(5):
    beans13.append(Image("PacMan VS Ghost\\Repeat\\beans13.png",game))

x = 300
for index in range(5):
    beans13[index].moveTo(x,300)
    beans13[index].resizeBy(-50)
    x +=50

beans14 = []
for index in range(5):
    beans14.append(Image("PacMan VS Ghost\\Repeat\\beans14.png",game))

x = 300
for index in range(5):
    beans14[index].moveTo(x,450)
    beans14[index].resizeBy(-50)
    x +=50

beans15 = []
for index in range(3):
    beans15.append(Image("PacMan VS Ghost\\Repeat\\beans15.png",game))

x = 50
for index in range(3):
    beans15[index].moveTo(x,540)
    beans15[index].resizeBy(-50)
    x +=50

beans16 = []
for index in range(3):
    beans16.append(Image("PacMan VS Ghost\\Repeat\\beans16.png",game))

x = 250
for index in range(3):
    beans16[index].moveTo(x,540)
    beans16[index].resizeBy(-50)
    x +=50

beans17 = []
for index in range(3):
    beans17.append(Image("PacMan VS Ghost\\Repeat\\beans17.png",game))

x = 450
for index in range(3):
    beans17[index].moveTo(x,540)
    beans17[index].resizeBy(-50)
    x +=50

beans18 = []
for index in range(3):
    beans18.append(Image("PacMan VS Ghost\\Repeat\\beans18.png",game))

x = 650
for index in range(3):
    beans18[index].moveTo(x,540)
    beans18[index].resizeBy(-50)
    x +=50

beans19 = []
for index in range(3):
    beans19.append(Image("PacMan VS Ghost\\Repeat\\beans19.png",game))

x = 50
for index in range(3):
    beans19[index].moveTo(x,590)
    beans19[index].resizeBy(-50)
    x +=50

beans20 = []
for index in range(7):
    beans20.append(Image("PacMan VS Ghost\\Repeat\\beans20.png",game))

x = 250
for index in range(7):
    beans20[index].moveTo(x,590)
    beans20[index].resizeBy(-50)
    x +=50

beans21 = []
for index in range(3):
    beans21.append(Image("PacMan VS Ghost\\Repeat\\beans20.png",game))

x = 650
for index in range(3):
    beans21[index].moveTo(x,590)
    beans21[index].resizeBy(-50)
    x +=50

beans22 = []
for index in range(2):
    beans22.append(Image("PacMan VS Ghost\\Repeat\\beans22.png",game))

x = 300
for index in range(2):
    beans22[index].moveTo(x,690)
    beans22[index].resizeBy(-50)
    x +=50

beans23 = []
for index in range(2):
    beans23.append(Image("PacMan VS Ghost\\Repeat\\beans23.png",game))

x = 450
for index in range(2):
    beans23[index].moveTo(x,690)
    beans23[index].resizeBy(-50)
    x +=50

#Rice Ball Setup
riceball1 = []
for index in range(3):
    riceball1.append(Image("PacMan VS Ghost\\Repeat\\Rice Ball 1.gif",game))

x = 50
for index in range(3):
    riceball1[index].moveTo(x,100)
    riceball1[index].resizeBy(-50)
    x +=155

riceball2 = []
for index in range(3):
    riceball2.append(Image("PacMan VS Ghost\\Repeat\\Rice Ball 2.gif",game))

x = 445
for index in range(3):
    riceball2[index].moveTo(x,100)
    riceball2[index].resizeBy(-50)
    x +=155

#Tempura Bowl Setup
tempurabowl1 = []
for index in range(2):
    tempurabowl1.append(Image("PacMan VS Ghost\\Repeat\\Tempura Bowl1.gif",game))

x = 50
for index in range(2):
    tempurabowl1[index].moveTo(x,200)
    tempurabowl1[index].resizeBy(-50)
    x +=230

tempurabowl2 = []
for index in range(2):
    tempurabowl2.append(Image("PacMan VS Ghost\\Repeat\\Tempura Bowl2.gif",game))

x = 520
for index in range(2):
    tempurabowl2[index].moveTo(x,200)
    tempurabowl2[index].resizeBy(-50)
    x +=230

#Curry Setup
curry = []
for index in range(2):
    curry.append(Image("PacMan VS Ghost\\Curry.gif",game))

x = 280
for index in range(2):
    curry[index].moveTo(x,390)
    curry[index].resizeBy(-50)
    x +=240

#Mild Curry Setup
mildcurry = []
for index in range(2):
    mildcurry.append(Image("PacMan VS Ghost\\Mild Curry.gif",game))

x = 280
for index in range(2):
    mildcurry[index].moveTo(x,490)
    mildcurry[index].resizeBy(-50)
    x +=240

#Shaved Ice Cream Setup
shavedicecream1 = []
for index in range(2):
    shavedicecream1.append(Image("PacMan VS Ghost\\Repeat\\Shaved Ice Cream1.gif",game))

x = 130
for index in range(2):
    shavedicecream1[index].moveTo(x,640)
    shavedicecream1[index].resizeBy(-50)
    x +=150

shavedicecream2 = []
for index in range(2):
    shavedicecream2.append(Image("PacMan VS Ghost\\Repeat\\Shaved Ice Cream2.gif",game))

x = 520
for index in range(2):
    shavedicecream2[index].moveTo(x,640)
    shavedicecream2[index].resizeBy(-50)
    x +=150

#Characters
pacman = Animation("PacMan VS Ghost\\PacMan Sprite.gif",3,game,40,124/3,frate=6)

ghost = Animation("PacMan VS Ghost\\Ghost.gif",5,game,94,434/5,frate=6)
ghost.resizeBy(-40)
'''--------------------------------------------------------------------------'''                   
#Title Screen
game.over = False
while not game.over:
    game.processInput()
    bk.draw()
    pmr.draw()
    pb.draw()
    
    if pb.collidedWith(mouse)and mouse.LeftClick:
        game.over = True
        bksound.play()

    game.update(30)
'''--------------------------------------------------------------------------'''
#Relocation For Level 1
pacman.moveTo(697,390)
ghost.moveTo(100,390)
grape.moveTo(400,375)

#Level 1
game.over = False
pp = 0
gp = 0
while not game.over:
    game.processInput()
    l1bk.draw()
    grape.draw()
    pacman.draw()
    ghost.draw()
    bksound.play()

    game.drawText("Use W,A,S,D",33,300,f)
    game.drawText("to move Ghost",25,325,f)

    game.drawText("Use arrow keys",665,300,f)
    game.drawText("to move PacMan",662,325,f)

    #Point System (Bean System)
    for index in range(15):
        beans1[index].draw()
        if beans1[index].collidedWith(pacman):
            pp += 1
            beans1[index].visible = False

        if beans1[index].collidedWith(ghost):
            gp += 1
            beans1[index].visible = False

    for index in range(10):
        beans2[index].draw()
        if beans2[index].collidedWith(pacman):
            pp += 1
            beans2[index].visible = False

        if beans2[index].collidedWith(ghost):
            gp += 1
            beans2[index].visible = False

    for index in range(10):
        beans3[index].draw()
        if beans3[index].collidedWith(pacman):
            pp += 1
            beans3[index].visible = False

        if beans3[index].collidedWith(ghost):
            gp += 1
            beans3[index].visible = False

    for index in range(15):
        beans4[index].draw()
        if beans4[index].collidedWith(pacman):
            pp += 1
            beans4[index].visible = False
            
        if beans4[index].collidedWith(ghost):
            gp += 1
            beans4[index].visible = False

    for index in range(7):
        beans5[index].draw()
        if beans5[index].collidedWith(pacman):
            pp += 1
            beans5[index].visible = False
            
        if beans5[index].collidedWith(ghost):
            gp += 1
            beans5[index].visible = False

    for index in range(7):
        beans6[index].draw()
        if beans6[index].collidedWith(pacman):
            pp += 1
            beans6[index].visible = False
            
        if beans6[index].collidedWith(ghost):
            gp += 1
            beans6[index].visible = False

    for index in range(4):
        beans7[index].draw()
        if beans7[index].collidedWith(pacman):
            pp += 1
            beans7[index].visible = False
            
        if beans7[index].collidedWith(ghost):
            gp += 1
            beans7[index].visible = False

    for index in range(4):
        beans8[index].draw()
        if beans8[index].collidedWith(pacman):
            pp += 1
            beans8[index].visible = False
            
        if beans8[index].collidedWith(ghost):
            gp += 1
            beans8[index].visible = False

    for index in range(3):
        beans9[index].draw()
        if beans9[index].collidedWith(pacman):
            pp += 1
            beans9[index].visible = False

        if beans9[index].collidedWith(ghost):
            gp += 1
            beans9[index].visible = False

    for index in range(2):
        beans10[index].draw()
        if beans10[index].collidedWith(pacman):
            pp += 1
            beans10[index].visible = False

        if beans10[index].collidedWith(ghost):
            gp += 1
            beans10[index].visible = False

    for index in range(2):
        beans11[index].draw()
        if beans11[index].collidedWith(pacman):
            pp += 1
            beans11[index].visible = False

        if beans11[index].collidedWith(ghost):
            gp += 1
            beans11[index].visible = False

    for index in range(3):
        beans12[index].draw()
        if beans12[index].collidedWith(pacman):
            pp += 1
            beans12[index].visible = False

        if beans12[index].collidedWith(ghost):
            gp += 1
            beans12[index].visible = False

    for index in range(5):
        beans13[index].draw()
        if beans13[index].collidedWith(pacman):
            pp += 1
            beans13[index].visible = False

        if beans13[index].collidedWith(ghost):
            gp += 1
            beans13[index].visible = False

    for index in range(5):
        beans14[index].draw()
        if beans14[index].collidedWith(pacman):
            pp += 1
            beans14[index].visible = False

        if beans14[index].collidedWith(ghost):
            gp += 1
            beans14[index].visible = False

    for index in range(3):
        beans15[index].draw()
        if beans15[index].collidedWith(pacman):
            pp += 1
            beans15[index].visible = False

        if beans15[index].collidedWith(ghost):
            gp += 1
            beans15[index].visible = False

    for index in range(3):
        beans16[index].draw()
        if beans16[index].collidedWith(pacman):
            pp += 1
            beans16[index].visible = False

        if beans16[index].collidedWith(ghost):
            gp += 1
            beans16[index].visible = False

    for index in range(3):
        beans17[index].draw()
        if beans17[index].collidedWith(pacman):
            pp += 1
            beans17[index].visible = False

        if beans17[index].collidedWith(ghost):
            gp += 1
            beans17[index].visible = False

    for index in range(3):
        beans18[index].draw()
        if beans18[index].collidedWith(pacman):
            pp += 1
            beans18[index].visible = False

        if beans18[index].collidedWith(ghost):
            gp += 1
            beans18[index].visible = False

    for index in range(3):
        beans19[index].draw()
        if beans19[index].collidedWith(pacman):
            pp += 1
            beans19[index].visible = False

        if beans19[index].collidedWith(ghost):
            gp += 1
            beans19[index].visible = False

    for index in range(7):
        beans20[index].draw()
        if beans20[index].collidedWith(pacman):
            pp += 1
            beans20[index].visible = False

        if beans20[index].collidedWith(ghost):
            gp += 1
            beans20[index].visible = False

    for index in range(3):
        beans21[index].draw()
        if beans21[index].collidedWith(pacman):
            pp += 1
            beans21[index].visible = False

        if beans21[index].collidedWith(ghost):
            gp += 1
            beans21[index].visible = False

    for index in range(2):
        beans22[index].draw()
        if beans22[index].collidedWith(pacman):
            pp += 1
            beans22[index].visible = False

        if beans22[index].collidedWith(ghost):
            gp += 1
            beans22[index].visible = False

    for index in range(2):
        beans23[index].draw()
        if beans23[index].collidedWith(pacman):
            pp += 1
            beans23[index].visible = False

        if beans23[index].collidedWith(ghost):
            gp += 1
            beans23[index].visible = False

    #Rice Ball System (Points Setup)
    for index in range(3):
        riceball1[index].draw()
        if riceball1[index].collidedWith(pacman):
            pp += 5
            pacman.health += 5
            riceball1[index].visible = False
            
        if riceball1[index].collidedWith(ghost):
            gp += 5
            ghost.health += 5
            riceball1[index].visible = False

    for index in range(3):
        riceball2[index].draw()
        if riceball2[index].collidedWith(pacman):
            pp += 5
            pacman.health += 5
            riceball2[index].visible = False
            
        if riceball2[index].collidedWith(ghost):
            gp += 5
            ghost.health += 5
            riceball2[index].visible = False

    #Tempura Bowl System (Points Setup)
    for index in range(2):
        tempurabowl1[index].draw()
        if tempurabowl1[index].collidedWith(pacman):
            pp += 10
            pacman.health -= 5
            tempurabowl1[index].visible = False

        if tempurabowl1[index].collidedWith(ghost):
            gp += 10
            pacman.health -=5
            tempurabowl1[index].visible = False

    for index in range(2):
        tempurabowl2[index].draw()
        if tempurabowl2[index].collidedWith(pacman):
            pp += 10
            pacman.health -= 5
            tempurabowl2[index].visible = False

        if tempurabowl2[index].collidedWith(ghost):
            gp += 10
            pacman.health -=5
            tempurabowl2[index].visible = False

    #Curry System (Points Setup)
    for index in range(2):
        curry[index].draw()
        if curry[index].collidedWith(pacman):
            pp -= 15
            pacman.health -= 10
            curry[index].visible = False

        if curry[index].collidedWith(ghost):
            gp -= 15
            ghost.health -= 10
            curry[index].visible = False

    #Mild Curry System (Points Setup)
    for index in range(2):
        mildcurry[index].draw()
        if mildcurry[index].collidedWith(pacman):
            pp -= 5
            pacman.health += 10
            mildcurry[index].visible = False

        if mildcurry[index].collidedWith(ghost):
            gp -= 5
            ghost.health += 10
            mildcurry[index].visible = False

    #Shaved Ice Cream System (Points Setup)
    for index in range(2):
        shavedicecream1[index].draw()
        if shavedicecream1[index].collidedWith(pacman):
            pp += 5
            pacman.health -= 5
            shavedicecream1[index].visible = False

        if shavedicecream1[index].collidedWith(ghost):
            gp += 5
            ghost.health -= 5
            shavedicecream1[index].visible = False

    for index in range(2):
        shavedicecream2[index].draw()
        if shavedicecream2[index].collidedWith(pacman):
            pp += 5
            pacman.health -= 5
            shavedicecream2[index].visible = False

        if shavedicecream2[index].collidedWith(ghost):
            gp += 5
            ghost.health -= 5
            shavedicecream2[index].visible = False
        

    #If Statements
    if pp > 85 and pacman.collidedWith(grape) and pacman.health > 45:
        game.over = True

    if gp > 85 and ghost.collidedWith(grape) and ghost.health > 45:
        game.over = True

    #Teleportation
    if pacman.isOffScreen("left"):
        pacman.moveTo(697,390)
        
    if pacman.isOffScreen("right"):
        pacman.moveTo(100,390)

    if ghost.isOffScreen("left"):
        ghost.moveTo(697,390)
        
    if ghost.isOffScreen("right"):
        ghost.moveTo(100,390)
        
    #PacMan Control
    if keys.Pressed[K_UP]:
        pacman.y -= 4
        pacman.rotateTo(90)
    if keys.Pressed[K_DOWN]:
        pacman.y += 4
        pacman.rotateTo(270)
    if keys.Pressed[K_RIGHT]:
        pacman.x += 4
        pacman.rotateTo(360)
    if keys.Pressed[K_LEFT]:
        pacman.x -= 4
        pacman.rotateTo(180)

    #Ghost Control
    if keys.Pressed[K_w]:
        ghost.y -= 4
    if keys.Pressed[K_s]:
        ghost.y += 4
    if keys.Pressed[K_d]:
        ghost.x += 4
    if keys.Pressed[K_a]:
        ghost.x -= 4

    #Pointing System
    game.drawText("Health: " + str(pacman.health),655,440,F)
    game.drawText("Health: " + str(ghost.health),15,440,F)
    game.drawText("Points: " + str(pp),655,465,F)
    game.drawText("Points: " + str(gp),15,465,F)
    game.update(60)
'''----------------------------------------------------------------------------------'''
#Relocation For Level 2
pacman.moveTo(765,40)
ghost.moveTo(50,745)

#Points Setup
beans1 = []
for index in range(15):
    beans1.append( Image ("PacMan VS Ghost\\Repeat\\beans1.png",game))

x = 50
for index in range(15):
    beans1[index].moveTo(x,125)
    beans1[index].resizeBy(-50)
    x +=50

beans2 = []
for index in range(9):
    beans2.append( Image ("PacMan VS Ghost\\Repeat\\beans2.png",game))
    
y = 160
for index in range(9):
    beans2[index].moveTo(130,y)
    beans2[index].resizeBy(-50)
    y +=50

beans3 = []
for index in range(9):
    beans3.append( Image ("PacMan VS Ghost\\Repeat\\beans3.png",game))
    
y = 160
for index in range(9):
    beans3[index].moveTo(675,y)
    beans3[index].resizeBy(-50)
    y +=50

beans4 = []
for index in range(15):
    beans4.append( Image ("PacMan VS Ghost\\Repeat\\beans4.png",game))
    
x = 50
for index in range(15):
    beans4[index].moveTo(x,610)
    beans4[index].resizeBy(-50)
    x +=50

beans5 = []
for index in range(4):
    beans5.append(Image("PacMan VS Ghost\\Repeat\\beans5.png",game))

x = 50
for index in range(4):
    beans5[index].moveTo(x,45)
    beans5[index].resizeBy(-50)
    x +=50

beans6 = []
for index in range(5):
    beans6.append(Image("PacMan VS Ghost\\Repeat\\beans6.png",game))

x = 300
for index in range(5):
    beans6[index].moveTo(x,45)
    beans6[index].resizeBy(-50)
    x +=50

beans7 = []
for index in range(4):
    beans7.append(Image("PacMan VS Ghost\\Repeat\\beans7.png",game))

x = 200
for index in range(4):
    beans7[index].moveTo(x,235)
    beans7[index].resizeBy(-50)
    x +=50

beans8 = [] 
for index in range(4):
    beans8.append(Image("PacMan VS Ghost\\Repeat\\beans8.png",game))

x = 450
for index in range(4):
    beans8[index].moveTo(x,235)
    beans8[index].resizeBy(-50)
    x +=50

beans9 = []
for index in range(9):
    beans9.append(Image("PacMan VS Ghost\\Repeat\\beans9.png",game))

x = 200
for index in range(9):
    beans9[index].moveTo(x,325)
    beans9[index].resizeBy(-50)
    x +=50

beans10 = []
for index in range(3):
    beans10.append(Image("PacMan VS Ghost\\Repeat\\beans10.png",game))

x = 200
for index in range(3):
    beans10[index].moveTo(x,375)
    beans10[index].resizeBy(-50)
    x +=50

beans11 = []
for index in range(3):
    beans11.append(Image("PacMan VS Ghost\\Repeat\\beans11.png",game))

x = 515
for index in range(3):
    beans11[index].moveTo(x,375)
    beans11[index].resizeBy(-50)
    x +=50

beans12 = []
for index in range(5):
    beans12.append(Image("PacMan VS Ghost\\Repeat\\beans12.png",game))

x = 300
for index in range(5):
    beans12[index].moveTo(x,465)
    beans12[index].resizeBy(-50)
    x +=50

beans13 = []
for index in range(4):
    beans13.append(Image("PacMan VS Ghost\\Repeat\\beans13.png",game))

x = 200
for index in range(4):
    beans13[index].moveTo(x,515)
    beans13[index].resizeBy(-50)
    x +=50

beans14 = []
for index in range(5):
    beans14.append(Image("PacMan VS Ghost\\Repeat\\beans14.png",game))

x = 450
for index in range(5):
    beans14[index].moveTo(x,515)
    beans14[index].resizeBy(-50)
    x +=50

beans15 = []
for index in range(3):
    beans15.append(Image("PacMan VS Ghost\\Repeat\\beans15.png",game))

x = 600
for index in range(3):
    beans15[index].moveTo(x,45)
    beans15[index].resizeBy(-50)
    x +=50

beans16 = []
for index in range(2):
    beans16.append(Image("PacMan VS Ghost\\Repeat\\beans16.png",game))

x = 300
for index in range(2):
    beans16[index].moveTo(x,660)
    beans16[index].resizeBy(-50)
    x +=50

beans17 = []
for index in range(2):
    beans17.append(Image("PacMan VS Ghost\\Repeat\\beans17.png",game))

x = 450
for index in range(2):
    beans17[index].moveTo(x,660)
    beans17[index].resizeBy(-50)
    x +=50

beans18 = []
for index in range(14):
    beans18.append(Image("PacMan VS Ghost\\Repeat\\beans18.png",game))

x = 100
for index in range(14):
    beans18[index].moveTo(x,745)
    beans18[index].resizeBy(-50)
    x +=50

beans19 = []
for index in range(2):
    beans19.append(Image("PacMan VS Ghost\\Repeat\\beans19.png",game))

y = 660
for index in range(2):
    beans19[index].moveTo(50,y)
    beans19[index].resizeBy(-50)
    y +=50

beans20 = []
for index in range(2):
    beans20.append(Image("PacMan VS Ghost\\Repeat\\beans20.png",game))

y = 660
for index in range(2):
    beans20[index].moveTo(600,y)
    beans20[index].resizeBy(-50)
    y += 50

beans21 = []
for index in range(2):
    beans21.append(Image("PacMan VS Ghost\\Repeat\\beans21.png",game))

y = 655
for index in range(2):
    beans21[index].moveTo(210,y)
    beans21[index].resizeBy(-50)
    y +=50

beans22 = []
for index in range(2):
    beans22.append(Image("PacMan VS Ghost\\Repeat\\beans22.png",game))

y = 655
for index in range(2):
    beans22[index].moveTo(750,y)
    beans22[index].resizeBy(-50)
    y += 50

beans23 = []
for index in range(2):
    beans23.append(Image("PacMan VS Ghost\\Repeat\\beans23.png",game))

x = 200
for index in range(2):
    beans23[index].moveTo(x,460)
    beans23[index].resizeBy(-50)
    x += 400

#Rice Ball Setup
riceball1 = []
for index in range(2):
    riceball1.append(Image("PacMan VS Ghost\\Repeat\\Rice Ball 1.gif",game))

x = 50
for index in range(2):
    riceball1[index].moveTo(x,80)
    riceball1[index].resizeBy(-50)
    x +=155

riceball2 = []
for index in range(2):
    riceball2.append(Image("PacMan VS Ghost\\Repeat\\Rice Ball 2.gif",game))

x = 290
for index in range(2):
    riceball2[index].moveTo(x,80)
    riceball2[index].resizeBy(-50)
    x +=235

riceball3 = []
for index in range(2):
    riceball3.append(Image("PacMan VS Ghost\\Repeat\\Rice Ball 3.gif",game))

x = 595
for index in range(2):
    riceball3[index].moveTo(x,80)
    riceball3[index].resizeBy(-50)
    x +=160

riceball4 = []
for index in range(2):
    riceball4.append(Image("PacMan VS Ghost\\Repeat\\Rice Ball 4.gif",game))

x = 290
for index in range(2):
    riceball4[index].moveTo(x,705)
    riceball4[index].resizeBy(-50)
    x +=230
    

#Tempura Bowl Setup
tempurabowl1 = []
for index in range(2):
    tempurabowl1.append(Image("PacMan VS Ghost\\Repeat\\Tempura Bowl1.gif",game))

x = 210
for index in range(2):
    tempurabowl1[index].moveTo(x,185)
    tempurabowl1[index].resizeBy(-50)
    x +=160

tempurabowl2 = []
for index in range(2):
    tempurabowl2.append(Image("PacMan VS Ghost\\Repeat\\Tempura Bowl2.gif",game))

x = 445
for index in range(2):
    tempurabowl2[index].moveTo(x,185)
    tempurabowl2[index].resizeBy(-50)
    x +=160

#Curry Setup
curry = []
for index in range(2):
    curry.append(Image("PacMan VS Ghost\\Curry.gif",game))

x = 285
for index in range(2):
    curry[index].moveTo(x,280)
    curry[index].resizeBy(-50)
    x +=235

#Mild Curry Setup
mildcurry = []
for index in range(2):
    mildcurry.append(Image("PacMan VS Ghost\\Mild Curry.gif",game))

x = 290
for index in range(2):
    mildcurry[index].moveTo(x,560)
    mildcurry[index].resizeBy(-50)
    x +=235

#Shaved Ice Cream Setup
shavedicecream1 = []
for index in range(2):
    shavedicecream1.append(Image("PacMan VS Ghost\\Repeat\\Shaved Ice Cream1.gif",game))

x = 210
for index in range(2):
    shavedicecream1[index].moveTo(x,420)
    shavedicecream1[index].resizeBy(-50)
    x +=80

shavedicecream2 = []
for index in range(2):
    shavedicecream2.append(Image("PacMan VS Ghost\\Repeat\\Shaved Ice Cream2.gif",game))

x = 525
for index in range(2):
    shavedicecream2[index].moveTo(x,420)
    shavedicecream2[index].resizeBy(-50)
    x +=75
'''--------------------------------------------------------------------------'''
#Level 2
game.over = False
pp = 0
gp = 0
while not game.over:
    game.processInput()
    l2bk.draw()
    cherry.draw()
    pacman.draw()
    ghost.draw()

    #Point System
    for index in range(15):
        beans1[index].draw()
        if beans1[index].collidedWith(pacman):
            pp += 1
            beans1[index].visible = False

        if beans1[index].collidedWith(ghost):
            gp += 1
            beans1[index].visible = False

    for index in range(9):
        beans2[index].draw()
        if beans2[index].collidedWith(pacman):
            pp += 1
            beans2[index].visible = False

        if beans2[index].collidedWith(ghost):
            gp += 1
            beans2[index].visible = False

    for index in range(9):
        beans3[index].draw()
        if beans3[index].collidedWith(pacman):
            pp += 1
            beans3[index].visible = False

        if beans3[index].collidedWith(ghost):
            gp += 1
            beans3[index].visible = False

    for index in range(15):
        beans4[index].draw()
        if beans4[index].collidedWith(pacman):
            pp += 1
            beans4[index].visible = False
            
        if beans4[index].collidedWith(ghost):
            gp += 1
            beans4[index].visible = False

    for index in range(4):
        beans5[index].draw()
        if beans5[index].collidedWith(pacman):
            pp += 1
            beans5[index].visible = False

        if beans5[index].collidedWith(ghost):
            gp += 1
            beans5[index].visible = False

    for index in range(5):
        beans6[index].draw()
        if beans6[index].collidedWith(pacman):
            pp += 1
            beans6[index].visible = False

        if beans6[index].collidedWith(ghost):
            gp += 1
            beans6[index].visible = False

    for index in range(4):
        beans7[index].draw()
        if beans7[index].collidedWith(pacman):
            pp += 1
            beans7[index].visible = False

        if beans7[index].collidedWith(ghost):
            gp += 1
            beans7[index].visible = False

    for index in range(4):
        beans8[index].draw()
        if beans8[index].collidedWith(pacman):
            pp += 1
            beans8[index].visible = False

        if beans8[index].collidedWith(ghost):
            gp += 1
            beans8[index].visible = False

    for index in range(9):
        beans9[index].draw()
        if beans9[index].collidedWith(pacman):
            pp += 1
            beans9[index].visible = False

        if beans9[index].collidedWith(ghost):
            gp += 1
            beans9[index].visible = False

    for index in range(3):
        beans10[index].draw()
        if beans10[index].collidedWith(pacman):
            pp += 1
            beans10[index].visible = False

        if beans10[index].collidedWith(ghost):
            gp += 1
            beans10[index].visible = False

    for index in range(3):
        beans11[index].draw()
        if beans11[index].collidedWith(pacman):
            pp += 1
            beans11[index].visible = False

        if beans11[index].collidedWith(ghost):
            gp += 1
            beans11[index].visible = False

    for index in range(5):
        beans12[index].draw()
        if beans12[index].collidedWith(pacman):
            pp += 1
            beans12[index].visible = False

        if beans12[index].collidedWith(ghost):
            gp += 1
            beans12[index].visible = False

    for index in range(4):
        beans13[index].draw()
        if beans13[index].collidedWith(pacman):
            pp += 1
            beans13[index].visible = False

        if beans13[index].collidedWith(ghost):
            gp += 1
            beans13[index].visible = False

    for index in range(4):
        beans14[index].draw()
        if beans14[index].collidedWith(pacman):
            pp += 1
            beans14[index].visible = False

        if beans14[index].collidedWith(ghost):
            gp += 1
            beans14[index].visible = False

    for index in range(3):
        beans15[index].draw()
        if beans15[index].collidedWith(pacman):
            pp += 1
            beans15[index].visible = False

        if beans15[index].collidedWith(ghost):
            gp += 1
            beans15[idnex].visible = False

    for index in range(2):
        beans16[index].draw()
        if beans16[index].collidedWith(pacman):
            pp += 1
            beans16[index].visible = False

        if beans16[index].collidedWith(ghost):
            gp += 1
            beans16[index].visible = False

    for index in range(2):
        beans17[index].draw()
        if beans17[index].collidedWith(pacman):
            pp += 1
            beans17[index].visible = False

        if beans17[index].collidedWith(ghost):
            gp += 1
            beans17[index].visible = False

    for index in range(14):
        beans18[index].draw()
        if beans18[index].collidedWith(pacman):
            pp += 1
            beans18[index].visible = False

        if beans18[index].collidedWith(ghost):
            gp += 1
            beans18[index].visible = False

    for index in range(2):
        beans19[index].draw()
        if beans19[index].collidedWith(pacman):
            pp += 1
            beans19[index].visible = False

        if beans19[index].collidedWith(ghost):
            gp += 1
            beans19[index].visible = False

    for index in range(2):
        beans20[index].draw()
        if beans20[index].collidedWith(pacman):
            pp += 1
            beans20[index].visible = False

        if beans20[index].collidedWith(ghost):
            gp += 1
            beans20[index].visible = False

    for index in range(2):
        beans21[index].draw()
        if beans21[index].collidedWith(pacman):
            pp += 1
            beans21[index].visible = False

        if beans21[index].collidedWith(ghost):
            gp += 1
            beans21[index].visible = False

    for index in range(2):
        beans22[index].draw()
        if beans22[index].collidedWith(pacman):
            pp += 1
            beans22[index].visible = False

        if beans22[index].collidedWith(ghost):
            gp += 1
            beans22[index].visible = False

    for index in range(2):
        beans23[index].draw()
        if beans23[index].collidedWith(pacman):
            pp += 1
            beans23[index].visible = False

        if beans23[index].collidedWith(ghost):
            gp += 1
            beans23[index].visible = False

    #Rice Ball System (Points Setup)
    for index in range(2):
        riceball1[index].draw()
        if riceball1[index].collidedWith(pacman):
            pp += 5
            pacman.health += 5
            riceball1[index].visible = False
            
        if riceball1[index].collidedWith(ghost):
            gp += 5
            ghost.health += 5
            riceball1[index].visible = False

    for index in range(2):
        riceball2[index].draw()
        if riceball2[index].collidedWith(pacman):
            pp += 5
            pacman.health += 5
            riceball2[index].visible = False
            
        if riceball2[index].collidedWith(ghost):
            gp += 5
            ghost.health += 5
            riceball2[index].visible = False

    for index in range(2):
        riceball3[index].draw()
        if riceball3[index].collidedWith(pacman):
            pp += 5
            pacman.health += 5
            riceball3[index].visible = False
            
        if riceball3[index].collidedWith(ghost):
            gp += 5
            ghost.health += 5
            riceball3[index].visible = False

    for index in range(2):
        riceball4[index].draw()
        if riceball4[index].collidedWith(pacman):
            pp += 5
            pacman.health += 5
            riceball4[index].visible = False
            
        if riceball4[index].collidedWith(ghost):
            gp += 5
            ghost.health += 5
            riceball4[index].visible = False

    #Tempura Bowl System (Points Setup)
    for index in range(2):
        tempurabowl1[index].draw()
        if tempurabowl1[index].collidedWith(pacman):
            pp += 10
            pacman.health -= 5
            tempurabowl1[index].visible = False

        if tempurabowl1[index].collidedWith(ghost):
            gp += 10
            pacman.health -=5
            tempurabowl1[index].visible = False

    for index in range(2):
        tempurabowl2[index].draw()
        if tempurabowl2[index].collidedWith(pacman):
            pp += 10
            pacman.health -= 5
            tempurabowl2[index].visible = False

        if tempurabowl2[index].collidedWith(ghost):
            gp += 10
            pacman.health -=5
            tempurabowl2[index].visible = False

    #Curry System (Points Setup)
    for index in range(2):
        curry[index].draw()
        if curry[index].collidedWith(pacman):
            pp -= 15
            pacman.health -= 10
            curry[index].visible = False

        if curry[index].collidedWith(ghost):
            gp -= 15
            ghost.health -= 10
            curry[index].visible = False

    #Mild Curry System (Points Setup)
    for index in range(2):
        mildcurry[index].draw()
        if mildcurry[index].collidedWith(pacman):
            pp -= 5
            pacman.health += 10
            mildcurry[index].visible = False

        if mildcurry[index].collidedWith(ghost):
            gp -= 5
            ghost.health += 10
            mildcurry[index].visible = False

    #Shaved Ice Cream System (Points Setup)
    for index in range(2):
        shavedicecream1[index].draw()
        if shavedicecream1[index].collidedWith(pacman):
            pp += 5
            pacman.health -= 5
            shavedicecream1[index].visible = False

        if shavedicecream1[index].collidedWith(ghost):
            gp += 5
            ghost.health -= 5
            shavedicecream1[index].visible = False

    for index in range(2):
        shavedicecream2[index].draw()
        if shavedicecream2[index].collidedWith(pacman):
            pp += 5
            pacman.health -= 5
            shavedicecream2[index].visible = False

        if shavedicecream2[index].collidedWith(ghost):
            gp += 5
            ghost.health -= 5
            shavedicecream2[index].visible = False

    #If Statements
    if pp > 92 and pacman.collidedWith(cherry) and pacman.health > 50:
        game.over = True

    if gp > 92 and ghost.collidedWith(cherry) and ghost.health > 50:
        game.over = True

    #PacMan's Teleportation
    if pacman.isOffScreen("left")and pacman.y > 300:
        pacman.moveTo(725,237)
        
    if pacman.isOffScreen("right")and pacman.y > 300:
        pacman.moveTo(45,237)

    if pacman.isOffScreen("left")and pacman.y < 300:
        pacman.moveTo(725,465)
        
    if pacman.isOffScreen("right")and pacman.y < 300:
        pacman.moveTo(45,465)
        
    #Ghost's Teleportation
    if ghost.isOffScreen("left")and ghost.y > 300:
        ghost.moveTo(725,237)
        
    if ghost.isOffScreen("right")and ghost.y > 300:
        ghost.moveTo(45,237)
        
    if ghost.isOffScreen("left")and ghost.y < 300:
        ghost.moveTo(725,465)
        
    if ghost.isOffScreen("right")and ghost.y < 300:
        ghost.moveTo(45,465)
        
    #PacMan Control
    if keys.Pressed[K_UP]:
        pacman.y -= 4
        pacman.rotateTo(90)
    if keys.Pressed[K_DOWN]:
        pacman.y += 4
        pacman.rotateTo(270)
    if keys.Pressed[K_RIGHT]:
        pacman.x += 4
        pacman.rotateTo(360)
    if keys.Pressed[K_LEFT]:
        pacman.x -= 4
        pacman.rotateTo(180)

    #Ghost Control
    if keys.Pressed[K_w]:
        ghost.y -= 4
    if keys.Pressed[K_s]:
        ghost.y += 4
    if keys.Pressed[K_d]:
        ghost.x += 4
    if keys.Pressed[K_a]:
        ghost.x -= 4

    #Pointing System
    game.drawText("Health: " + str(pacman.health),730,300,NF)
    game.drawText("Health: " + str(ghost.health),15,300,NF)
    game.drawText("Points: " + str(pp),730,390,NF)
    game.drawText("Points: " + str(gp),15,390,NF)
    game.update(60)

game.quit()

#https://pythonspot.com/maze-in-pygame/
#https://gist.github.com/parsons-Jsr/4043325/revisions
