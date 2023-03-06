from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import *

import functions
import subprocess, sys


class Window(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()

    # открытие приложения по контролю FAN
    def open_Fan_Control(self):
        subprocess.Popen('FanControl\\FanControler\\FanControl.exe')

    def initUI(self):
        self.setWindowTitle('Мониторинг')
        self.setGeometry(0, 0, 1280, 720)

        self.label = QLabel(self)
        self.pixmap = QPixmap('images\\bg.jpg')
        self.label.setPixmap(self.pixmap)
        self.label.resize(self.pixmap.width(),
                          self.pixmap.height())

        self.update_button = QPushButton('Обновить информацию', self)
        self.update_button.setGeometry(40, 570, 533, 100)
        self.update_button.setFont(QFont('Times', 30))
        self.update_button.setStyleSheet('QPushButton {background-color: #191970; color: #4169E1;}')
        self.update_button.clicked.connect(self.update_data)

        self.open_Fan_Control_button = QPushButton('Открыть FAN Control', self)
        self.open_Fan_Control_button.setGeometry(706, 570, 533, 100)
        self.open_Fan_Control_button.setFont(QFont('Times', 30))
        self.open_Fan_Control_button.setStyleSheet('QPushButton {background-color: #191970; color: #4169E1;}')
        self.open_Fan_Control_button.clicked.connect(self.open_Fan_Control)

        self.CPU_info_button = QPushButton('Информация о \n процессоре', self)
        self.CPU_info_button.setGeometry(40, 25, 200, 500)
        self.CPU_info_button.setFont(QFont('Times', 15))
        self.CPU_info_button.setStyleSheet('QPushButton {background-color: #191970; color: #4169E1;}')
        self.CPU_info_button.setEnabled(False)

        self.GPU_info_button = QPushButton('Информация о \n видеокарте', self)
        self.GPU_info_button.setGeometry(373, 25, 200, 500)
        self.GPU_info_button.setFont(QFont('Times', 15))
        self.GPU_info_button.setStyleSheet('QPushButton {background-color: #191970; color: #4169E1;}')
        self.GPU_info_button.setEnabled(False)

        self.RAM_info_button = QPushButton('Информация об \n оперативной памяти', self)
        self.RAM_info_button.setGeometry(706, 25, 200, 500)
        self.RAM_info_button.setFont(QFont('Times', 15))
        self.RAM_info_button.setStyleSheet('QPushButton {background-color: #191970; color: #4169E1;}')
        self.RAM_info_button.setEnabled(False)

        self.ROM_info_button = QPushButton('Информация о \n дисках', self)
        self.ROM_info_button.setGeometry(1040, 25, 200, 500)
        self.ROM_info_button.setFont(QFont('Times', 15))
        self.ROM_info_button.setStyleSheet('QPushButton {background-color: #191970; color: #4169E1;}')
        self.ROM_info_button.setEnabled(False)

    def update_data(self):
        self.ROM_info = functions.get_ROM_info()
        self.RAM_info = functions.get_RAM_info()
        self.GPU_info = functions.get_GPU_info()
        self.CPU_info = functions.get_CPU_info()

        self.CPU_info_button.setFont(QFont('Times', 10))
        name = self.CPU_info[0].split()
        first = ' '.join(name[: len(name) // 2])
        second = ' '.join(name[len(name) // 2:])
        text = f'Модель процессора: \n  {first} \n {second} \n ' \
               f'Температура процессора: \n {self.CPU_info[1]} \n' \
               f'Частота процессора: \n {self.CPU_info[2]} \n' \
               f'Загруженность процессора: \n {self.CPU_info[3]} \n' \
               f'Количество ядер: \n {self.CPU_info[4]} \n' \
               f'Количество потоков: \n {self.CPU_info[5]}'
        self.CPU_info_button.setText(text)

        self.GPU_info_button.setFont(QFont('Times', 10))
        name = self.GPU_info[0].split()
        first = ' '.join(name[: len(name) // 2])
        second = ' '.join(name[len(name) // 2:])
        text = f'Модель видеокарты: \n  {first} \n {second} \n ' \
               f'Температура видеокарты: \n {self.GPU_info[1]} \n' \
               f'Загруженность видеокарты: \n {self.GPU_info[2]} \n' \
               f'Количество использованой  \n видеопамяти: \n {self.GPU_info[3]} \n' \
               f'Количество свободной \n видеопамяти: \n {self.GPU_info[4]} \n'
        self.GPU_info_button.setText(text)

        self.RAM_info_button.setFont(QFont('Times', 10))
        text = f'ОЗУ: \n' \
               f'Общий объём ОЗУ \n {self.RAM_info[0]} \n' \
               f'Свободный объём ОЗУ \n {self.RAM_info[1]} \n' \
               f'Используемый объём ОЗУ \n {self.RAM_info[2]}'

        self.RAM_info_button.setText(text)

        self.ROM_info_button.setFont(QFont('Times', 10))
        text = ''
        for i in self.ROM_info:
            text += f'Диск {i} \n' \
                    f'Общий объём \n {self.ROM_info[i][0]} \n' \
                    f'Свободный объём \n {self.ROM_info[i][1]} \n' \
                    f'Используемый объём \n {self.ROM_info[i][2]} \n'

        self.ROM_info_button.setText(text)
