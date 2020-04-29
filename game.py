import turtle 
import os
import math
import random
import platform

        
#Screen Setup
wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Space Raiders")
wn.bgpic("/Users/zeinabalazzawi/Desktop/python game/background3.gif")
wn.tracer(0)


#register the shapes
turtle.register_shape("/Users/zeinabalazzawi/Desktop/python game/rocket1.gif")
turtle.register_shape("/Users/zeinabalazzawi/Desktop/python game/cat1.gif")
turtle.register_shape("/Users/zeinabalazzawi/Desktop/python game/fish1.gif")


#Border
border_pen = turtle.Turtle()
border_pen.speed(0) 
border_pen.color("white")
border_pen.penup() 
border_pen.setposition(-300,-300)
border_pen.pensize(3)
for side in range(4):
    border_pen.fd(500)
    border_pen.lt(90)
border_pen.hideturtle()

#set the score to 0
score = 0

#draw the score
score_pen = turtle.Turtle()
score_pen.speed(0)
score_pen.color("white")
score_pen.penup()
score_pen.setposition(-290, 280)
scorestring = "Score: {}" .format(score) 
score_pen.write(scorestring, False, align="left", font=("Arial", 14, "normal"))
score_pen.hideturtle()


#Player Turtle
player = turtle.Turtle()
player.color("blue")
player.shape("/Users/zeinabalazzawi/Desktop/python game/rocket1.gif")
player.penup()
player.speed(0)
player.setposition(0,-250)
player.setheading(90)
player.speed = 0


#choose number of enemies
number_of_enemies = 30
#create an empty list of enemies
enemies = []

#add enemies to the list
for i in range(number_of_enemies):
    #create enemy
    enemies.append(turtle.Turtle())

enemy_start_x = -225
enemy_start_y = 250
enemy_number = 0


for enemy in enemies:
    enemy.color("red")
    enemy.shape("/Users/zeinabalazzawi/Desktop/python game/cat1.gif")
    enemy.penup()
    enemy.speed(0)
    x = enemy_start_x + (50 * enemy_number)
    y = enemy_start_y 
    enemy.setposition(x,y)
    #update the enemy number
    enemy_number += 1
    if enemy_number == 10:
        enemy_start_y -= 50
        enemy_number = 0

enemyspeed = 0.2

#create the player's bullet
bullet = turtle.Turtle()
bullet.color("yellow")
bullet.shape("/Users/zeinabalazzawi/Desktop/python game/fish1.gif")
bullet.penup()
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(0.5, 0.5)
bullet.hideturtle()

bulletspeed = 10

#define bullet state
#ready - ready to fire
#fire - bullet is firing
bulletstate = "ready"


#moving left and right
def move_left():
    player.speed = -3

def move_right():
    player.speed = 3
    x = player.xcor()


def move_player():
    x = player.xcor()
    x += player.speed
    if x < - 280:
        x = - 280
    if x > 280:
        x = 280
    player.setx(x)
    
def fire_bullet():
    #declare bulletstate as a global if it needs changed
    global bulletstate
    if bulletstate == "ready":
            play_sound("laser.wav")
            bulletstate = "fire"
            #move bullet just above the player
            x = player.xcor()
            y = player.ycor() + 10
            bullet.setposition(x, y)
            bullet.showturtle()

def isCollision(t1, t2):
    distance = math.sqrt(math.pow(t1.xcor()-t2.xcor(),2)+math.pow(t1.ycor()-t2.ycor(),2))
    if distance < 15:
        return True
    else:
        return False

def play_sound(sound_file, time = 60):
        os.system("afplay {}&".format(sound_file))
        if time > 0:
              turtle.ontimer(lambda: play_sound(sound_file, time), t=int(time * 1000))    
    

#create keyboard bindings
wn.listen()
wn.onkeypress(move_left,"Left")
wn.onkeypress(move_right,"Right")
wn.onkeypress(fire_bullet, "space")

#play background music
play_sound("space.wav", 60)

#main game loop
while True:

    wn.update()
    move_player()

    for enemy in enemies:
        #move the enemy
        x = enemy.xcor()
        x += enemyspeed
        enemy.setx(x)

        #move enemy up and down
        if enemy.xcor() >280:
            #move all enemies down
            for e in enemies:
                y = e.ycor()
                y -= 40
                e.sety(y)
            #change enemy direction
            enemyspeed *= -1
                
            

        if enemy.xcor() < -280:
            #move all enemies down
            for e in enemies:
                y = e.ycor()
                y -= 40
                e.sety(y)
            #change enemy direction
            enemyspeed *= -1

        #Check for a collision between the bullet and enemy
        if isCollision(bullet,enemy):
            play_sound("meow.wav")
            #reset the bullet
            bullet.hideturtle()
            bulletstate = "ready"
            bullet.setposition(0, -400)
            #Reset the enemy
            enemy.setposition(0, 10000)
            #update the score
            score += 10
            scorestring = "Score: {}" .format(score) 
            score_pen.clear()
            score_pen.write(scorestring, False, align="left", font=("Arial", 14, "normal"))
            
        if isCollision(player, enemy):
            play_sound("meow.wav")
            player.hideturtle()
            print ("Game Over")
            break
            
            
    #move the bullet
    if bulletstate == "fire":
        y = bullet.ycor()
        y += bulletspeed
        bullet.sety(y)

    #check to see if bullet reach top
    if bullet.ycor() >275:
        bullet.hideturtle()
        bulletstate = "ready"

   
        

