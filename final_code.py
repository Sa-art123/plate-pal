import sys
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QDialog, QApplication, QFileDialog
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QLabel
import cv2
import calo



class MainWindow(QDialog):
    def __init__(self):
        super(MainWindow,self).__init__()
        loadUi("gui.ui",self)
        self.browse.clicked.connect(self.browsefiles)
        self.CALCULATE.clicked.connect(self.bmi)
        self.CALCULATE_2.clicked.connect(self.macalo)
        self.age.setText("age")
        #self.age.editingFinished.connect(self.changeText)
        self.height.setText("height")
       # self.height.editingFinished.connect(self.changeText)
        self.weight.setText("weight")
        #self.weight.editingFinished.connect(self.changeText)
        self.condition.setWordWrap(True)
        self.condition.setText("distance of food image taken should be 25cm to 30 cm apart")
       
        self.show()
       
       
    def macalo(self):
        calorie_data = {
            "apple": 0.52,  # kcal per gram
            "chapati": 3.49,  # kcal per gram
            "chicken_gravy": 1.8,  # kcal per gram
            "fries": 3.12,  # kcal per gram
            "idli": 1.12,  # kcal per gram
            "pizza": 2.66,  # kcal per gram
            "rice": 1.3,  # kcal per gram
            "soda": 0.42,  # kcal per ml
            "tomato": 0.18,  # kcal per gram
            "vada": 3.5,  # kcal per gram
            "banana": 0.89,  # kcal per gram
            "burger": 2.95  # kcal per gram
        }

        def calculate_calories(food, weight_or_volume):
            if food not in calorie_data:
                return "Food item not found. Please enter a valid food name."
           
            calories = (weight_or_volume) * calorie_data[food]  # Convert mg to g (or use ml as is)
            return f"Calories in {weight_or_volume} mg/ml of {food}: {calories:.2f} kcal"

        foname = self.age_2.text()
        print(foname)
        foweight= self.age_3.text()
        print(foweight)
        
        food_item = foname.strip().lower()
        weight_or_volume = float(foweight)

        # Calculate and print the calorie count
        #print(calculate_calories(food_item, weight_or_volume))
        self.condition_5.setWordWrap(True)
        self.condition_5.setText(calculate_calories(food_item, weight_or_volume))
        
    def bmi(self):
        text = self.age.text()
        print(text)
        text1= self.height.text()
        print(text1)
        text2= self.weight.text()
        print(text2)
        height=float(text1)
        weight=float(text2)
        BMI=weight/(height*height)
        print (BMI)
        bm=str(BMI)
        self.result.setText(bm[0:4])
        if BMI<18.5:
            print("under weight")
            self.condition_6.setWordWrap(True)
            self.condition_6.setText("Underweight")
           
        if BMI > 18.5:
            if BMI < 24.9:
                print("normal")
                self.condition_6.setWordWrap(True)
                self.condition_6.setText("Normal")
               
        if BMI > 25:
            if BMI < 29.9:
                print("over weight")
                self.condition_6.setWordWrap(True)
                self.condition_6.setText("Overweight")
               
        if BMI>=30:
            print("obese")
            self.condition_6.setWordWrap(True)
            self.condition_6.setText("Obese")
           
    # def changeText(self):
    #     text = self.age.text()
    #     print(text)
    #     text1= self.height.text()
    #     print(text1)
    #     text2= self.weight.text()
    #     print(text2)

    def browsefiles(self):
        fname=QFileDialog.getOpenFileName(self, 'Open file', 'D:\codefirst.io\PyQt5 tutorials\Browse Files', 'Images (*.png, *.xmp *.jpg)')
        self.filename.setText(fname[0])
       
        
        val=calo.predcalo(fname[0])
        # image = cv2.imread(fname[0])
        
        # cv2.imwrite("img.jpg", annotated_frame)
        self.condition_2.setWordWrap(True)
        self.condition_2.setText("                                     ")
        self.condition_3.setWordWrap(True)
        self.condition_3.setText("                                     ")
        self.condition_4.setWordWrap(True)
        self.condition_4.setText("                                     ")
        
       
        # Display the image in the QLabel
        print(val)
        name=str(val[0])
        self.condition_2.setWordWrap(True)
        self.condition_2.setText(name)
        
        are=str(val[1])
        self.condition_3.setWordWrap(True)
        self.condition_3.setText(are)
        
        cal=str(val[2])
        self.condition_4.setWordWrap(True)
        self.condition_4.setText(cal)
        
        im = r"C:\Users\user1\Desktop\project\code\img.jpg"
        pixmap = QtGui.QPixmap(im)
        self.label.setPixmap(pixmap)
        self.label.setScaledContents(True)

app=QApplication(sys.argv)
mainwindow=MainWindow()
widget=QtWidgets.QStackedWidget()
widget.addWidget(mainwindow)
widget.setFixedWidth(1142)
widget.setFixedHeight(583)
widget.show()
sys.exit(app.exec_())
