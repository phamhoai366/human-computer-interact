# Pyshine
from random import choice
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QFileDialog
from PyQt6.QtGui import QImage
import imutils
import time
import numpy as np
import cv2,os
import pyshine as ps
from keras.models import load_model

class Ui_MainWindow(object):
	def setupUi(self, MainWindow):
		MainWindow.setObjectName("MainWindow")
		MainWindow.resize(800, 600)
		self.centralwidget = QtWidgets.QWidget(MainWindow)
		self.centralwidget.setObjectName("centralwidget")
		self.gridLayout_8 = QtWidgets.QGridLayout(self.centralwidget)
		self.gridLayout_8.setObjectName("gridLayout_8")
		self.gridLayout_5 = QtWidgets.QGridLayout()
		self.gridLayout_5.setObjectName("gridLayout_5")
		self.gridLayout = QtWidgets.QGridLayout()
		self.gridLayout.setObjectName("gridLayout")
		spacerItem = QtWidgets.QSpacerItem(158, 0, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
		self.gridLayout.addItem(spacerItem, 0, 0, 1, 1)
		self.label_4 = QtWidgets.QLabel(self.centralwidget)
		self.label_4.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";")
		self.label_4.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
		self.label_4.setObjectName("label_4")
		self.gridLayout.addWidget(self.label_4, 0, 1, 1, 1)
		spacerItem1 = QtWidgets.QSpacerItem(118, 0, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
		self.gridLayout.addItem(spacerItem1, 0, 2, 1, 1)
		self.gridLayout_5.addLayout(self.gridLayout, 0, 0, 1, 2)
		self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
		self.groupBox.setObjectName("groupBox")
		self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox)
		self.gridLayout_3.setObjectName("gridLayout_3")
		spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
		self.gridLayout_3.addItem(spacerItem2, 1, 1, 1, 1)
		self.label = QtWidgets.QLabel(self.groupBox)
		
		self.label.setObjectName("label")
		self.gridLayout_3.addWidget(self.label, 0, 1, 1, 1)
		spacerItem3 = QtWidgets.QSpacerItem(0, 188, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
		self.gridLayout_3.addItem(spacerItem3, 0, 2, 1, 1)
		self.gridLayout_5.addWidget(self.groupBox, 1, 0, 1, 1)
		self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
		self.groupBox_2.setObjectName("groupBox_2")
		self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox_2)
		self.gridLayout_2.setObjectName("gridLayout_2")
		self.label_2 = QtWidgets.QLabel(self.groupBox_2)

		self.label_2.setObjectName("label_2")
		self.gridLayout_2.addWidget(self.label_2, 0, 1, 1, 1)
		spacerItem4 = QtWidgets.QSpacerItem(0, 188, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
		self.gridLayout_2.addItem(spacerItem4, 0, 0, 1, 1)
		spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
		self.gridLayout_2.addItem(spacerItem5, 1, 1, 1, 1)
		self.gridLayout_5.addWidget(self.groupBox_2, 1, 1, 1, 1)
		self.gridLayout_4 = QtWidgets.QGridLayout()
		self.gridLayout_4.setObjectName("gridLayout_4")
		spacerItem6 = QtWidgets.QSpacerItem(148, 0, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
		self.gridLayout_4.addItem(spacerItem6, 0, 0, 1, 1)
		self.label_3 = QtWidgets.QLabel(self.centralwidget)
		self.label_3.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";")
		self.label_3.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
		self.label_3.setObjectName("label_3")
		self.gridLayout_4.addWidget(self.label_3, 0, 1, 1, 1)
		spacerItem7 = QtWidgets.QSpacerItem(158, 0, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
		self.gridLayout_4.addItem(spacerItem7, 0, 2, 1, 1)
		self.gridLayout_5.addLayout(self.gridLayout_4, 2, 0, 1, 2)
		self.gridLayout_8.addLayout(self.gridLayout_5, 0, 0, 1, 1)
		self.gridLayout_7 = QtWidgets.QGridLayout()
		self.gridLayout_7.setObjectName("gridLayout_7")
		self.gridLayout_6 = QtWidgets.QGridLayout()
		self.gridLayout_6.setObjectName("gridLayout_6")
		self.label_5 = QtWidgets.QLabel(self.centralwidget)
		self.label_5.setObjectName("label_5")
		self.gridLayout_6.addWidget(self.label_5, 0, 1, 1, 1)
		self.label_6 = QtWidgets.QLabel(self.centralwidget)
		self.label_6.setObjectName("label_6")
		self.pushButton = QtWidgets.QPushButton(self.centralwidget)
		self.pushButton.setObjectName("pushButton")
		self.gridLayout_6.addWidget(self.pushButton, 0, 5, 1, 1)
		self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
		self.pushButton_3.setObjectName("pushButton_3")
		self.gridLayout_7.addWidget(self.pushButton_3, 2, 0, 1, 1)
		spacerItem8 = QtWidgets.QSpacerItem(346, 17, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
		self.gridLayout_7.addItem(spacerItem8, 2, 1, 1, 1)
		self.radioButton = QtWidgets.QRadioButton(self.centralwidget)
		self.radioButton.setObjectName("radioButton")
		self.gridLayout_7.addWidget(self.radioButton, 2, 2, 1, 2)
		self.radioButton_2 = QtWidgets.QRadioButton(self.centralwidget)
		self.radioButton_2.setChecked(True)
		self.radioButton_2.setObjectName("radioButton_2")
		self.gridLayout_7.addWidget(self.radioButton_2, 2, 4, 1, 1)
		self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
		self.pushButton_4.setObjectName("pushButton_4")
		self.gridLayout_7.addWidget(self.pushButton_4, 2, 5, 1, 1)
		self.gridLayout_8.addLayout(self.gridLayout_7, 1, 0, 1, 1)
		MainWindow.setCentralWidget(self.centralwidget)
		self.statusbar = QtWidgets.QStatusBar(MainWindow)
		self.statusbar.setObjectName("statusbar")
		MainWindow.setStatusBar(self.statusbar)

		self.pushButton_4.clicked.connect(self.loadImage)
		self.pushButton_3.clicked.connect(self.loadModel)
		self.pushButton_4.setEnabled(False)
		self.radioButton.clicked.connect(self.selectVideo)
		self.radioButton_2.clicked.connect(self.selectCam)

		self.retranslateUi(MainWindow)
		QtCore.QMetaObject.connectSlotsByName(MainWindow)
		self.started = False

		self.acquire = False
		self.loaded_model = None
		self.test  =  False
		self.cam = True 

		self.CLASS_DICT = {
		"Rock": 0,
		"Paper": 1,
		"Scissors": 2,
		"None": 3
		}
		
		self.REV_CLASS_DICT = {
		0: "Rock",
		1: "Paper",
		2: "Scissors",
		3: "None"
		}

		self.ROCK_IMAGE = cv2.imread('images/Rock.jpg')
		self.ROCK_IMAGE  = imutils.resize(self.ROCK_IMAGE ,height = 480 )
		self.PAPER_IMAGE = cv2.imread('images/Paper.jpg')
		self.PAPER_IMAGE  = imutils.resize(self.PAPER_IMAGE ,height = 480 )
		self.SCISSORS_IMAGE = cv2.imread('images/Scissors.jpg')
		self.SCISSORS_IMAGE  = imutils.resize(self.SCISSORS_IMAGE ,height = 480 )
		self.NONE_IMAGE = cv2.imread('images/Try.png')
		self.NONE_IMAGE  = imutils.resize(self.NONE_IMAGE ,height = 480 )
		self.DETECTED_IMAGE = self.NONE_IMAGE

		self.W = 28
		self.H = 28
		self.winner='None'
		self.radioButton.setEnabled(False)
		
	def selectCam(self):
		self.cam = True
	
	def selectVideo(self):
		self.cam = True
		
	def loadModel(self):
		"""
		This function will open a file dialog to let user load the model (.h5 file only)
		after that set the status message
		"""
		model_filename = QFileDialog.getOpenFileName(filter="Keras (*.h5)")[0]
		try:
			self.loaded_model = load_model(model_filename)
			self.test = True
			self.pushButton_4.setEnabled(True)
			self.radioButton.setEnabled(True)
			self.label_3.setText("STATUS: Model loaded! Press Start")
		except Exception as e:
			pass
			# print(e)
			self.label_3.setText("STATUS: {}".format(e))

		
	def find_winner(self,predicted_name, pc_selected_name):
		if predicted_name == pc_selected_name:
			return "Tie"

		if predicted_name == "Rock":
			if pc_selected_name == "Scissors":
				return "User Win"
			if pc_selected_name == "Paper":
				return "Computer Win"

		if predicted_name == "Paper":
			if pc_selected_name == "Rock":
				return "User Win"
			if pc_selected_name == "Scissors":
				return "Computer Win"

		if predicted_name == "Scissors":
			if pc_selected_name == "Paper":
				return "User Win"
			if pc_selected_name == "Rock":
				return "Computer Win"
				
	def mapper(self,labels):
		return self.CLASS_DICT[labels]

	def demapper(self,val):
		return self.REV_CLASS_DICT[val]
	
		
	def loadImage(self):		
		if self.started:
			self.started=False
			self.pushButton_4.setText('Start')	
			# self.pushButton_2.setEnabled(True)
			self.pushButton_3.setEnabled(True)

		else:
			self.started=True
			self.pushButton_4.setText('Stop')
			# self.pushButton_2.setEnabled(False)
			self.pushButton_3.setEnabled(False)			
		
		if self.cam:
			vid = cv2.VideoCapture(0)
			
		else:			
			video_filename =  'out.avi'
			vid = cv2.VideoCapture(video_filename)
				
		cnt=0
		frames_to_count=20
		st = 0
		sample_count=0
		prev_move = None
		while(vid.isOpened()):
		
			_, self.image = vid.read()
			try:
				self.image  = imutils.resize(self.image ,height = 480 )
			except:
				break
	
			if cnt == frames_to_count:
				try: # To avoid divide by 0 we put it in try except
					self.fps = round(frames_to_count/(time.time()-st)) 						
					st = time.time()
					cnt=0
				except:
					pass
			
			cnt+=1
			if self.acquire:
				
				roi = self.image[80:310, 80:310]
				save_path = os.path.join(self.IMG_CLASS_PATH, '{}.jpg'.format(sample_count + 1))
				sample_count+=1
				Total = int(self.samples)
				value = (sample_count/Total)*100
				self.progressBar.setValue(value)
				cv2.imwrite(save_path, roi)
				
				if sample_count == int(self.samples):
					self.acquire = False
					sample_count = 0
					self.pushButton_3.setEnabled(True)
			
			if self.test:
				roi = self.image[80:310, 80:310]
				time.sleep(0.033)
				img = cv2.cvtColor(roi, cv2.COLOR_BGR2RGB)
				img = cv2.resize(img, (self.W, self.H))
				
				img = img.astype('float32')
		
				
				img = img/255
				pred = self.loaded_model.predict(np.array([img]))
				
				pred_key = np.argmax(pred[0])
				predicted_name = self.demapper(pred_key)
				
				self.image = ps.putBText(self.image,predicted_name.upper(),text_offset_x=80,text_offset_y=10,font_scale=1.5,text_RGB=(220,0,0))
	
				# Find who is the winner
				if prev_move != predicted_name:
					if predicted_name != "None":
						pc_selected_name = choice(['Rock', 'Paper', 'Scissors'])
						self.winner = self.find_winner(predicted_name, pc_selected_name)
						if self.winner == 'Computer Win':
							self.groupBox.setStyleSheet("background-color: rgb(255, 255, 255);")
							self.groupBox_2.setStyleSheet("background-color: rgb(0, 255, 127);")
						elif self.winner == 'User Win':
							self.groupBox_2.setStyleSheet("background-color: rgb(255, 255, 255);")
							self.groupBox.setStyleSheet("background-color: rgb(0, 255, 127);")
						else:
							self.groupBox_2.setStyleSheet("background-color: rgb(0, 255, 127);")
							self.groupBox.setStyleSheet("background-color: rgb(0, 255, 127);")

					else:
						pc_selected_name = "None"
						self.winner = "Waiting..."
				prev_move = predicted_name
				self.label_3.setText("STATUS: {}".format(self.winner).upper())
				
				if pc_selected_name =='Rock':
					self.DETECTED_IMAGE = self.ROCK_IMAGE
				elif pc_selected_name =='Paper':
					self.DETECTED_IMAGE = self.PAPER_IMAGE
				elif pc_selected_name =='Scissors':
					self.DETECTED_IMAGE = self.SCISSORS_IMAGE
				else:
					self.DETECTED_IMAGE = self.NONE_IMAGE
								

			self.update()
			key = cv2.waitKey(1) & 0xFF
			if self.started==False:
				break
				
	
	def setPhoto(self,image):
		self.tmp = image
		self.tmp = cv2.rectangle(self.tmp, (80, 80), (310, 310), (0, 20, 200), 2)

		image = imutils.resize(image,height=480)
		frame = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
		image = QImage(frame, frame.shape[1],frame.shape[0],frame.strides[0],QImage.Format.Format_RGB888)
		self.label.setPixmap(QtGui.QPixmap.fromImage(image))

		frame = cv2.cvtColor(self.DETECTED_IMAGE, cv2.COLOR_BGR2RGB)
		image = QImage(frame, frame.shape[1],frame.shape[0],frame.strides[0],QImage.Format.Format_RGB888)
		self.label_2.setPixmap(QtGui.QPixmap.fromImage(image))
	
	
	def update(self):
		img = self.image
		self.setPhoto(img)			

	def retranslateUi(self, MainWindow):
		_translate = QtCore.QCoreApplication.translate
		MainWindow.setWindowTitle(_translate("MainWindow", "RPS Game"))
		self.label_4.setText(_translate("MainWindow", "ROCK PAPER SCISSORS"))
		self.groupBox.setTitle(_translate("MainWindow", "User"))
		self.label.setText(_translate("MainWindow", "User Video"))
		self.groupBox_2.setTitle(_translate("MainWindow", "Computer"))
		self.label_2.setText(_translate("MainWindow", "Computer Video"))
		self.label_3.setText(_translate("MainWindow", "Load Model ..."))

		self.pushButton.setText(_translate("MainWindow", "Back"))
	
		self.pushButton_3.setText(_translate("MainWindow", "Load Model"))
		self.radioButton.setText(_translate("MainWindow", "Video input"))
		self.radioButton_2.setText(_translate("MainWindow", "Camera input"))
		self.pushButton_4.setText(_translate("MainWindow", "Start"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
