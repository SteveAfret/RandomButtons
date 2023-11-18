from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtMultimedia import *
import sys
import time
import asyncio
from random import randint

#создаём "мозг" приложения
app = QApplication([])
height = randint(100, 1000)
weight = randint(100, 1000)
#создаём окно приложения
main_win = QWidget()
NAME = randint (0,10)
if NAME == 0:
    main_win.setWindowTitle('Консоль Разработчика (Умная)')
if NAME == 1:
    main_win.setWindowTitle('Демонстрация Возможностей PyQt5')
if NAME == 2:
    main_win.setWindowTitle('2+2=FISH')
if NAME == 3:
    main_win.setWindowTitle('Кто Прочитал Тот Программист')
if NAME == 4:
    main_win.setWindowTitle('Оконная Концовка!!!!')
if NAME == 5:
    main_win.setWindowTitle('Сегодня 17.05.2022. Честно Говорю!')
if NAME == 6:
    main_win.setWindowTitle('У Меня ПослеЗавтра Экзамен По Английскому 〒▽〒')
if NAME == 7:
    main_win.setWindowTitle('Группа (Из Одного Человека)')
if NAME == 8:
    main_win.setWindowTitle('88888888')
if NAME == 9:
    main_win.setWindowTitle('Лучший Проект')
if NAME == 10:
    main_win.setWindowTitle('Окно С Кучей (Почти) Бесполезных Кнопок, Которое Меняет Свои Размеры При Каждом Открытии Да, Название Именно Такое.')
main_win.resize(weight, height)
pal = main_win.palette()
cifri = ('0','1','2','3','4','5','6','7','8','9')
bukvi = ('A','B','C','D','E','F')
actbacklcolor = '#'
inactbacklcolor = '#'
for i in range (6):
    cif_or_buk = randint(1,2)
    if cif_or_buk == 1:
        cifra = randint(0, 9)
        newsymbcolor = cifri[cifra]
        actbacklcolor += newsymbcolor
    if cif_or_buk == 2:
        bukva = randint(0, 5)
        newsymbcolor = bukvi[bukva]
        actbacklcolor += newsymbcolor
#print(actbacklcolor)
for i in range (6):
    cif_or_buk = randint(1,2)
    if cif_or_buk == 1:
        cifra = randint(0, 9)
        newsymbcolor = cifri[cifra]
        inactbacklcolor += newsymbcolor
    if cif_or_buk == 2:
        bukva = randint(0, 5)
        newsymbcolor = bukvi[bukva]
        inactbacklcolor += newsymbcolor
#print(inactbacklcolor)
pal.setColor(QPalette.Normal, QPalette.Window, QColor(actbacklcolor))
pal.setColor(QPalette.Inactive, QPalette.Window, QColor(inactbacklcolor))
main_win.setPalette(pal)

#создаём виджеты
EmptyText = QLabel(' ')
MainText = QLabel('Пожалуйста, Ничего Не Нажимай!')
winner1 = QLabel('?')
winner2 = QLabel('??')
word = QLabel('???')
Phrase = QLabel('? ?? ??? ?? ?')
buttonwinner1 = QPushButton('Сгенерировать',)
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
JustWHAT = randint(0,4)
if JustWHAT == 0:
    buttonJUST.setEnabled(True)
elif JustWHAT == 1 or JustWHAT == 2 or JustWHAT == 3 or JustWHAT == 4:
    buttonJUST.setEnabled(False)
buttonPRESS = QPushButton('Нажми На Меня!')
TimesClickedPRESS = 1
buttonSOUND = QPushButton('????')
buttonSOUND2 = QPushButton('Звуковое Сопровождение')
buttonSTOP = QPushButton('STOP MUSIC')
buttonCOUNT = QPushButton('Нажми 10 Раз!!!')
buttonBACK = QPushButton('Поменять Цвет Фона')



