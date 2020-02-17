import sys
import random
import requests
from PySide2.QtWidgets import QWidget,QVBoxLayout, QPushButton, QLineEdit, QLabel, QGridLayout,QApplication, QGroupBox
from PySide2 import QtCore, QtGui



class MyWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.createLayout()
        vboxes = QVBoxLayout()
        vboxes.addWidget(self.gb)
        self.setLayout(vboxes)

    def createLayout(self):
        self.gb = QGroupBox("Enter your zip code.")
        self.gb.setAlignment(QtCore.Qt.AlignCenter)
        self.vbox = QVBoxLayout()
        self.label = QLabel("Your Zip Code")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        textfield = QLineEdit("")
        textfield.setAlignment(QtCore.Qt.AlignCenter)
        self.vbox.addWidget(textfield)
        self.vbox.addWidget(self.label)
        textfield.textChanged[str].connect(self.weather)
        self.gb.setLayout(self.vbox)

    def weather(self,text):
        params = {
            'access_key':'d7ed3db83b545d1235bdd8008de97b13',
            'query': '',
            'unit':'f'
        }
        params['query'] = text
        params['unit'] = 'f'
        self.label.setText(text)
        print(params) 
        if params['query']!= "":
            api_result = requests.get('http://api.weatherstack.com/current', params)
            response = api_result.json()
            temperature = response['current']['temperature']
            self.label.setText(u"Current temperature of zip code is %d F" % (((response['current']['temperature']*9)/5)+32))
        else:
            return
        
        print(response)
      



app = QApplication(sys.argv)

widget = MyWidget()
widget.resize(400,400)
widget.setWindowIconText("Weather")
widget.setWindowTitle("Weather")
widget.show()
app.exec_()
sys.exit()