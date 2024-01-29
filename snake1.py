import sys
import cv2
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QApplication, QMainWindow, QGraphicsScene, QGraphicsView
from PyQt6.QtCore import Qt, QPointF, QTimer
from PyQt6.QtGui import QPainter, QBrush, QColor, QPen
import numpy as np


class Ui_MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Khởi tạo các biến
        self.scene = QGraphicsScene()
        self.view = QGraphicsView(self.scene)
        self.setCentralWidget(self.view)
        self.setGeometry(0, 0, 500, 500)
        self.setWindowTitle("Game rắn")
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_game)
        self.timer.start(100)
        self.last_key_pressed = None
        self.direction = QPointF(1, 0)
        self.snake = [QPointF(4, 0), QPointF(3, 0), QPointF(2, 0), QPointF(1, 0), QPointF(0, 0)]
        self.food_position = QPointF(3, 3)
        
        # Khởi tạo OpenCV để phát hiện chuyển động
        self.cap = cv2.VideoCapture(0)
        self.background = None
        self.threshold = 20
        self.accumulated_weight = 0.5
       
    def update_game(self):
        # Xoá màn hình trở lại
        self.scene.clear()

        # Thêm thức ăn
        brush = QBrush(QColor(200, 0, 0))
        self.scene.addEllipse(self.food_position.x() * 25, self.food_position.y() * 25, 25, 25, QPen(QtGui.QColor('while')), brush)

        # Cập nhật vị trí của con rắn theo hướng đi
        new_position = self.snake[0] + self.direction
        self.snake.insert(0, new_position)
        self.snake.pop()

        # Kiểm tra xem con rắn ăn được thức ăn hay không
        if new_position == self.food_position:
            self.food_position = QPointF(np.random.randint(0, 19), np.random.randint(0, 19))
            self.snake.append(self.snake[-1])

        # Kiểm tra xem con rắn va chạm vào tường hay không
        if new_position.x() < 0 or new_position.x() > 19 or new_position.y() < 0 or new_position.y() > 19:
            self.timer.stop()
            print("Game over")

        # Kiểm tra xem con rắn va chạm vào cơ thể của nó hay không
        if new_position in self.snake[1:]:
            self.timer.stop()
            print("Game over")
        
        # Vẽ con rắn lên màn hình
        brush = QBrush(QtGui.QColor('while'))
        for i, p in enumerate(self.snake):
            self.scene.addEllipse(p.x() * 25, p.y() * 25, 25, 25, QPen(QtGui.QColor('while')), brush)

        # Lấy hướng đi từ phím nhấn hoặc chuyển động của tay
        key_pressed = self.last_key_pressed
        ret, frame = self.cap.read()
        frame = cv2.flip(frame, 1)
        frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        frame_gray = cv2.GaussianBlur(frame_gray, (7, 7), 0)

        if self.background is None:
            self.background = frame_gray
        else:
            diff = cv2.absdiff(self.background, frame_gray)
            thresholded = cv2.threshold(diff, self.threshold, 255, cv2.THRESH_BINARY)[1]
            thresholded = cv2.dilate(thresholded, None, iterations=2)
            contours, _ = cv2.findContours(thresholded, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            if len(contours) > 0:
                hand_contour = max(contours, key=cv2.contourArea)
                hand_center = np.mean(hand_contour, axis=0)
                hand_center = np.squeeze(hand_center)
                direction_vector = hand_center - np.array([250, 250])
                # print(direction_vector)
                
                if np.abs(direction_vector[0]) > np.abs(direction_vector[1]):
                    if direction_vector[0] > 0:
                        key_pressed = Qt.Key.Key_Right
                    else:
                        key_pressed = Qt.Key.Key_Left
                else:
                    if direction_vector[1] > 0:
                        key_pressed = Qt.Key.Key_Down
                    else:
                        key_pressed = Qt.Key.Key_Up
                    
        if key_pressed == Qt.Key.Key_Left and self.direction != QPointF(1, 0):
            self.direction = QPointF(-1, 0)
        elif key_pressed == Qt.Key.Key_Right and self.direction != QPointF(-1, 0):
            self.direction = QPointF(1, 0)
        elif key_pressed == Qt.Key.Key_Up and self.direction != QPointF(0, 1):
            self.direction = QPointF(0, -1)
        elif key_pressed == Qt.Key.Key_Down and self.direction != QPointF(0, -1):
            self.direction = QPointF(0, 1)

        self.last_key_pressed = None
       
        
    def keyPressEvent(self, event):
        """Lưu phím cuối cùng được nhấn"""
        self.last_key_pressed = event.key()
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    game = Ui_MainWindow()
    game.show()
    sys.exit(app.exec())