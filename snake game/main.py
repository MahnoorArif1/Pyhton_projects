from turtle import Screen
import food
import score
from snake import Snake
import time
import winsound

def pause_game():
    global is_paused
    is_paused = not is_paused
def game_over():
    global is_paused
    is_paused = True
    score_board.game_over_text()
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)
snake = Snake()
snake_food=food.Food()
score_board=score.Score()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
screen.onkey(pause_game, "space")
game_speed = 0.15
game_is_on = True
is_paused = False
while game_is_on:
    screen.update()
    time.sleep(game_speed)
    if is_paused:
        time.sleep(0.1)
        continue
    snake.move()
    # if snake eats the food
    if snake.head.distance(snake_food)<=15:
        winsound.Beep(1000, 100)
        snake_food.refresh()
        score_board.cal_score()
        snake.extend()
        #increasing speed as it eats food
        if game_speed > 0.05:
            game_speed -= 0.005
# if snake hits the wall
    if (snake.head.xcor()>295 or snake.head.xcor()<-295) or (snake.head.ycor()>295 or snake.head.ycor()<-295):
        snake.snake_reset()
# if it collides with any part of its own
    for segment in snake.segments[1:]:
        if snake.head.distance(segment)<5:
            winsound.Beep(200, 500)
            score_board.game_over_text()
            score_board.game_reset()
            score_board.ref()
            snake.new_snake()
screen.exitonclick()
