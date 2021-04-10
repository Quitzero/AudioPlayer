from PyQt5 import uic, QtCore, QtGui
from PyQt5.QtWidgets import QApplication, QFileDialog, QMessageBox
import os
import pygame


def Play():
    global b
    try:
        music_file = form.listWidget.currentItem().text()
        pygame.mixer.music.load(f"Sound\\{music_file}")
        pygame.mixer.music.play()
        form.label_2.setText(f'{music_file}')
        b = False
    except:
        print("Error!")


def Stop():
    try:
        pygame.mixer.music.stop()
    except:
        print("Error!")


def Pause():
    global b
    try:
        if b:
            pygame.mixer.music.unpause()
            b = False
        else:
            pygame.mixer.music.pause()
            b = True
    except:
        print("Error!")


def showDialog():
    QFileDialog.getOpenFileName(None, 'Open File', 'Sound', "MP3 (*.mp3);;All files (*.*)")
    list_refresh()


def deleteDialog():
    try:
        music_file = form.listWidget.currentItem().text()
        mbox = QMessageBox()
        mbox.setWindowTitle('Подтверждение')
        mbox.setText(f"Вы действительно хотите удалить {music_file}?")
        mbox.setIcon(QMessageBox.Question)
        mbox.setStandardButtons(QMessageBox.No | QMessageBox.Ok)
        mbox.buttonClicked.connect(deleteSound)
        mbox.exec()
    except:
        print("Error!")


def deleteSound(btn):
    try:
        music_file = form.listWidget.currentItem().text()
        if btn.text() == 'OK':
            os.remove(f'Sound\\{music_file}')
            list_refresh()
        elif btn.text() == 'No':
            list_refresh()
    except:
        e = QMessageBox()
        e.setWindowTitle('Ошибка')
        e.setText(f"Невозможно удалить проигрываемый файл!")
        e.setIcon(QMessageBox.Warning)
        e.setStandardButtons(QMessageBox.Ok)
        e.exec()


def mute():
    global c
    global m
    global mb
    try:
        if not mb:
            m = round(c, 1)
            form.progressBar.setProperty("value", 0)
            pygame.mixer.music.set_volume(0)
            mb = True
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap("Ico\\Mute.png"))
            form.pushButton_6.setIcon(icon)
            form.pushButton_6.setIconSize(QtCore.QSize(21, 24))
        else:
            form.progressBar.setProperty("value", c * 100)
            pygame.mixer.music.set_volume(m)
            mb = False
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap("Ico\\Audio.png"))
            form.pushButton_6.setIcon(icon)
            form.pushButton_6.setIconSize(QtCore.QSize(30, 30))
    except:
        print("Error!")


def volume_up():
    global c
    try:
        c += 0.1
        pygame.mixer.music.set_volume(round(c, 1))
        if c >= 1:
            c = 1.0
        form.progressBar.setProperty("value", c * 100)
    except:
        print("Error!")


def volume_down():
    global c
    try:
        c -= 0.1
        pygame.mixer.music.set_volume(round(c, 1))
        if c <= 0:
            c = 0.0
        form.progressBar.setProperty("value", c * 100)
    except:
        print("Error!")


m = None
c = 0.5
mb = False
b = False
pygame.init()
pygame.mixer.music.set_volume(c)
Form, Window = uic.loadUiType("tracker.ui")
app = QApplication([])
window = Window()
form = Form()
form.setupUi(window)
form.progressBar.setProperty("value", c * 100)


def list_refresh():
    form.listWidget.clear()
    files = os.listdir(path='Sound')
    for i in files:
        if '.mp3' in i:
            form.listWidget.addItem(i)


list_refresh()

form.pushButton.clicked.connect(Play)
form.pushButton_2.clicked.connect(Stop)
form.pushButton_3.clicked.connect(Pause)
form.pushButton_4.clicked.connect(showDialog)
form.pushButton_5.clicked.connect(deleteDialog)
form.pushButton_6.clicked.connect(mute)
form.pushButton_7.clicked.connect(volume_down)
form.pushButton_8.clicked.connect(volume_up)

window.show()
app.exec()

