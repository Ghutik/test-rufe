# напиши здесь код основного приложения и первого экрана
from instr import *
from second_win import *
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton,QVBoxLayout
class MainWin(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.initUI()
        self.connects()
        self.show()
    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)
    def initUI(self):
        self.hello_label = QLabel(txt_hello)
        self.instruction_label = QLabel(txt_instruction)
        self.button = QPushButton(txt_name)
        self.vlayout = QVBoxLayout()
        self.vlayout.addWidget(self.hello_label)
        self.vlayout.addWidget(self.instruction_label)
        self.vlayout.addWidget(self.button)
        self.setLayout(self.vlayout)
    def connects(self):
        self.button.clicked.connect(self.next_click)
    def next_click(self):
        self.hide()
        self.test = TestWin()

app = QApplication([])
main_win = MainWin()
app.exec_()
