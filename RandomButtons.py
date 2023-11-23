import sqlite3
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtMultimedia import *
import sys
import time
import asyncio
from random import randint

# создаём "мозг" приложения
app = QApplication([])
height = randint(200, 800)
weight = randint(200, 800)
# создаём окно приложения
main_win = QWidget()
NAME = randint(0, 10)
names = ['Консоль Разработчика (Умная)', 'Демонстрация Возможностей PyQt5', '2+2=FISH', 'Кто Прочитал Тот Программист',
         'Оконная Концовка!!!!', 'Сегодня 17.05.2022. Честно Говорю!', 'У Меня ПослеЗавтра Экзамен По Английскому 〒▽〒',
         'Группа (Из Одного Человека)', '88888888', 'Лучший Проект',
         'Окно С Кучей (Почти) Бесполезных Кнопок, Которое Меняет Свои Размеры При Каждом Открытии Да, Название Именно Такое.']
main_win.setWindowTitle(names[NAME])
main_win.resize(weight, height)
pal = main_win.palette()
cifri = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9')
bukvi = ('A', 'B', 'C', 'D', 'E', 'F')
actbacklcolor = '#'
inactbacklcolor = '#'
for i in range(6):
    cif_or_buk = randint(1, 2)
    if cif_or_buk == 1:
        cifra = randint(0, 9)
        newsymbcolor = cifri[cifra]
        actbacklcolor += newsymbcolor
    if cif_or_buk == 2:
        bukva = randint(0, 5)
        newsymbcolor = bukvi[bukva]
        actbacklcolor += newsymbcolor
# print(actbacklcolor)
for i in range(6):
    cif_or_buk = randint(1, 2)
    if cif_or_buk == 1:
        cifra = randint(0, 9)
        newsymbcolor = cifri[cifra]
        inactbacklcolor += newsymbcolor
    if cif_or_buk == 2:
        bukva = randint(0, 5)
        newsymbcolor = bukvi[bukva]
        inactbacklcolor += newsymbcolor
# print(inactbacklcolor)
pal.setColor(QPalette.Normal, QPalette.Window, QColor(actbacklcolor))
pal.setColor(QPalette.Inactive, QPalette.Window, QColor(inactbacklcolor))
main_win.setPalette(pal)

# создаём виджеты
buttonIMAGE = QPushButton('IMAGE')
EmptyText = QLabel(' ')
MainText = QLabel('Пожалуйста, Ничего Не Нажимай!')
winner1 = QLabel('?')
winner2 = QLabel('??')
word = QLabel('???')
Phrase = QLabel('? ?? ??? ?? ?')
buttonwinner1 = QPushButton('Сгенерировать', )
buttonwinner2 = QPushButton('Сгенерировать (Но Круче!)')
buttonword = QPushButton('Сгенерировать Слово')
buttonJUST = QPushButton('Кнопка (Не Работает)')
buttonClose = QPushButton('Close')
buttonPhrase = QPushButton('Фраза (Новая)')
msg = QMessageBox()
msg.setWindowTitle("Поздравляю!")
msg.setText("Ты Получил Неработающую Концовку!\n"
            "Да, Я Соврал, Эта Кнопка Работает!")
msg.setIcon(QMessageBox.Warning)
JustWHAT = randint(0, 1)
if JustWHAT == 0:
    buttonJUST.setEnabled(True)
elif JustWHAT == 1:
    buttonJUST.setEnabled(False)
buttonPRESS = QPushButton('Нажми На Меня!', main_win)
buttonPRESSold = QPushButton('Нажми На Меня!')
TimesClickedPRESS = 1
buttonSOUND = QPushButton('????')
buttonSOUND2 = QPushButton('Звуковое Сопровождение')
buttonSTOP = QPushButton('STOP MUSIC')
buttonCOUNT = QPushButton('Нажми 100 Раз!!!')
buttonBACK = QPushButton('Поменять Цвет Фона')
buttonHISTORY = QPushButton('ИСТОРИЯ')
buttonMENUDELETEHISTORY = QPushButton('Очистить')

