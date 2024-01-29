import json
import os
import queue
import random
import sys

from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtCore import Qt, QBasicTimer
from PyQt6.QtGui import QPainter, QBrush
from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox

# setting:
FOOD_NUM = 30
TIME_INTERVAL = 5
BOARD_ROW = 20
BOARD_COLUMN = 30
AUTO_PLAY = True
SPEED = 500

UP = 1
DOWN = -1
LEFT = 2
RIGHT = -2

# prohibit changing numbers
BLANK = 0
HEAD = 1
BODY = 2
FOOD = 3


class Snake:

    def __init__(self):
        self.row = BOARD_ROW  # y
        self.column = BOARD_COLUMN  # x
        # init the head
        self.head = [random.randint(3, self.column - 3), random.randint(3, self.row - 3)]  # x, y
        # init the tail
        self.tail = self.head
        # init the board
        self.board = [[BLANK for _ in range(self.row)] for _ in range(self.column)]  # [row][column]; [x][y]
        self.board[self.head[0]][self.head[1]] = HEAD  # [x][y]
        # init the direction
        self.direction = UP
        # init the food
        self.food_num = FOOD_NUM
        self.food = [[-1, -1] for _ in range(self.food_num)]
        # init the snake
        self.live = True
        self.length = 1
        # init the snake queue
        self.snake_queue = queue.Queue(self.row * self.column)
        self.snake_queue.put(self.head)
        self.new_food()
        # print("snake init done...")

    def new_food(self):
        # update previous food positions
        for f in self.food:
            if f != [-1, -1]:
                self.board[f[0]][f[1]] = BLANK
        # initialize food list to [-1, -1]
        self.food = [[-1, -1] for _ in range(self.food_num)]
        # get new food positions
        count = 0
        while count <= self.food_num - 1:
            temp_food = [random.randint(0, self.column - 1), random.randint(0, self.row - 1)]
            if self.board[temp_food[0]][temp_food[1]] != BLANK:
                continue
            else:
                # print("new food position: " + str(temp_food))
                self.food[count] = temp_food
                self.board[temp_food[0]][temp_food[1]] = FOOD
                count += 1

    def check_collision(self, direction):
        collision = False
        new_head = self.head[:]
        if direction == UP:
            if self.head[1] == 0:
                collision = True
            new_head[1] -= 1
        elif direction == DOWN:
            if self.head[1] == self.row - 1:
                collision = True
            new_head[1] += 1
        elif direction == LEFT:
            if self.head[0] == 0:
                collision = True
            new_head[0] -= 1
        elif direction == RIGHT:
            if self.head[0] == self.column - 1:
                collision = True
            new_head[0] += 1
        return collision, new_head

    def go(self, direction):
        if direction + self.direction == 0:  # contrary to the previous direction
            # print("snake wants to shrink...")
            pass
        else:
            self.direction = direction
       
        collision, new_head = self.check_collision(self.direction)
        if collision:
            # print("snake hits border")
            self.live = False
        else:
            if new_head in self.food:  # encounter food
                # print("snake gets food...")
                self.length += 1
                self.board[new_head[0]][new_head[1]] = HEAD
                self.board[self.head[0]][self.head[1]] = BODY
                self.head = new_head[:]
                self.snake_queue.put(self.head)
                food_index = self.food.index(new_head)
                self.food[food_index] = [-1, -1]
            elif self.board[new_head[0]][new_head[1]] == BODY:
                # print("snack eats its body...")
                self.live = False
            elif self.board[new_head[0]][new_head[1]] == BLANK:
                # print("snake just forward... direction: {}".format(direction))
                self.board[self.head[0]][self.head[1]] = BODY  # update previous head position to body
                # print(self.head)
                self.head = new_head[:]
                # print(self.head)
                self.board[self.head[0]][self.head[1]] = HEAD  # update new head position
                self.snake_queue.put(new_head)
                self.tail = self.snake_queue.get()
                self.board[self.tail[0]][self.tail[1]] = BLANK  # update previous tail position to blank

