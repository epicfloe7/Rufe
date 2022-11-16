from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout
from PyQt5.QtCore import Qt

app = QApplication([])
window = QWidget()
window.resize(900,600)

label_introduction = QLabel('Добро пожаловать в программу по определению состояния здоровья!')
label_rules = QLabel('Данное приложение позволит вам с помощью теста Руфье провести перечную диагностику вашего здоровья.\nПроба Руфье представляет собой нагрузочный комплекс, предназначенный для оценки работоспособности сердца при физической нагрузке.\nУ испытуемого, находящегося в положении лежа на спине в течение 5 мин\nУ испытуемого, находящегося в положении лежа на спине в течение 5 мин\nУ испытуемого, находящегося в положении лежа на спине в течение 5 мин определяют частоту пульса за 15 секунд; затем в течение 45 секунд испытуемый выполняет 30 приседаний.\nПосле окончания нагрузки испытуемый ложится, и у него вновь подсчитывается число пульсаций за первый 15 секунд\nа потом - за последние 15 секунд первой минуты периода восстановления\nВажно! Если в процессе проведения испытания вы почувствуете себя плохо (появится головокружение, шум в ушах, сильная одышка и др.), то\nтест необходимо прервать и обратиться к врачу ')
button_start = QPushButton('Начать')
layout1 = QVBoxLayout()
layout1.addWidget(label_introduction, alignment=Qt.AlignLeft)
layout1.addWidget(label_rules, alignment=Qt.AlignLeft)
layout1.addWidget(button_start, alignment=Qt.AlignCenter)

window.setLayout(layout1)

window.show()
app.exec_()