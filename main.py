from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QLineEdit
from PyQt5.QtCore import Qt, QTime, QTimer
from PyQt5.QtGui import QFont

app = QApplication([])
window = QWidget()
window.resize(900,600)
window2 = QWidget()
window2.resize(900,600)
window3 = QWidget()
window3.resize(900,600)


def change_1_to_2():
    window2.setLayout(layout2)
    window.hide()
    window2.show()


def change_2_to_3():
    window3.setLayout(screen3)
    window2.hide()
    window3.show()


def timer1_start():
    global times1, timer
    times1 = QTime(0,0,30)
    timer = QTimer()
    timer.timeout.connect(timer1_event)
    timer.start(1000)
    times1.toString('hh:mm:ss')


def timer1_event():
    global times1, timer
    times1 = times1.addSecs(-1)
    times_text = times1.toString('hh:mm:ss')
    if times_text == '00:00:00':
        timer.stop()
    timer_and_counter.setText(times_text)


def timer2_start():
    global times1, timer
    times1 = QTime(0,0,0)
    timer = QTimer()
    timer.timeout.connect(timer2_event)
    timer.start(1500)
    times1.toString('s')


def timer2_event():
    global times1, timer
    times1 = times1.addSecs(1)
    times_text = times1.toString('s')
    if times_text == '30':
        timer.stop()
    timer_and_counter.setText(times_text)


def timer3_start():
    global times1, timer
    times1 = QTime(0,1,0)
    timer = QTimer()
    timer.timeout.connect(timer3_event)
    timer.start(1000)
    times1.toString('hh:mm:ss')


def timer3_event():
    global times1, timer

    times1 = times1.addSecs(-1)
    timers_text = times1.toString('hh:mm:ss')

    if int(times1.toString('hh:mm:ss')[6:8]) <= 15:
        timer_and_counter.setStyleSheet('color: rgb(0,255,0)')
    elif int(times1.toString('hh:mm:ss')[6:8]) >= 45:
        timer_and_counter.setStyleSheet('color: rgb(0,255,0)')
    else:
        timer_and_counter.setStyleSheet('color: rgb(0,0,0)')
    
    if timers_text == '00:00:00':
        timer.stop()

    timer_and_counter.setText(timers_text)


label_introduction = QLabel('Добро пожаловать в программу по определению состояния здоровья!')
label_rules = QLabel('Данное приложение позволит вам с помощью теста Руфье провести перечную диагностику вашего здоровья.\nПроба Руфье представляет собой нагрузочный комплекс, предназначенный для оценки работоспособности сердца при физической нагрузке.\nУ испытуемого, находящегося в положении лежа на спине в течение 5 мин\nУ испытуемого, находящегося в положении лежа на спине в течение 5 мин\nУ испытуемого, находящегося в положении лежа на спине в течение 5 мин определяют частоту пульса за 15 секунд; затем в течение 45 секунд испытуемый выполняет 30 приседаний.\nПосле окончания нагрузки испытуемый ложится, и у него вновь подсчитывается число пульсаций за первый 15 секунд\nа потом - за последние 15 секунд первой минуты периода восстановления\nВажно! Если в процессе проведения испытания вы почувствуете себя плохо (появится головокружение, шум в ушах, сильная одышка и др.), то\nтест необходимо прервать и обратиться к врачу ')
button_start = QPushButton('Начать')
layout1 = QVBoxLayout()
layout2 = QHBoxLayout()
line_main = QVBoxLayout()
line_timer = QVBoxLayout()

label_fio = QLabel('Введите Ф.И.О:')
text_enter_fio = QLineEdit()

label_age = QLabel('Полных лет:')
text_enter_age = QLineEdit()

action_label = QLabel('Лягте на спину и замерьте пульс за 15 секунд. Нажмите кнопку "Начать первый тест", чтобы запустить таймер.\nРезультат запишите в соответствующие поле.')
timer1_start_button = QPushButton('Начать первый тест')
text_enter_result1 = QLineEdit()

action2_label = QLabel('Выполните 30 приседаний за 45 секунд. Для этого нажмите кнопку "Начать делать приседания",\nчтобы запустить счётчик приседаний.')
counter_start_button = QPushButton('Начать делать приседания')

label_last = QLabel('Лягте на спину и замерьте пульс сначала за первые 15 секунд минуты, затем за последние 15 секунд.\nНажмите кнопку "Начать финальный тест", чтобы запустить таймер.\nЗеленым обозначены секунды, в течение которых необходимо\nпроводить измерения, черным - минуты без замера пульсаций. Результаты запишите а соответствующие поля')
final_button = QPushButton('Начать финальный тест')

final_text_enter = QLineEdit()
final1_text_enter = QLineEdit()

timer_and_counter = QLabel('00:00:00')
timer_and_counter.setFont(QFont("Times", 36, QFont.Bold))
line_timer.addWidget(timer_and_counter, alignment=Qt.AlignRight)
button_end = QPushButton('Завершить тест')

line_main.addWidget(label_fio, alignment=Qt.AlignLeft)
line_main.addWidget(text_enter_fio, alignment=Qt.AlignLeft)
line_main.addWidget(label_age, alignment=Qt.AlignLeft)
line_main.addWidget(text_enter_age, alignment=Qt.AlignLeft)
line_main.addWidget(action_label, alignment=Qt.AlignLeft)
line_main.addWidget(timer1_start_button, alignment=Qt.AlignLeft)
line_main.addWidget(timer1_start_button, alignment=Qt.AlignLeft)
line_main.addWidget(text_enter_result1, alignment=Qt.AlignLeft)
line_main.addWidget(action2_label, alignment=Qt.AlignLeft)
line_main.addWidget(counter_start_button, alignment=Qt.AlignLeft)
line_main.addWidget(label_last, alignment=Qt.AlignLeft)
line_main.addWidget(final_button, alignment=Qt.AlignLeft)
line_main.addWidget(final_text_enter, alignment=Qt.AlignLeft)
line_main.addWidget(final1_text_enter, alignment=Qt.AlignLeft)
line_main.addWidget(button_end,alignment=Qt.AlignCenter)

layout1.addWidget(label_introduction, alignment=Qt.AlignLeft)
layout1.addWidget(label_rules, alignment=Qt.AlignLeft)
layout1.addWidget(button_start, alignment=Qt.AlignCenter)

layout2.addLayout(line_main)
layout2.addLayout(line_timer)
window.setLayout(layout1)
button_start.pressed.connect(change_1_to_2)
button_end.pressed.connect(change_2_to_3)
timer1_start_button.pressed.connect(timer1_start)
counter_start_button.pressed.connect(timer2_start)
final_button.pressed.connect(timer3_start)


screen3 = QVBoxLayout()
result_number = ((90+88+77) - 200)/10
result_word_number = QLabel(f"Индекс Руфье: {result_number}")

result_word_word = 0
if result_number <= 3:
    result_word_word = 'Хорошая'
elif 3 <= result_number <= 6:
    result_word_word = 'Средняя'
elif 7 <= result_number <= 9:
    result_word_word = 'Удовлетворительная'
elif 10 <= result_number <= 14:
    result_word_word = 'Плохая'
elif result_number >= 15:
    result_word_word = 'Очень плохая'

result_word = QLabel(f"Работоспоссобность сердца: {result_word_word}")

screen3.addWidget(result_word_number, alignment=Qt.AlignCenter)
screen3.addWidget(result_word, alignment=Qt.AlignCenter)

window.show()
app.exec_()
window.show()
app.exec_()