class Game(QMainWindow):
    def __init__(self):
        super().__init__()
        Game.load_configuration()
        self.title = "Snake Game"
        self.size = 30
        self.opacity = 1
        self.update_timer = QBasicTimer()
        self.status_bar = self.statusBar()
        self.brush = [QBrush(QtGui.QColor('while'), Qt.BrushStyle.SolidPattern), QBrush(QtGui.QColor('blue'), Qt.BrushStyle.SolidPattern),
                      QBrush(QtGui.QColor('green'), Qt.BrushStyle.SolidPattern), QBrush(QtGui.QColor('yellow'), Qt.BrushStyle.SolidPattern)]
        self.time_count = 0
        # snake
        self.snake = Snake()
        self.row = self.snake.row  # y
        self.column = self.snake.column  # x

        self.init_ui()
        self.init_game()

    def init_game(self):
        # print("game init...")
        self.update_timer.start(SPEED, self)

    def init_ui(self):
        self.resize(self.column * self.size, self.row * self.size)
        self.setWindowTitle(self.title)
        self.setWindowOpacity(self.opacity)
        self.show()

    def paintEvent(self, event):
        painter = QPainter()
        painter.begin(self)
        for x in range(self.column):
            for y in range(self.row):
                # print("current block state: {}".format(self.snake.board[x][y]))
                painter.setBrush(self.brush[self.snake.board[x][y]])
                painter.drawRect(x * self.size, y * self.size, self.size, self.size)

        painter.end()

    def timerEvent(self, event):
        if event.timerId() == self.update_timer.timerId():
            self.time_count += 1
            if self.snake.live:
                self.snake.go(self.auto_play())
                if self.time_count % TIME_INTERVAL == 0:
                    self.snake.new_food()
            else:
                self.game_over()
        self.update()

    def auto_play(self):
        if not AUTO_PLAY:
            return self.snake.direction
        else:
            direction_list = [UP, DOWN, RIGHT, LEFT]
            final_direction = self.snake.direction
            for d in direction_list:
                if d + self.snake.direction != 0:
                    collision, new_head = self.snake.check_collision(d)
                    if collision or self.snake.board[new_head[0]][new_head[1]] == BODY:
                        continue
                    else:
                        if new_head in self.snake.food:
                            final_direction = d
                            return final_direction
                        elif self.snake.board[new_head[0]][new_head[1]] == BLANK:
                            final_direction = d
                            continue

            return final_direction

    def game_over(self):
        answer = QMessageBox.question(self, "Game Over",
                                      "Time: {0}\nLength: {1}\nDo you want to try again?".format(self.time_count,
                                                                                                 self.snake.length),
                                      QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        if answer == QMessageBox.StandardButton.Yes:
            self.snake = Snake()
        else:
            sys.exit(app.exec())

    def keyPressEvent(self, event):
        if self.snake.live:
            if event.key() == Qt.Key.Key_W:
                self.snake.go(UP)
            elif event.key() == Qt.Key.Key_S:
                self.snake.go(DOWN)
            elif event.key() == Qt.Key.Key_A:
                self.snake.go(LEFT)
            elif event.key() == Qt.Key.Key_D:
                self.snake.go(RIGHT)
            elif event.key() == Qt.Key.Key_P:
                pass
            self.update()

    @classmethod
    def load_configuration(cls):
        try:
            profile_name = "config.json"
            exist = os.path.exists(profile_name)
            if not exist:
                with open(profile_name, 'w', encoding='utf-8') as f:
                    config_dict = {'FOOD_NUM': 30, 'TIME_INTERVAL': 5, 'BOARD_ROW': 20, 'BOARD_COLUMN': 30,
                                   'AUTO_PLAY': True, 'SPEED': 1000}
                    f.write(json.dumps(config_dict, sort_keys=True, indent=4, separators=(",", ":")))
            else:
                with open(profile_name, 'r') as f:
                    global FOOD_NUM, TIME_INTERVAL, BOARD_ROW, BOARD_COLUMN, AUTO_PLAY, SPEED
                    config_dict = json.loads(f.read())
                    FOOD_NUM = config_dict['FOOD_NUM']
                    TIME_INTERVAL = config_dict['TIME_INTERVAL']
                    BOARD_ROW = config_dict['BOARD_ROW']
                    BOARD_COLUMN = config_dict['BOARD_COLUMN']
                    AUTO_PLAY = config_dict['AUTO_PLAY']
                    SPEED = config_dict['SPEED']
        except IOError:
            print("There was a error when load profile.")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Game()
    sys.exit(app.exec())