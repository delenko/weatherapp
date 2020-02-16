import sys
import random
import requests
from PySide2 import QtCore, QtWidgets,QtGui

class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.textfield = QtWidgets.QLineEdit("")
        self.button = QtWidgets.QPushButton("Enter")
        self.text = QtWidgets.QLabel("Boo")
        self.layout = QtWidgets.QVBoxLayout()
        self.text.setAlignment(QtCore.Qt.AlignCenter)
        self.layout.addWidget(self.textfield)
        self.layout.addWidget(self.text)
        self.layout.addWidget(self.button)
        self.setLayout(self.layout)
        self.button.clicked.connect(self.weather())

    def weather(self):
        params = {
            'access_key':'d7ed3db83b545d1235bdd8008de97b13',
            'query': '',
            'unit':'f'
        }
        params['query'] = self.textfield.text()
        api_result = requests.get('http://api.weatherstack.com/current', params)
        response = api_result.json()
        print(response)
        #temperature = response['current']['temperature']
        #self.textfield.setText(u"Current temperature of zip code is %d" % (response['list']['3']['current']['temperature']))


if __name__ =="__main__":
    app = QtWidgets.QApplication([])

    widget = MyWidget()
    widget.resize(800,600)
    widget.show()

    sys.exit(app.exec_())