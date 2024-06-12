# напиши здесь код основного приложения и первого экрана
from instr import *
fromsecond_win instr import *
from PyQt5.QWidgets import QApplication, QWidgets, QLabel, QPushButton,QVBoxLayout
class MainWin(QWidjet):
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
    def initUi(self):
        self.hello_label = QLabel(txt_hello)
        self.instruction_label = QLabel(txt_instruction)
        self.button = QPushButton(txt_name)
        self.vlayout = QVBoxLayout()
        self.vlayout.addWidget(self.hello_label)
        self.vlayout.addWidget(self.instruction_label)
        self.vlayout.addWidget(self.button)
        self.set_layout(self.vlayout)
    def connects(self):
        self.button.clicked.connect(self.next_click)
    def next_click(self):
        self.hide()
        self.test = TestWin()

app = QApplication([])
main_win = MainWin()
app.exec_()