HOWEVERYTHING = randint(0, 4)
#создаём направляющую линию (лэйаут)
if HOWEVERYTHING == 0:
    v_line = QVBoxLayout()
    v_line.addWidget(buttonClose, stretch=1, alignment = Qt.AlignTop)
    v_line.addWidget(EmptyText, stretch=0, alignment = Qt.AlignTop)
    v_line.addWidget(MainText, stretch=10, alignment = Qt.AlignCenter)
    v_line.addWidget(winner1, stretch=1, alignment = Qt.AlignLeft)
    v_line.addWidget(buttonwinner1, stretch=10, alignment = Qt.AlignLeft)
    v_line.addWidget(winner2, stretch=1, alignment = Qt.AlignRight)
    v_line.addWidget(buttonwinner2, stretch=10, alignment = Qt.AlignRight)
    v_line.addWidget(buttonPhrase, stretch=1, alignment = Qt.AlignCenter)
    v_line.addWidget(Phrase, stretch=1, alignment = Qt.AlignCenter)
    v_line.addWidget(buttonPRESS, stretch=5, alignment = Qt.AlignCenter)
    v_line.addWidget(buttonCOUNT, stretch=25, alignment = Qt.AlignCenter)
    v_line.addWidget(buttonSOUND2, stretch=10, alignment = Qt.AlignRight)
    v_line.addWidget(buttonSTOP, stretch=10, alignment = Qt.AlignRight)
    v_line.addWidget(buttonJUST, stretch=100, alignment = Qt.AlignCenter)
    v_line.addWidget(buttonSOUND, stretch=10, alignment = Qt.AlignLeft)
    v_line.addWidget(word, stretch=1, alignment = Qt.AlignCenter)
    v_line.addWidget(buttonword, stretch=1, alignment = Qt.AlignCenter)
    v_line.addWidget(buttonBACK, stretch=1, alignment = Qt.AlignRight)
if HOWEVERYTHING == 1:
    v_line = QVBoxLayout()
    v_line.addWidget(buttonBACK, stretch=1, alignment = Qt.AlignRight)
    v_line.addWidget(buttonClose, stretch=1, alignment = Qt.AlignTop)
    v_line.addWidget(buttonPRESS, stretch=25, alignment = Qt.AlignCenter)
    v_line.addWidget(buttonSOUND2, stretch=10, alignment = Qt.AlignRight)
    v_line.addWidget(buttonSTOP, stretch=10, alignment = Qt.AlignRight)
    v_line.addWidget(EmptyText, stretch=0, alignment = Qt.AlignTop)
    v_line.addWidget(MainText, stretch=10, alignment = Qt.AlignCenter)
    v_line.addWidget(buttonPhrase, stretch=1, alignment = Qt.AlignCenter)
    v_line.addWidget(Phrase, stretch=1, alignment = Qt.AlignCenter)
    v_line.addWidget(word, stretch=1, alignment = Qt.AlignCenter)
    v_line.addWidget(buttonword, stretch=1, alignment = Qt.AlignCenter)
    v_line.addWidget(buttonCOUNT, stretch=25, alignment = Qt.AlignCenter)
    v_line.addWidget(winner1, stretch=1, alignment = Qt.AlignLeft)
    v_line.addWidget(buttonwinner1, stretch=10, alignment = Qt.AlignLeft)
    v_line.addWidget(winner2, stretch=1, alignment = Qt.AlignRight)
    v_line.addWidget(buttonwinner2, stretch=10, alignment = Qt.AlignRight)
    v_line.addWidget(buttonJUST, stretch=100, alignment = Qt.AlignCenter)
    v_line.addWidget(buttonSOUND, stretch=10, alignment = Qt.AlignLeft)