HOWEVERYTHING = randint(0, 4)
# создаём направляющую линию (лэйаут)
# HOWEVERYTHING = 0
# HOWEVERYTHING = 1
# HOWEVERYTHING = 2
# HOWEVERYTHING = 3
# HOWEVERYTHING = 4
if HOWEVERYTHING == 0:
    v_line = QVBoxLayout()
    v_line.addWidget(buttonClose, stretch=1, alignment=Qt.AlignTop)
    v_line.addWidget(EmptyText, stretch=0, alignment=Qt.AlignTop)
    v_line.addWidget(MainText, stretch=10, alignment=Qt.AlignCenter)
    v_line.addWidget(winner1, stretch=1, alignment=Qt.AlignLeft)
    v_line.addWidget(buttonwinner1, stretch=10, alignment=Qt.AlignLeft)
    v_line.addWidget(winner2, stretch=1, alignment=Qt.AlignRight)
    v_line.addWidget(buttonwinner2, stretch=10, alignment=Qt.AlignRight)
    v_line.addWidget(buttonIMAGE, stretch=10, alignment=Qt.AlignCenter)
    v_line.addWidget(buttonPhrase, stretch=1, alignment=Qt.AlignCenter)
    v_line.addWidget(Phrase, stretch=1, alignment=Qt.AlignCenter)
    v_line.addWidget(buttonPRESSold, stretch=5, alignment=Qt.AlignCenter)
    v_line.addWidget(buttonCOUNT, stretch=25, alignment=Qt.AlignCenter)
    v_line.addWidget(buttonSOUND2, stretch=10, alignment=Qt.AlignRight)
    v_line.addWidget(buttonSTOP, stretch=10, alignment=Qt.AlignRight)
    v_line.addWidget(buttonHISTORY, stretch=10, alignment=Qt.AlignLeft)
    v_line.addWidget(buttonMENUDELETEHISTORY, stretch=10, alignment=Qt.AlignLeft)
    v_line.addWidget(buttonJUST, stretch=100, alignment=Qt.AlignCenter)
    v_line.addWidget(buttonSOUND, stretch=10, alignment=Qt.AlignLeft)
    v_line.addWidget(word, stretch=1, alignment=Qt.AlignCenter)
    v_line.addWidget(buttonword, stretch=1, alignment=Qt.AlignCenter)
    v_line.addWidget(buttonBACK, stretch=1, alignment=Qt.AlignRight)
    buttonPRESS.setGeometry(weight // 2 - 50, height // 2, 100, 30)
    buttonPRESS.hide()
if HOWEVERYTHING == 1:
    v_line = QVBoxLayout()
    v_line.addWidget(buttonHISTORY, stretch=10, alignment=Qt.AlignLeft)
    v_line.addWidget(buttonMENUDELETEHISTORY, stretch=10, alignment=Qt.AlignLeft)
    v_line.addWidget(buttonBACK, stretch=1, alignment=Qt.AlignRight)
    v_line.addWidget(buttonClose, stretch=1, alignment=Qt.AlignTop)
    v_line.addWidget(buttonPRESSold, stretch=25, alignment=Qt.AlignCenter)
    v_line.addWidget(buttonSOUND2, stretch=10, alignment=Qt.AlignRight)
    v_line.addWidget(buttonSTOP, stretch=10, alignment=Qt.AlignRight)
    v_line.addWidget(EmptyText, stretch=0, alignment=Qt.AlignTop)
    v_line.addWidget(MainText, stretch=10, alignment=Qt.AlignCenter)
    v_line.addWidget(buttonPhrase, stretch=1, alignment=Qt.AlignCenter)
    v_line.addWidget(Phrase, stretch=1, alignment=Qt.AlignCenter)
    v_line.addWidget(word, stretch=1, alignment=Qt.AlignCenter)
    v_line.addWidget(buttonword, stretch=1, alignment=Qt.AlignCenter)
    v_line.addWidget(buttonCOUNT, stretch=25, alignment=Qt.AlignCenter)
    v_line.addWidget(winner1, stretch=1, alignment=Qt.AlignLeft)
    v_line.addWidget(buttonwinner1, stretch=10, alignment=Qt.AlignLeft)
    v_line.addWidget(winner2, stretch=1, alignment=Qt.AlignRight)
    v_line.addWidget(buttonwinner2, stretch=10, alignment=Qt.AlignRight)
    v_line.addWidget(buttonIMAGE, stretch=10, alignment=Qt.AlignRight)
    v_line.addWidget(buttonJUST, stretch=100, alignment=Qt.AlignCenter)
    v_line.addWidget(buttonSOUND, stretch=10, alignment=Qt.AlignLeft)
    buttonPRESS.setGeometry(weight // 2 - 50, height // 2, 100, 25)
    buttonPRESS.hide()
if HOWEVERYTHING == 2:
    v_line = QVBoxLayout()
    v_line.addWidget(buttonPRESSold, stretch=25, alignment=Qt.AlignCenter)
    v_line.addWidget(MainText, stretch=10, alignment=Qt.AlignCenter)
    v_line.addWidget(EmptyText, stretch=0, alignment=Qt.AlignTop)
    v_line.addWidget(buttonHISTORY, stretch=10, alignment=Qt.AlignLeft)
    v_line.addWidget(buttonMENUDELETEHISTORY, stretch=10, alignment=Qt.AlignLeft)
    v_line.addWidget(buttonSOUND2, stretch=10, alignment=Qt.AlignRight)
    v_line.addWidget(buttonSTOP, stretch=10, alignment=Qt.AlignRight)
    v_line.addWidget(winner2, stretch=1, alignment=Qt.AlignRight)
    v_line.addWidget(buttonwinner2, stretch=10, alignment=Qt.AlignRight)
    v_line.addWidget(word, stretch=1, alignment=Qt.AlignCenter)
    v_line.addWidget(buttonword, stretch=1, alignment=Qt.AlignCenter)
    v_line.addWidget(buttonPhrase, stretch=1, alignment=Qt.AlignCenter)
    v_line.addWidget(Phrase, stretch=1, alignment=Qt.AlignCenter)
    v_line.addWidget(buttonJUST, stretch=100, alignment=Qt.AlignCenter)
    v_line.addWidget(buttonIMAGE, stretch=10, alignment=Qt.AlignRight)
    v_line.addWidget(buttonSOUND, stretch=10, alignment=Qt.AlignLeft)
    v_line.addWidget(buttonBACK, stretch=1, alignment=Qt.AlignRight)
    v_line.addWidget(buttonCOUNT, stretch=25, alignment=Qt.AlignCenter)
    v_line.addWidget(winner1, stretch=1, alignment=Qt.AlignLeft)
    v_line.addWidget(buttonwinner1, stretch=10, alignment=Qt.AlignLeft)
    v_line.addWidget(buttonClose, stretch=1, alignment=Qt.AlignTop)
    buttonPRESS.setGeometry(weight // 2 - 50, height // 2, 100, 25)
    buttonPRESS.hide()
if HOWEVERYTHING == 3:
    v_line = QVBoxLayout()
    v_line.addWidget(buttonSOUND2, stretch=10, alignment=Qt.AlignRight)
    v_line.addWidget(buttonSTOP, stretch=10, alignment=Qt.AlignRight)
    v_line.addWidget(buttonPhrase, stretch=1, alignment=Qt.AlignCenter)
    v_line.addWidget(Phrase, stretch=1, alignment=Qt.AlignCenter)
    v_line.addWidget(buttonHISTORY, stretch=10, alignment=Qt.AlignLeft)
    v_line.addWidget(buttonMENUDELETEHISTORY, stretch=10, alignment=Qt.AlignLeft)
    v_line.addWidget(EmptyText, stretch=0, alignment=Qt.AlignTop)
    v_line.addWidget(buttonCOUNT, stretch=25, alignment=Qt.AlignCenter)
    v_line.addWidget(buttonBACK, stretch=1, alignment=Qt.AlignRight)
    v_line.addWidget(word, stretch=1, alignment=Qt.AlignCenter)
    v_line.addWidget(buttonword, stretch=1, alignment=Qt.AlignCenter)
    v_line.addWidget(winner1, stretch=1, alignment=Qt.AlignLeft)
    v_line.addWidget(buttonwinner1, stretch=10, alignment=Qt.AlignLeft)
    v_line.addWidget(buttonClose, stretch=1, alignment=Qt.AlignTop)
    v_line.addWidget(buttonPRESSold, stretch=25, alignment=Qt.AlignCenter)
    v_line.addWidget(buttonJUST, stretch=100, alignment=Qt.AlignCenter)
    v_line.addWidget(buttonSOUND, stretch=10, alignment=Qt.AlignLeft)
    v_line.addWidget(winner2, stretch=1, alignment=Qt.AlignRight)
    v_line.addWidget(buttonwinner2, stretch=10, alignment=Qt.AlignRight)
    v_line.addWidget(MainText, stretch=10, alignment=Qt.AlignCenter)
    v_line.addWidget(buttonIMAGE, stretch=10, alignment=Qt.AlignCenter)
    buttonPRESS.setGeometry(weight // 2 - 50, height // 2, 100, 25)
    buttonPRESS.hide()
if HOWEVERYTHING == 4:
    dvig_x = 0
    dvig_y = 0
    v_line = QVBoxLayout()
    v_line.addWidget(buttonIMAGE, stretch=10, alignment=Qt.AlignCenter)
    v_line.addWidget(word, stretch=1, alignment=Qt.AlignCenter)
    v_line.addWidget(buttonword, stretch=1, alignment=Qt.AlignCenter)
    v_line.addWidget(buttonPhrase, stretch=1, alignment=Qt.AlignCenter)
    v_line.addWidget(Phrase, stretch=1, alignment=Qt.AlignCenter)
    v_line.addWidget(buttonCOUNT, stretch=25, alignment=Qt.AlignCenter)
    v_line.addWidget(buttonJUST, stretch=100, alignment=Qt.AlignCenter)
    v_line.addWidget(winner1, stretch=1, alignment=Qt.AlignLeft)
    v_line.addWidget(buttonwinner1, stretch=10, alignment=Qt.AlignLeft)
    v_line.addWidget(buttonSOUND, stretch=10, alignment=Qt.AlignLeft)
    v_line.addWidget(buttonClose, stretch=1, alignment=Qt.AlignTop)
    v_line.addWidget(buttonBACK, stretch=1, alignment=Qt.AlignRight)
    v_line.addWidget(buttonPRESSold, stretch=25, alignment=Qt.AlignCenter)
    v_line.addWidget(MainText, stretch=10, alignment=Qt.AlignCenter)
    v_line.addWidget(EmptyText, stretch=0, alignment=Qt.AlignTop)
    v_line.addWidget(winner2, stretch=1, alignment=Qt.AlignRight)
    v_line.addWidget(buttonwinner2, stretch=10, alignment=Qt.AlignRight)
    v_line.addWidget(buttonSOUND2, stretch=10, alignment=Qt.AlignRight)
    v_line.addWidget(buttonSTOP, stretch=10, alignment=Qt.AlignRight)
    v_line.addWidget(buttonHISTORY, stretch=10, alignment=Qt.AlignLeft)
    v_line.addWidget(buttonMENUDELETEHISTORY, stretch=10, alignment=Qt.AlignLeft)
    buttonPRESS.setGeometry(weight // 2 - 50, height // 2, 100, 25)
    buttonPRESS.hide()

# Создаем подключение к базе данных (файл my_database.db будет создан)
connection = sqlite3.connect('my_database.db')
cursor = connection.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS Results(name TEXT NOT NULL, result TEXT NOT NULL, time TEXT NOT NULL)''')
connection.commit()

# Устанавливам направляющую линию v_line как главную направляющую линию окна
main_win.setLayout(v_line)


def show_winner1():
    number1 = randint(0, 9999)
    # number1 = 999
    if number1 == 9999 or number1 == 999 or number1 == 99 or number1 == 9:
        winner1.setText('Удачливая Концовка!!!!')
    else:
        winner1.setText(str(number1))
    vremya = time.asctime()
    cursor.execute('INSERT INTO Results (name, result, time) VALUES (?, ?, ?)',
                   ('Сгенерированное Число: ', number1, vremya[11:19]))


def show_winner2():
    number2 = randint(0, 99999999999999999)
    # number2 = 0
    if number2 == 0 or number2 == 99999999999999999:
        winner2.setText('Божественная Концовка.... Вау(ಠ_ಠ)')
    else:
        winner2.setText(str(number2))
    vremya = time.asctime()
    cursor.execute('INSERT INTO Results (name, result, time) VALUES (?, ?, ?)',
                   ('Сгенерированное Большое Число: ', number2, vremya[11:19]))


def show_word():
    # letters = ('а','б','в','г','д','е','ё','ж','з','и','й','к','л','м','н','о','п','р','с','т','у','ф','х','ц','ч','ш','щ','ъ','ы','ь','э','ю','я')
    # letters = ('а','мон','му','фу','во','да','не','зик','зо','ро','ри','лё','ме','мё','нэ','пи','ку','лю','ка','ту','па','но','ко','ке','ля','же','лу','по','ле','ду','ги','ба','га')
    glasnie = ('а', 'ё', 'у', 'е', 'ы', 'о', 'э', 'я', 'и', 'ю', 'œ')
    soglasnie = (
    'й', 'ц', 'к', 'н', 'г', 'ш', 'щ', 'з', 'х', 'ф', 'в', 'п', 'р', 'л', 'д', 'ж', 'ч', 'с', 'м', 'т', 'б',)
    kol_vo = randint(2, 6)
    neword = ''
    n = 0
    for i in range(kol_vo):
        lettersoglas = randint(0, 20)
        newlettersoglas = soglasnie[lettersoglas]
        if n == 0:
            newlettersoglas = newlettersoglas.upper()
            n = 1
        neword += newlettersoglas
        letterglas = randint(0, 10)
        newletterglas = glasnie[letterglas]
        neword += newletterglas
    word.setText(neword)
    vremya = time.asctime()
    cursor.execute('INSERT INTO Results (name, result, time) VALUES (?, ?, ?)',
                   ('Сгенерированное Слово: ', neword, vremya[11:19]))


def show_close():
    app.exit()


def show_phraser():
    prilog = (
    'красивый', 'подозрительный', 'мужской', 'ужасный', 'прекрасный', 'пузырьчатый', 'тупой', 'замечательный', 'умный',
    'уродливый', 'ужасный', 'гениальный', 'хитрый', 'ленивый', 'толстый', 'жирный', 'плотный', 'удивлённый',
    'спокойный', 'любимый', 'рыжий', 'бездушный', 'злой', 'добрый', 'прозрачный', 'безумный', 'рандомный')
    sushi = (
    'кот', 'пёс', 'Дмитрий', 'Иван', 'человек', 'стул', 'щавель', 'стол', 'халтурщик', 'филин', 'Вася', 'петух', 'тигр',
    'лев', 'гений', 'Женя', 'мужик', 'Степан', 'призрак', 'дятел', 'батя', 'Егор', 'Марк', 'Андрей', 'программист',
    'Стенли', 'конец')
    glagol = (
    'танцует', 'кричит', 'ничего не делает', 'ходит', 'звонит Бену', 'думает', 'ждёт', 'тупит', 'смеётся', 'фырчит',
    'вопит', 'существует и это факт', 'ленится', 'лежит', 'не существует', 'страдает', 'пьёт чай', 'стоит', 'не моется',
    'топает', 'болеет', 'медленно умирает', 'не любит гостей', 'находится за твоей спиной', 'наблюдает', 'пишет код',
    'получен')
    kol_vo = randint(1, 1)
    newpraser = ''
    n = 0
    for i in range(kol_vo):
        kol_voprilog = randint(1, 3)
        if kol_voprilog == 1:
            howprilog = randint(0, 26)
            newprilog = prilog[howprilog]
            newpraser += newprilog
            newpraser += ' '
        if kol_voprilog == 2:
            howprilog = randint(0, 26)
            newprilog = prilog[howprilog]
            newpraser += newprilog
            newpraser += ' '
            howprilog = randint(0, 26)
            newprilog = prilog[howprilog]
            newpraser += newprilog
            newpraser += ' '
        if kol_voprilog == 3:
            howprilog = randint(0, 26)
            newprilog = prilog[howprilog]
            newpraser += newprilog
            newpraser += ' '
            howprilog = randint(0, 26)
            newprilog = prilog[howprilog]
            newpraser += newprilog
            newpraser += ' '
            howprilog = randint(0, 26)
            newprilog = prilog[howprilog]
            newpraser += 'и '
            newpraser += newprilog
            newpraser += ' '
        kol_vosushi = randint(1, 2)
        if kol_vosushi == 1:
            howsushi = randint(0, 26)
            newsushi = sushi[howsushi]
            newpraser += newsushi
            newpraser += ' '
        elif kol_vosushi == 2:
            glagol = (
            'танцуют', 'орут', 'ничего не делают', 'ходят', 'звонят Бену', 'думают', 'ждут', 'тупят', 'смеются',
            'фырчат', 'вопят', 'существуют и это факт', 'ленятся', 'лежат', 'не существуют', 'страдают', 'пьют чай',
            'стоят', 'не моются', 'топают', 'болеют', 'медленно умирают', 'не любят гостей',
            'находятся за твоей спиной', 'наблюдают', 'пишут код', 'получены')
            howsushi = randint(0, 26)
            newsushi = sushi[howsushi]
            newpraser += newsushi
            if kol_voprilog == 3:
                newpraser += ' а также '
            else:
                newpraser += ' и '
            howprilog = randint(0, 26)
            newprilog = prilog[howprilog]
            newpraser += newprilog
            newpraser += ' '
            howsushi = randint(0, 26)
            newsushi = sushi[howsushi]
            newpraser += newsushi
            newpraser += ' '
        kol_voglagol = randint(1, 2)
        if kol_voglagol == 1:
            howglagol = randint(0, 26)
            newglagol = glagol[howglagol]
            newpraser += newglagol
            newpraser += ' '
        elif kol_voglagol == 2:
            howglagol = randint(0, 26)
            newglagol = glagol[howglagol]
            newpraser += newglagol
            newpraser += ' и '
            howglagol = randint(0, 26)
            newglagol = glagol[howglagol]
            newpraser += newglagol
            newpraser += ' '
    Phrase.setText(newpraser)
    vremya = time.asctime()
    cursor.execute('INSERT INTO Results (name, result, time) VALUES (?, ?, ?)',
                   ('Сгенерированная Фраза: ', newpraser, vremya[11:19]))


def show_just():
    msg.exec_()
    vremya = time.asctime()
    cursor.execute('INSERT INTO Results (name, result, time) VALUES (?, ?, ?)',
                   ('Неработающая Кнопка: ', 'Работает', vremya[11:19]))


def show_image():
    imagemsg = QMessageBox()
    which_im = randint(0, 10)
    kartinki = ['wow.png', 'НЕТ.png', 'лестница.png', 'Бар и бета.png',
                'ОкноСКучей(Почти)БесполезныхКнопок,КотороеМеняетСвоиРазмерыПриКаждомОткрытии.jpg', 'Stwquia.png',
                'Why Is Everyone So Mean To Me.png', 'куб2.png', '88888888ver2.png', 'XP.png', 'TV.png']
    imagemsg.setWindowTitle(kartinki[which_im])
    pixmap = QPixmap(kartinki[which_im])
    imagemsg.setIconPixmap(pixmap)
    imagemsg.exec_()
    vremya = time.asctime()
    cursor.execute('INSERT INTO Results (name, result, time) VALUES (?, ?, ?)',
                   ('Название Картинки: ', kartinki[which_im], vremya[11:19]))


HowPressMany = 0


def show_count():
    global HowPressMany
    if HowPressMany != 100:
        HowPressMany += 1
        buttonCOUNT.setText(str(HowPressMany))
    if HowPressMany == 100:
        buttonCOUNT.setText("Я Смотрю Тебе Совсем\n"
                            "Нечем Заняться (ಠ_ಠ)")
    # print(HowPressMany)
    vremya = time.asctime()
    cursor.execute('INSERT INTO Results (name, result, time) VALUES (?, ?, ?)',
                   ('Счётчик Кнопки Счётчика: ', HowPressMany, vremya[11:19]))


def show_press():
    dvig_x = randint(5, weight-5)
    dvig_y = randint(5, height+10)
    buttonPRESS.move(dvig_x, dvig_y)
    buttonPRESSold.hide()
    buttonPRESS.show()
    vremya = time.asctime()
    cursor.execute('INSERT INTO Results (name, result, time) VALUES (?, ?, ?)', (
    'Положение Кнопки "Нажми На Меня!": ', 'x-' + str(dvig_x) + ' ' + 'y-' + str(dvig_y), vremya[11:19]))


def show_music():
    randmus = randint(0, 11)
    choose_of_sound = ['BruhSound.wav', 'fail1.wav', 'fail2.wav', 'dengi.wav', 'hitsound.wav', 'sms.wav',
                       'teleport.wav', 'timeresumes.wav', 'villager.wav', 'wind.wav', 'kryack.wav', 'kubstol.wav']
    music = choose_of_sound[randmus]
    buttonSOUND.play = QSound(music)
    buttonSOUND.play.play()
    buttonSOUND.setEnabled(False)
    QTimer.singleShot(1000, resetbuttonsound)
    # print('sound')
    vremya = time.asctime()
    cursor.execute('INSERT INTO Results (name, result, time) VALUES (?, ?, ?)',
                   ('Проигрыш Звука: ', choose_of_sound[randmus], vremya[11:19]))


def resetbuttonsound():
    buttonSOUND.setEnabled(True)
    # cursor.execute('INSERT INTO Results (name, result) VALUES (?, ?)', ('Ресет Звука: ', 'RESET1'))


whatmus = 0


# Не Будет Работать ПокаЧто (Очевидно)
def show_music2():
    global whatmus
    choose_of_music = ['goodjob.wav', 'pesnyazagad.wav', 'spacecool.wav', 'lastgoodbye.wav', 'superidol.wav']
    music2 = 'goodjob.wav'
    music2 = choose_of_music[whatmus]
    whatmus += 1
    if whatmus == 5:
        whatmus = 0
    buttonSOUND2.play2 = QSound(music2)
    buttonSOUND2.play2.play()
    buttonSOUND2.setEnabled(False)
    QTimer.singleShot(2000, resetbuttonsound2)
    # print('sound')
    vremya = time.asctime()
    cursor.execute('INSERT INTO Results (name, result, time) VALUES (?, ?, ?)',
                   ('Проигрыш Музыки: ', choose_of_music[whatmus], vremya[11:19]))


def resetbuttonsound2():
    buttonSOUND2.setEnabled(True)
    # cursor.execute('INSERT INTO Results (name, result) VALUES (?, ?)', ('Ресет Музыки: ', 'RESET2'))


def show_stop():
    buttonSOUND2.play2 = QSound('')
    buttonSOUND2.play2.play()
    vremya = time.asctime()
    cursor.execute('INSERT INTO Results (name, result, time) VALUES (?, ?, ?)',
                   ('Остановка Музыки: ', 'STOP', vremya[11:19]))


def show_back():
    pal = main_win.palette()
    cifri = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9')
    bukvi = ('A', 'B', 'C', 'D', 'E', 'F')
    actbacklcolor = '#'
    inactbacklcolor = '#'
    for i in range(6):
        cif_or_buk = randint(1, 2)
        if cif_or_buk == 1:
            cifra = randint(0, 9)
            newsymbcolor = cifri[cifra]
            actbacklcolor += newsymbcolor
        if cif_or_buk == 2:
            bukva = randint(0, 5)
            newsymbcolor = bukvi[bukva]
            actbacklcolor += newsymbcolor
    # print(actbacklcolor)
    for i in range(6):
        cif_or_buk = randint(1, 2)
        if cif_or_buk == 1:
            cifra = randint(0, 9)
            newsymbcolor = cifri[cifra]
            inactbacklcolor += newsymbcolor
        if cif_or_buk == 2:
            bukva = randint(0, 5)
            newsymbcolor = bukvi[bukva]
            inactbacklcolor += newsymbcolor
    # print(inactbacklcolor)
    pal.setColor(QPalette.Normal, QPalette.Window, QColor(actbacklcolor))
    pal.setColor(QPalette.Inactive, QPalette.Window, QColor(inactbacklcolor))
    main_win.setPalette(pal)
    vremya = time.asctime()
    cursor.execute('INSERT INTO Results (name, result, time) VALUES (?, ?, ?)',
                   ('Смена Цвета Фона (Активный\Неактивный): ', actbacklcolor + ' ' + inactbacklcolor, vremya[11:19]))


historia_txt = ''


# def show_history():
# global historia_txt
# history = QMessageBox()
# history.setWindowTitle("История")
# cursor.execute('SELECT * FROM Results')
# results = cursor.fetchall()
# print(results)
# for i in results:
# a, b = i
# print(a, b)
# historia_txt = historia_txt + a + ' ' + b + '\n'
# history.setText(historia_txt)
# cursor.execute('INSERT INTO Results (name, result) VALUES (?, ?)', ('История: ', 'ОТКРЫТА ИСТОРИЯ'))
# history.exec_()



def show_history():
    his_win.hide()
    global historia_txt
    vremya = time.asctime()
    cursor.execute('INSERT INTO Results (name, result, time) VALUES (?, ?, ?)',
                   ('История: ', 'ОТКРЫТА ИСТОРИЯ', vremya[11:19]))
    cursor.execute('SELECT * FROM Results')
    results = cursor.fetchall()
    tablet = QTableWidget(len(results), 3, his_win)
    tablet.setColumnWidth(0, 260)
    tablet.setColumnWidth(1, 550)
    tablet.setColumnWidth(2, 190)
    tablet.setHorizontalHeaderLabels(['Операция', 'Результат', 'Время'])
    tablet.setEditTriggers(QAbstractItemView.NoEditTriggers)
    for i in range(len(results)):
        for k in range(3):
            tablet.setItem(i, k, QTableWidgetItem(results[i][k]))
    tablet.setGeometry(0, 0, 1000, 1000)
    his_win.show()

def delete_history():
    cursor.execute('DELETE FROM Results')
    connection.commit()
    his_win.hide()

# Привязка функции-обработчика
buttonIMAGE.clicked.connect(show_image)
buttonwinner1.clicked.connect(show_winner1)
buttonwinner2.clicked.connect(show_winner2)
buttonword.clicked.connect(show_word)
buttonClose.clicked.connect(show_close)
buttonPhrase.clicked.connect(show_phraser)
buttonJUST.clicked.connect(show_just)
buttonPRESS.clicked.connect(show_press)
buttonPRESSold.clicked.connect(show_press)
buttonSOUND.clicked.connect(show_music)
buttonSOUND2.clicked.connect(show_music2)
buttonSTOP.clicked.connect(show_stop)
buttonCOUNT.clicked.connect(show_count)
buttonBACK.clicked.connect(show_back)
buttonHISTORY.clicked.connect(show_history)
buttonMENUDELETEHISTORY.clicked.connect(delete_history)

his_win = QWidget()
his_win.setWindowTitle("История")
his_win.resize(1000, 800)


# показать окно
main_win.show()
# запуск приложения
app.exec_()

# cursor.execute('SELECT * FROM Results')
# results = cursor.fetchall()
# Выводим результаты
# for res in results:
# print(res)