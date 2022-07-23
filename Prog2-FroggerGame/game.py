import turtle


s = turtle.Screen()     # create a new screen
print (s.screensize())
w, h = s.screensize()   # get the width and height of the screen
s.setup(w+20, h+20)    # make the window a little larger than the screen object
s.tracer(0)        # disable automatic screen update

ball = turtle.Turtle()
ball.hideturtle()
ball_x = 0
ball_y = 0
ball_r = 25

player1 = turtle.Turtle()
player1.hideturtle()
player1_x = (-(w/2)+(ball_r*2))
player1_y = 0 - 50
player1.goto(player1_x,player1_y)

player2 = turtle.Turtle()
player2.hideturtle()
player2_x = ((w/2)-(ball_r*2))
player2_y = 0 - 50
player2.penup()
player2.goto(player2_x,player2_y)
player2.pendown()

pen = turtle.Turtle()
pen.penup()
pen.color("black")
pen.hideturtle()
pen.goto(0, 100)


count_x = 0
count_y = 0
score_1 = 0
score_2 = 0
ball_speed=2
max_score = 10
win_player = ''

winner = turtle.Turtle()
winner.speed(0)
winner.penup()
winner.color("white")
winner.hideturtle()
winner.goto(0, 0)

def set_score_1(value):
  global score_1
  score_1 = value
  score()

def set_score_2(value):
  global score_2
  score_2 = value
  score()

#drawing boards
def draw_rectangle(t,board_w,board_h):
    t.setheading(0)
    for i in range(2):
        t.forward(board_w)
        t.left(90)
        t.forward(board_h)
        t.left(90)


#screens for start and winning
def main_screen():
  s.bgcolor('black')
  s.onkey(play,'Return')
  winner.write("Press Enter to start!", align="center", font=("Courier", 20))
  s.listen()

def win(player):
  s.bgcolor('black')
  s.onkey(play, 'Return')
  winner.write(f" Player {player} wins!\nPress Enter to continue", align="center", font=("Courier", 20))
  s.listen()


#reset the screen
def reset():
  global score_1
  global score_2
  global ball_x
  global ball_y
  global ball_speed
  global player1_x
  global player1_y
  global player2_x
  global player2_y
  score_1=0
  score_2=0
  ball_x = 0
  ball_y = 0
  ball_speed = 2
  player1_x = (-(w/2)+(ball_r*2))
  player1_y = 0 - 50
  player1.goto(player1_x,player1_y)
  
  player2_x = ((w/2)-(ball_r*2))
  player2_y = 0 - 50
  player2.penup()
  player2.goto(player2_x,player2_y)
  player2.pendown()


#controls
def player1_up():
    global player1_y
    if ((player1.ycor() + 100) < (h/2)):
      player1_y+=20

def player1_down():
    global player1_y
    if ((player1.ycor()) > - (h/2)):  
      player1_y-=20

def player2_up():
    global player2_y
    if ((player2.ycor() + 100) < (h/2)):
      player2_y+=20

def player2_down():
    global player2_y
    if ((player2.ycor()) > - (h/2)):  
      player2_y-=20

def play():
  s.bgcolor('white')
  game_screen()     

def clear_screen():
  ball.clear()
  winner.clear()
  player1.clear()
  player2.clear()

def score():
  pen.clear()
  pen.write(f"{score_1}               {score_2}", align="center", font=("Arial", 30))


def game():
    global win_player
    global player1_x
    global player1_y
    global player2_x
    global player2_y
    global ball_x
    global ball_y
    global count_x
    global count_y
    global board_w
    global score_1
    global score_2
    global ball_speed
    global max_score

    #changing dirrection (ball_x)
    if count_x %2 == 0:
      ball_x -=ball_speed
    else:
      ball_x +=ball_speed

    #changing dirrection (ball_y)
    if count_y %2 == 0:
      ball_y -=ball_speed
    else:
      ball_y += ball_speed


    # handle conditions
    if ((ball_y - (ball_r/3)) <= -(h/2) or (ball_y + (ball_r/6)) >= (h/2)):
      count_y+=1
      ball_speed += 0.1
      print('Speed has increased')

    if ((ball_x + (ball_r/3)) >= (w/2) ):
      ball_x = 0
      ball_y = 0
      count_x+=1
      ball_speed = 2
      set_score_1(score_1+1)
      # ball_speed += 0.1
      # print('Speed has increased')

      if score_1 == max_score:
        win_player = '1'
        reset()
        win(win_player)
        return
      
      
    if ((ball_x - (ball_r/6)) <= -(w/2)):
      ball_x = 0
      ball_y = 0
      count_x+=1
      ball_speed = 2
      set_score_2(score_2+1)
      # ball_speed += 0.5
      # print('Speed has increased')

      if score_2 == max_score:
        win_player = '2'
        reset()
        win(win_player)
        return
    
    clear_screen()
    # draw
    ball.penup()
    ball.goto(ball_x,ball_y)
    ball.pendown()
    ball.dot(ball_r)

    player1.penup()
    player1.goto(player1_x-(50),player1_y)
    player1.pendown()
    draw_rectangle(player1,10,100)

    player2.penup()
    player2.goto(player2_x+(35),player2_y)
    player2.pendown()
    draw_rectangle(player2,10,100)

    s.update()
  
    #checking if player1 touched ball
    for i in range(100):
        if ball.distance(player1.xcor()-3,player1.ycor()+i) <= ball_r:
          player1.goto((-(w/2)+(ball_r*2))+10,player1_y)
          count_x+=1
    # if (player1.xcor() < ball.xcor() + (ball_r*2) and
    #     player1.xcor() + board_w() > ball.xcor() and
    #     player1.ycor() < ball.ycor() + (ball_r*2) and
    #     board_h + player1.ycor() > ball.ycor()):
            

    #checking if player2 touched ball
    for n in range(100):
        if ball.distance(player2.xcor()+13,player2.ycor()+n) <= ball_r:
            player2.goto(((w/2)+(ball_r*2))-10,player2_y)
            count_x+=1

    s.ontimer(game,10)

#main loop
def game_screen():
  global win_player
  global player1_x
  global player1_y
  global player2_x
  global player2_y
  global ball_x
  global ball_y
  global count_x
  global count_y
  global board_w
  global score_1
  global score_2
  global ball_speed
  global max_score

  s.onkey(player1_up,'w')
  s.onkey(player1_down,'s')

  s.onkey(player2_up, 'Up')
  s.onkey(player2_down, 'Down')

  s.listen()
  game()
  score()

def main():
  main_screen()

main()