if HOWEVERYTHING == 2:
    v_line = QVBoxLayout()
    v_line.addWidget(buttonPRESS, stretch=25, alignment = Qt.AlignCenter)
    v_line.addWidget(MainText, stretch=10, alignment = Qt.AlignCenter)
    v_line.addWidget(EmptyText, stretch=0, alignment = Qt.AlignTop)
    v_line.addWidget(buttonSOUND2, stretch=10, alignment = Qt.AlignRight)
    v_line.addWidget(buttonSTOP, stretch=10, alignment = Qt.AlignRight)
    v_line.addWidget(winner2, stretch=1, alignment = Qt.AlignRight)
    v_line.addWidget(buttonwinner2, stretch=10, alignment = Qt.AlignRight)
    v_line.addWidget(word, stretch=1, alignment = Qt.AlignCenter)
    v_line.addWidget(buttonword, stretch=1, alignment = Qt.AlignCenter)
    v_line.addWidget(buttonPhrase, stretch=1, alignment = Qt.AlignCenter)
    v_line.addWidget(Phrase, stretch=1, alignment = Qt.AlignCenter)
    v_line.addWidget(buttonJUST, stretch=100, alignment = Qt.AlignCenter)
    v_line.addWidget(buttonSOUND, stretch=10, alignment = Qt.AlignLeft)
    v_line.addWidget(buttonBACK, stretch=1, alignment = Qt.AlignRight)
    v_line.addWidget(buttonCOUNT, stretch=25, alignment = Qt.AlignCenter)
    v_line.addWidget(winner1, stretch=1, alignment = Qt.AlignLeft)
    v_line.addWidget(buttonwinner1, stretch=10, alignment = Qt.AlignLeft)
    v_line.addWidget(buttonClose, stretch=1, alignment = Qt.AlignTop)
if HOWEVERYTHING == 3:
    v_line = QVBoxLayout()
    v_line.addWidget(buttonSOUND2, stretch=10, alignment = Qt.AlignRight)
    v_line.addWidget(buttonSTOP, stretch=10, alignment = Qt.AlignRight)
    v_line.addWidget(buttonPhrase, stretch=1, alignment = Qt.AlignCenter)
    v_line.addWidget(Phrase, stretch=1, alignment = Qt.AlignCenter)
    v_line.addWidget(EmptyText, stretch=0, alignment = Qt.AlignTop)
    v_line.addWidget(buttonCOUNT, stretch=25, alignment = Qt.AlignCenter)
    v_line.addWidget(buttonBACK, stretch=1, alignment = Qt.AlignRight)
    v_line.addWidget(word, stretch=1, alignment = Qt.AlignCenter)
    v_line.addWidget(buttonword, stretch=1, alignment = Qt.AlignCenter)
    v_line.addWidget(winner1, stretch=1, alignment = Qt.AlignLeft)
    v_line.addWidget(buttonwinner1, stretch=10, alignment = Qt.AlignLeft)
    v_line.addWidget(buttonClose, stretch=1, alignment = Qt.AlignTop)
    v_line.addWidget(buttonPRESS, stretch=25, alignment = Qt.AlignCenter)
    v_line.addWidget(buttonJUST, stretch=100, alignment = Qt.AlignCenter)
    v_line.addWidget(buttonSOUND, stretch=10, alignment = Qt.AlignLeft)
    v_line.addWidget(winner2, stretch=1, alignment = Qt.AlignRight)
    v_line.addWidget(buttonwinner2, stretch=10, alignment = Qt.AlignRight)
    v_line.addWidget(MainText, stretch=10, alignment = Qt.AlignCenter)
if HOWEVERYTHING == 4:
    v_line = QVBoxLayout()
    v_line.addWidget(word, stretch=1, alignment = Qt.AlignCenter)
    v_line.addWidget(buttonword, stretch=1, alignment = Qt.AlignCenter)
    v_line.addWidget(buttonPhrase, stretch=1, alignment = Qt.AlignCenter)
    v_line.addWidget(Phrase, stretch=1, alignment = Qt.AlignCenter)
    v_line.addWidget(buttonCOUNT, stretch=25, alignment = Qt.AlignCenter)
    v_line.addWidget(buttonJUST, stretch=100, alignment = Qt.AlignCenter)
    v_line.addWidget(winner1, stretch=1, alignment = Qt.AlignLeft)
    v_line.addWidget(buttonwinner1, stretch=10, alignment = Qt.AlignLeft)
    v_line.addWidget(buttonSOUND, stretch=10, alignment = Qt.AlignLeft)
    v_line.addWidget(buttonClose, stretch=1, alignment = Qt.AlignTop)
    v_line.addWidget(buttonBACK, stretch=1, alignment = Qt.AlignRight)
    v_line.addWidget(buttonPRESS, stretch=25, alignment = Qt.AlignCenter)
    v_line.addWidget(MainText, stretch=10, alignment = Qt.AlignCenter)
    v_line.addWidget(EmptyText, stretch=0, alignment = Qt.AlignTop)
    v_line.addWidget(winner2, stretch=1, alignment = Qt.AlignRight)
    v_line.addWidget(buttonwinner2, stretch=10, alignment = Qt.AlignRight)
    v_line.addWidget(buttonSOUND2, stretch=10, alignment = Qt.AlignRight)
    v_line.addWidget(buttonSTOP, stretch=10, alignment = Qt.AlignRight)







