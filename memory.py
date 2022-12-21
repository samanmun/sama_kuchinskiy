#создай приложение для запоминания информации
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets  import (QApplication,QWidget,QRadioButton,QPushButton,QLabel,QGroupBox,QHBoxLayout,QVBoxLayout,QButtonGroup,)
from random import shuffle
def next_question():
    window.cur_question += 1
    if window.cur_question >= len(question_list):
        window.cur_question = 0
    q = question_list[window.cur_question]
    ask(q)
app =QApplication([])
window = QWidget()

lb_Question = QLabel('В каком году основали Москву')
btn_Ok = QPushButton('Ответить')

layout_line1 = QHBoxLayout()
layout_line2 = QHBoxLayout()
layout_line3 = QHBoxLayout()

AnsGroupBox = QGroupBox('Правильно/Непарвильно')
right_answer = QLabel("В 1975")
v_layout = QVBoxLayout()
v_layout.addWidget(right_answer, alignment=(Qt.AlignHCenter|Qt.AlignVCenter))
AnsGroupBox.setLayout(v_layout)

RadioGroup = QButtonGroup()
RadioGroupBox = QGroupBox("Варианты ответов")
rbtn_1 = QRadioButton('1147')
rbtn_2 =  QRadioButton('2022')
rbtn_3 = QRadioButton('2030')
rbtn_4 = QRadioButton('123')

RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)

layout_ans1 = QHBoxLayout()
layout_ans2 = QVBoxLayout()
layout_ans3 = QVBoxLayout()

layout_ans2.addWidget(rbtn_1)
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3)
layout_ans3.addWidget(rbtn_4)
layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)

RadioGroupBox.setLayout(layout_ans1)

layout_line1.addWidget(lb_Question)

layout_line3.addStretch(1)
layout_line3.addWidget(btn_Ok, stretch=2)
layout_line3.addStretch(1)

RadioGroupBox.hide()
layout_line2.addWidget(RadioGroupBox)
layout_line2.addWidget(AnsGroupBox)

layout_main = QVBoxLayout()
layout_main.addLayout(layout_line1)

layout_main.addStretch(1)
layout_main.addLayout(layout_line2)
layout_main.addStretch(1)

layout_main.addLayout(layout_line3)
window.setLayout(layout_main)

def show_result():
    RadioGroupBox.hide()
    AnsGroupBox.show()
    btn_Ok.setText('Следующий вопрос')

def show_question():
    RadioGroupBox.show()
    AnsGroupBox.hide()
    btn_Ok.setText("Ответить")
    RadioGroup.setExclusive(False)
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGroup.setExclusive(True)
class Question():
    def __init__ (self,question,right, wrong1,wrong2,wrong3):
        self.question = question
        self.right = right
        self.wrong1 = wrong1
        self.wrong2 = wrong2        
        self.wrong3 = wrong3
q = Question("На каком планете мы живем","Марс","Кибертрон","Асгард","Земля")

answers = [rbtn_1,rbtn_2,rbtn_3,rbtn_4]
def ask(q):
    shuffle(answers)
    answers[0].setText(q.right)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    lb_Question.setText(q.question)
    right_answer.setText(q.right)
    show_question()

def show_correct(res):
    right_answer.setText(res)
    show_result()
def check_answer():
    if answers[0].isChecked():
        show_correct('Правильно')
    else:
        if answers[1].isChecked() or answers[2].isChecked() or   answers[3].isChecked():
                show_correct('Неправильно') 
questions_list = []
questions_list.append(Question('Государственный язык Португалий','Английский','Исапнский','Французкий','Узбекский'))
questions_list.append(q)
def click_Ok():
    if btn_Ok.text() == 'Ответить':
        check_answer()
    else:
        next_question()
btn_Ok.clicked.connect(click_Ok)
ask(questions_list[0])
btn_Ok.clicked.connect(check_answer)
window.show()
app.exec_()
