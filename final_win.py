from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel
from instr import *

class FinalWin(QWidget):
    def __init__ (self, exp):
        super().__init__()
        self.initUI()
        self.set_appear()
        self.show()
        self.exp = exp
    
    def initUI(self):
        self.work_text = QLabel(txt_workheart + self.results())
        self.index_text = QLabel(txt_index + str(self.index))
        self.workh_text = QLabel(txt_workheart)
        self.index_text = QLabel(txt_index)
        self.layout_line = QVBoxLayout()
        self.layout_line.addWidget(self.index_text, alignment = Qt.AlignCenter)
        self.layout_line.addWidget(self.workh_text, alignment = Qt.AlignCenter)
        self.setLayout(self.layout_line)
    def set_appear(self):
        self.setWindowTitle(txt_finalwin)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)

    def results(self):
        if self.exp.age < 7:
            return "немає даних для такого віку"
        self.index = (4 * (int(self.exp.t1)) + (int(self.exp.t2)) + (int(self.exp.tt3)) - 200) / 10
        #7-8
        if self.exp.age == 7 or self.exp.age == 8:
            if self.index >= 21:
                return txt_res1
            elif self.index < 21 or self.index >= 17:
                return txt_res2
            elif self.index < 17 or self.index >= 12:
                return txt_res3
            elif self.index < 12 or self.index >= 6.5:
                return txt_res4
            else:
                return txt_res5
            #9-10
        if self.exp.age == 9 or self.exp.age == 10:
            if self.index >= 19.5:
                return txt_res1
            elif self.index < 19.5 or self.index >= 15.5:
                return txt_res2
            elif self.index < 15.5 or self.index >= 10.5:
                return txt_res3
            elif self.index < 10.5 or self.index >= 5:
                return txt_res4
            else:
                return txt_res5
            #11-12
        if self.exp.age == 11 or self.exp.age == 12:
            if self.index >= 18:
                return txt_res1
            elif self.index < 18 or self.index >= 14:
                return txt_res2
            elif self.index < 9 or self.index >= 14:
                return txt_res3
            elif self.index < 9 or self.index >= 3.5:
                return txt_res4
            else:
                return txt_res5
        #13-14
        if self.exp.age == 13 or self.exp.age == 14:
            if self.index >= 16.5:
                return txt_res1
            elif self.index < 16.5 or self.index >= 12.5:
                return txt_res2
            elif self.index < 12.5 or self.index >= 7.5:
                return txt_res3
            elif self.index < 7.5 or self.index >= 2:
                return txt_res4
            else:
                return txt_res5
        #15+
        if self.exp.age >= 15:
            if self.index >= 15:
                return txt_res1
            elif self.index < 15 or self.index >= 11:
                return txt_res2
            elif self.index < 10 or self.index >= 6:
                return txt_res3
            elif self.index < 6 or self.index >= 0.5:
                return txt_res4
            else:
                return txt_res5