#Устанавливам направляющую линию v_line как главную направляющую линию окна
main_win.setLayout(v_line)

def show_winner1():
    number1 = randint(0, 9999)
    #number1 = 999
    if number1 == 9999 or number1 == 999 or number1 == 99 or number1 == 9:
        winner1.setText('Удачливая Концовка!!!!')
    else:
        winner1.setText(str(number1))


def show_winner2():
    number2 = randint(0, 9999999999999999999999999)
    #number2 = 0
    if number2 == 0 or number2 == 9999999999999999999999999:
        winner2.setText('Божественная Концовка.... Вау(ಠ_ಠ)')
    else:
        winner2.setText(str(number2))


def show_word():
    #letters = ('а','б','в','г','д','е','ё','ж','з','и','й','к','л','м','н','о','п','р','с','т','у','ф','х','ц','ч','ш','щ','ъ','ы','ь','э','ю','я')
    #letters = ('а','мон','му','фу','во','да','не','зик','зо','ро','ри','лё','ме','мё','нэ','пи','ку','лю','ка','ту','па','но','ко','ке','ля','же','лу','по','ле','ду','ги','ба','га')
    glasnie = ('а','ё','у','е','ы','о','э','я','и','ю','œ')
    soglasnie = ('й','ц','к','н','г','ш','щ','з','х','ф','в','п','р','л','д','ж','ч','с','м','т','б',)
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

def show_Close():
    app.exit()

def show_phraser():
    prilog = ('красивый','подозрительный','мужской','ужасный','прекрасный','пузырьчатый','тупой','замечательный','умный','уродливый','ужасный','гениальный','хитрый','ленивый','толстый','жирный','плотный','удивлённый','спокойный','любимый','рыжий','бездушный','злой','добрый','прозрачный','безумный','рандомный')
    sushi = ('кот','пёс','Дмитрий','Иван','человек','стул','щавель','стол','халтурщик','филин','Вася','петух','тигр','лев','гений','Женя','мужик','Степан','призрак','дятел','батя','Егор','Марк','Андрей','программист','Стенли','конец')
    glagol = ('танцует','кричит','ничего не делает','ходит','звонит Бену','думает','ждёт','тупит','смеётся','фырчит','вопит','существует и это факт','ленится','лежит','не существует','страдает','пьёт чай','стоит','не моется','топает','болеет','медленно умирает','не любит гостей','находится за твоей спиной','наблюдает','пишет код','получен')
    kol_vo = randint(1,1)
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
            glagol = ('танцуют','орут','ничего не делают','ходят','звонят Бену','думают','ждут','тупят','смеются','фырчат','вопят','существуют и это факт','ленятся','лежат','не существуют','страдают','пьют чай','стоят','не моются','топают','болеют','медленно умирают','не любят гостей','находятся за твоей спиной','наблюдают','пишут код','получены')
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

def show_JUST():
    msg.exec_()

HowPressMany = 0

def show_COUNT():
    global HowPressMany
    if HowPressMany != 10:
        HowPressMany += 1
        buttonCOUNT.setText(str(HowPressMany))
    if HowPressMany == 10:
        buttonCOUNT.setText("Я Смотрю Тебе Совсем\n"
                            "Нечем Заняться (ಠ_ಠ)")
    #print(HowPressMany)


def show_PRESS():
    buttonPRESS.move(randint(5,weight), randint(5,height))

