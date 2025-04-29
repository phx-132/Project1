class Television:
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self) -> None:
        """
        Method to create Television object
        """
        self.__status = False
        self.__muted = False
        self.__volume = Television.MIN_VOLUME
        self.__channel = Television.MIN_CHANNEL

    def power(self) -> None:
        """
        Method to power Television on and off
        """
        if self.__status:
            self.__status = False
        else:
            self.__status = True
    
    def mute(self) -> None:
        '''
        Method to mute/unmute the Television
        '''
        if self.__status:
            if self.__muted:
                self.__muted = False
            else:
                self.__muted = True

    def channel_up(self) -> None:
        """
        Method to go up by one channel
        """
        if self.__status:
            if self.__channel == Television.MAX_CHANNEL:
                self.__channel = Television.MIN_CHANNEL
            else:
                self.__channel += 1

    def channel_down(self) -> None:
        '''
        Method to go down by one channel
        '''
        if self.__status:
            if self.__channel == Television.MIN_CHANNEL:
                self.__channel = Television.MAX_CHANNEL
            else:
                self.__channel -= 1
    
    def volume_up(self) -> None:
        '''
        Method to raise the volume by one level
        '''
        if self.__status:
            if self.__muted:
                self.__muted = False
            if self.__volume < Television.MAX_VOLUME:
                self.__volume += 1
    
    def volume_down(self) -> None:
        '''
        Method to decrease the volume by one level
        '''
        if self.__status:
            if self.__muted:
                self.__muted = False
            if self.__volume > Television.MIN_VOLUME:
                self.__volume -= 1
    
    def __str__(self) -> str:
        '''
        Method to show Television status, channel, and volume
        :return: Power = [status], Channel = [channel], Volume = [volume]
        '''
        if self.__muted:
            return f'Power = {self.__status}, Channel = {self.__channel}, Volume = 0'
        else:
            return f'Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}'