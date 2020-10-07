#Pacman Ghost Algorithm - www.101computing.net/pacman-ghost-algorithm/
#Wa.01 remake version in python
from math import atan, cos, sin
from processing import *

WIDTH=300
HEIGHT=300
pacman_X = 30
pacman_Y = 30
delay = 5

ghost_X = 10
ghost_Y = 10

def setup():
    strokeWeight(3)
    frameRate(60)
    size(500,500)

def moveGhost():
  global ghost_X,ghost_Y,pacman_X,pacman_Y
  fill(211, 253, 131)
  stroke(255,255,255)

  #Find out the direction (angle) the Ghost needs to move towards
  #Using SOH-CAH-TOA trignometic rations
  opposite=pacman_Y-ghost_Y
  adjacent=pacman_X-ghost_X
  angle = atan(opposite/adjacent)
  if ghost_X>pacman_X:
    angle=angle+180

  #Use this angle to calculate the velocity vector of the Ghost
  #Once again using SOH-CAH-TOA trignometic rations
  velocity=3 #pixels per frame

  vx = velocity * cos(angle)
  vy = velocity * sin(angle)

  #Apply velocity vector to the Ghost coordinates to move/translate the ghost
  ghost_X = ghost_X + vx
  ghost_Y = ghost_Y + vy

  #Draw Ghost
  ellipse( ghost_X,ghost_Y,50,50)

def movePacman():
    global pacman_X, pacman_Y

    fill(197, 54, 33)
    stroke(0,0,0)
    fc = environment.frameCount

    #Pacman follows the mouse cursor
    pacman_X += (mouse.x-pacman_X)*1.2/(delay);
    pacman_Y += (mouse.y-pacman_Y)*1.2/(delay);


    #Draw Pacman
    ellipse(pacman_X,pacman_Y,20,20)

def playGame():
  background(50,50,150)
  movePacman()
  moveGhost()

draw = playGame
run()