#Не Будет Работать ПокаЧто (Очевидно)
def show_MUSIC():
    randmus = randint(0,11)
    if randmus == 0:
        music = 'D:/BruhSound.wav'
    if randmus == 1:
        music = 'D:/fail1.wav'
    if randmus == 2:
        music = 'D:/fail2.wav'
    if randmus == 3:
        music = 'D:/dengi.wav'
    if randmus == 4:
        music = 'D:/hitsound.wav'
    if randmus == 5:
        music = 'D:/sms.wav'
    if randmus == 6:
        music = 'D:/teleport.wav'
    if randmus == 7:
        music = 'D:/timeresumes.wav'
    if randmus == 8:
        music = 'D:/villager.wav'
    if randmus == 9:
        music = 'D:/wind.wav'
    if randmus == 10:
        music = 'D:/kryack.wav'
    if randmus == 11:
        music = 'D:/kubstol.wav'
    buttonSOUND.play = QSound(music)
    buttonSOUND.play.play()
    buttonSOUND.setEnabled(False)
    QTimer.singleShot(1000, resetbuttonsound)
    #print('sound')


def resetbuttonsound():
    buttonSOUND.setEnabled(True)

whatmus = 1

#Не Будет Работать ПокаЧто (Очевидно)
def show_MUSIC2():
    global whatmus
    music2 = 'D:/goodjob.wav'
    if whatmus == 1:
        music2 = 'D:/goodjob.wav'
        whatmus += 1
    elif whatmus == 2:
        music2 = 'D:/pesnyazagad.wav'
        whatmus += 1
    elif whatmus == 3:
        music2 = 'D:/spacecool.wav'
        whatmus += 1
    elif whatmus == 4:
        music2 = 'D:/lastgoodbye.wav'
        whatmus += 1
    elif whatmus == 5:
        music2 = 'D:/superidol.wav'
        whatmus = 1
    buttonSOUND2.play2 = QSound(music2)
    buttonSOUND2.play2.play()
    buttonSOUND2.setEnabled(False)
    QTimer.singleShot(2000, resetbuttonsound2)
    #print('sound')


def resetbuttonsound2():
    buttonSOUND2.setEnabled(True)


def show_STOP():
    buttonSOUND2.play2 = QSound('')
    buttonSOUND2.play2.play()

def show_BACK():
    pal = main_win.palette()
    cifri = ('0','1','2','3','4','5','6','7','8','9')
    bukvi = ('A','B','C','D','E','F')
    actbacklcolor = '#'
    inactbacklcolor = '#'
    for i in range (6):
        cif_or_buk = randint(1,2)
        if cif_or_buk == 1:
            cifra = randint(0, 9)
            newsymbcolor = cifri[cifra]
            actbacklcolor += newsymbcolor
        if cif_or_buk == 2:
            bukva = randint(0, 5)
            newsymbcolor = bukvi[bukva]
            actbacklcolor += newsymbcolor
    #print(actbacklcolor)
    for i in range (6):
        cif_or_buk = randint(1,2)
        if cif_or_buk == 1:
            cifra = randint(0, 9)
            newsymbcolor = cifri[cifra]
            inactbacklcolor += newsymbcolor
        if cif_or_buk == 2:
            bukva = randint(0, 5)
            newsymbcolor = bukvi[bukva]
            inactbacklcolor += newsymbcolor
    #print(inactbacklcolor)
    pal.setColor(QPalette.Normal, QPalette.Window, QColor(actbacklcolor))
    pal.setColor(QPalette.Inactive, QPalette.Window, QColor(inactbacklcolor))
    main_win.setPalette(pal)




#Привязка функции-обработчика
buttonwinner1.clicked.connect(show_winner1)
buttonwinner2.clicked.connect(show_winner2)
buttonword.clicked.connect(show_word)
buttonClose.clicked.connect(show_Close)
buttonPhrase.clicked.connect(show_phraser)
buttonJUST.clicked.connect(show_JUST)
buttonPRESS.clicked.connect(show_PRESS)
buttonSOUND.clicked.connect(show_MUSIC)
buttonSOUND2.clicked.connect(show_MUSIC2)
buttonSTOP.clicked.connect(show_STOP)
buttonCOUNT.clicked.connect(show_COUNT)
buttonBACK.clicked.connect(show_BACK)


#показать окно
main_win.show()
#запуск приложения
app.exec_()