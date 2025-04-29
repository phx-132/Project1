from PyQt6.QtWidgets import *
from gui import *
from television import *


class Logic(QMainWindow, Ui_Remote):
    tv = Television()
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.power_button.clicked.connect(lambda : self.power())
        self.mute_button.clicked.connect(lambda : self.mute())
        self.volume_up.clicked.connect(lambda : self.vol_up())
        self.volume_down.clicked.connect(lambda : self.vol_down())
        self.channel_down.clicked.connect(lambda : self.ch_down())
        self.channel_up.clicked.connect(lambda : self.ch_up())

    def power(self):
        self.tv.power()
        if self.tv.get_status() == False:
            self.power_status.setText('Power: OFF')
        else:
            self.power_status.setText('Power: ON')
    
    def mute(self):
        self.tv.mute()
        if self.tv.get_muted() == False:
            self.volume_status.setText(f'Volume: {self.tv.get_volume()}')
        else:
            self.volume_status.setText('Volume: Muted')
    def vol_up(self):
        self.tv.volume_up()
        self.volume_status.setText(f'Volume: {self.tv.get_volume()}')
    
    def vol_down(self):
        self.tv.volume_down()
        self.volume_status.setText(f'Volume: {self.tv.get_volume()}')
    
    def ch_down(self):
        self.tv.channel_down()
        self.channel_status.setText(f'Channel: {self.tv.get_channel()}')

    def ch_up(self):
        self.tv.channel_up()
        self.channel_status.setText(f'Channel: {self.tv.get_channel()}')

