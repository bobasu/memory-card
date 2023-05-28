#создай приложение для запоминания информации
from random import shuffle
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget, QHBoxLayout, QVBoxLayout, QGroupBox, 
                            QButtonGroup, QRadioButton, QPushButton, QLabel)

class Question():
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

question_list = []
question1 =  Question('Ты что-то употребил, потребил, требил?', 'Я джага', 'Нет', 'Да', 'Что это значит?')
question_list.append(question1)

question2 =  Question('Сколько я получил за дота рэп?', 'Лям рублей получил ***', 'Миллион', '100к', '200к 300к 500к миллион')
question_list.append(question2)

question3 = Question('Shadowraze?', 'Нет, ****, Pavshiy', 'Кто это?', 'Зачем?', 'Что?')
question_list.append(question3)





app = QApplication([])
window = QWidget()



window.setWindowTitle('MemoCard')
window.move(0,0)
window.resize(400, 300)

lb_question1 = QLabel('Самый сложный вопрос в мире!')
RadioGroupBox = QGroupBox('Варианты ответов')

qrbutton1 = QRadioButton('Вариант 1')
qrbutton2 = QRadioButton('Вариант 2')
qrbutton3 = QRadioButton('Вариант 3')
qrbutton4 = QRadioButton('Вариант 4')

layout_ans1 = QHBoxLayout()
layout_ans2 = QVBoxLayout()
layout_ans3 = QVBoxLayout()
layout_ans2.addWidget(qrbutton1)
layout_ans2.addWidget(qrbutton2)
layout_ans3.addWidget(qrbutton3)
layout_ans3.addWidget(qrbutton4)

layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)

RadioGroupBox.setLayout(layout_ans1)

AnsGroupBox = QGroupBox('Результаты теста')
lb_result = QLabel('Прав ты или нет?')
lb_correct = QLabel('Прав!')

layout_res = QVBoxLayout()
layout_res.addWidget(lb_result)
layout_res.addWidget(lb_correct)

AnsGroupBox.setLayout(layout_res)

button_okey = QPushButton('Ответить')

layout_line1 = QHBoxLayout()
layout_line2 = QHBoxLayout()
layout_line3 = QHBoxLayout()
layout_card = QVBoxLayout()

layout_line1.addWidget(lb_question1)
layout_line2.addWidget(RadioGroupBox)
layout_line2.addWidget(AnsGroupBox)
AnsGroupBox.hide()

layout_line3.addWidget(button_okey)

layout_card.addLayout(layout_line1)
layout_card.addLayout(layout_line2)
layout_card.addLayout(layout_line3)

window.setLayout(layout_card)

def show_result():
    RadioGroupBox.hide()
    AnsGroupBox.show()
    button_okey.setText('Следующий вопрос')

def show_question():
    AnsGroupBox.hide()
    RadioGroupBox.show()
    button_okey.setText('Ответить')
    button_group = QButtonGroup()
    button_group.addButton(qrbutton2)
    button_group.addButton(qrbutton2)
    button_group.addButton(qrbutton3)
    button_group.addButton(qrbutton4)

    button_group.setExclusive(False)
    qrbutton1.setChecked(False)
    qrbutton2.setChecked(False)
    qrbutton3.setChecked(False)
    qrbutton4.setChecked(False)
    button_group.setExclusive(True)

answers = [qrbutton1, qrbutton2, qrbutton3, qrbutton4]

def ask_question():
    shuffle(question_list)
    ask =  question_list[0]

    shuffle(answers)
    answers[0].setText(ask.right_answer)
    answers[1].setText(ask.wrong1)
    answers[2].setText(ask.wrong2)
    answers[3].setText(ask.wrong3)

    lb_question1.setText(ask.question)
    lb_correct.setText(ask.right_answer)

    show_question()

ask_question()
    



window.show()
app.exec_()

