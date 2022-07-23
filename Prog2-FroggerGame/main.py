######################################################
# Project: <assignment name>
# UIN: <656538534>
# repl.it URL: https://replit.com/@MykolaTurchak/Frogger#main.py
 
######################################################

# imports
import turtle
import random

#creating variables
s = turtle.Screen()

s.screensize(300, 300)
s.setup(330, 330)
w,h = s.screensize()
s.tracer(0)

print('w:', w, 'h:',h)

radius = 30

player_x = 0
player_y = -h/2 + radius

earth_x = -w/2 + radius
earth_y = h/2 - radius

left_object_x = w/2 - radius
left_object_y = h/2 - (radius *2)

right_object_x = -w/2 + radius
right_object_y = h/2 - (radius *3)

l_speed = 2
r_speed = 2
player_speed = 30

winner = turtle.Turtle()
winner.speed(0)
winner.penup()
winner.color("white")
winner.hideturtle()
winner.goto(0, 0)

count = 0

play = 'over'
score = 0

def main():
  #giving main() access to the variables
  global radius

  global player_x
  global player_y

  global earth_x
  global earth_y

  global left_object_x
  global left_object_y

  global right_object_x
  global right_object_y

  global l_speed
  global r_speed
  global player_speed

  global play
  global score



  #creating and appending objects
  objects = [{'t': turtle.Turtle(), 'x': random.randint(earth_x, earth_y),'y': earth_y,  'radius': radius, 'image': 'sun.gif', 'type': 'sun'}]

  objects.append({'t': turtle.Turtle(), 'x': player_x, 'y':player_y,  'radius': radius, 'image': 'earth.gif', 'type': 'player'})
  
  for i in range(3):
    objects.append({'t': turtle.Turtle(), 'x': random.randint(earth_x, earth_y), 'y':right_object_y,  'radius': radius, 'image': 'moon.gif', 'type': 'moon_left'})
    right_object_y -=60
  
  for i in range(4):
      objects.append({'t': turtle.Turtle(), 'x': random.randint(earth_x, earth_y), 'y':left_object_y, 'radius': radius, 'image': 'moon.gif', 'type': 'moon_right'})
      left_object_y -= 60



  #adding shapes
  def add_shape():
    for obj in objects:
        s.addshape(obj['image'])
        obj['t'].shape(obj['image'])



  #functions for the movement
  def right():
    for obj in objects:
      if obj['type'] == 'player' and obj['x'] <= w/2 -radius:
        obj['x'] += player_speed
         
  def up():
    for obj in objects:
      if obj['type'] == 'player' and obj['y'] <= h/2 -radius:
        obj['y'] += player_speed

  def left():
    for obj in objects:
      if obj['type'] == 'player' and obj['x'] >= -w/2 +radius:
        obj['x'] -= player_speed

  def down():
      for obj in objects :
        if obj['type'] == 'player' and obj['y'] >= -h/2 + (radius*2):
          obj['y'] -= player_speed



  #clearing all the objects
  def clearing():
    for obj in objects:
        obj['t'].clear()


  #main function that runs the game
  def render_game():
    global count
    global score

    add_shape()
    winner.clear()

    #loop that keeps the game running
    while play == 'play':
      s.bgpic('sky.gif')
      
      for obj in objects:
        clearing()

        #direction
        if obj['type'] == 'moon_right':
          obj['x'] +=r_speed
          if obj['x'] > w/2 + obj['radius']:
            obj['x'] = -w/2 - obj['radius']

        if obj['type'] == 'moon_left':
          obj['x'] -=l_speed
          if obj['x'] < -w/2 - obj['radius']:
            obj['x'] = w/2 + obj['radius']

        #colision check
        if obj['type']== 'moon_left' or obj['type']== 'moon_right':
          if objects[1]['t'].distance(obj['t']) < radius :
            objects[1]['x'] = 0
            objects[1]['y'] = -h/2 + radius

        if obj['type']== 'sun':
          if objects[1]['t'].distance(obj['t']) < radius :
            
            #if touched the sun, end the game
            if count == 1 or count == 3:
              score+=10
              play == 'over'
              end_screen()
            count+=1
            continue

        #drawing dictinary iteams
        obj['t'].penup()
        obj['t'].goto(obj['x'], obj['y'])
        obj['t'].pendown()

        #writting score
      if play == 'play':
        winner.penup()
        winner.goto(90,-140)
        winner.write(f'Your Score: {score}', align="center", font=("Courier", 10))

      #key events
      s.onkey(up, 'Up') 
      s.onkey(down, 'Down')
      s.onkey(left, 'Left')
      s.onkey(right, 'Right')

      #listening to the keys being pressed
      s.listen()

      #updating the screen
      s.update()
  

  #creating pre game screen  
  def pre_game_screen():
    global play
    play = 'play'
    s.bgcolor('black')
    s.onkey(render_game, 'Return')
    winner.write("Press Enter to continue", align="center", font=("Courier", 15))
    s.listen()



  #end screen
  def end_screen():
    s.clear()
    global play
    play = 'over'
    s.bgcolor('black')
    winner.goto(0, 0)
    winner.write(f'You Won!\nYour Score: {score}', align="center", font=("Courier", 15))
    
  
  pre_game_screen()

  s.listen()
     

main()
