from PyQt5.QtCore import pyqtSignal, QObject, pyqtProperty


class MoonshinerModel(QObject):

    def __init__(self):
        QObject.__init__(self)
        self._temp1 = 0
        self._temp2 = 0
        self._temp3 = 0
        self._temp4 = 0
        self._voltage = 0

    temp1_changed = pyqtSignal(float)
    temp2_changed = pyqtSignal(float)
    temp3_changed = pyqtSignal(float)
    temp4_changed = pyqtSignal(float)
    voltage_changed = pyqtSignal(int)

    # датчики температуры
    @pyqtProperty(float, notify=temp1_changed)
    def temp1(self):
        return self._temp1

    @temp1.setter
    def temp1(self, value):
        if self._temp1 == value:
            return
        self._temp1 = value
        self.temp1_changed.emit(value)

    @pyqtProperty(float, notify=temp2_changed)
    def temp2(self):
        return self._temp2

    @temp2.setter
    def temp2(self, value):
        if self._temp2 == value:
            return
        self._temp2 = value
        self.temp2_changed.emit(value)

    @pyqtProperty(float, notify=temp3_changed)
    def temp3(self):
        return self._temp3

    @temp3.setter
    def temp3(self, value):
        if self._temp3 == value:
            return
        self._temp3 = value
        self.temp3_changed.emit(value)

    @pyqtProperty(float, notify=temp4_changed)
    def temp4(self):
        return self._temp4

    @temp4.setter
    def temp4(self, value):
        if self._temp4 == value:
            return
        self._temp4 = value
        self.temp4_changed.emit(value)

    # текущее напряжение
    @pyqtProperty(int, notify=voltage_changed)
    def voltage(self):
        return self._voltage

    @voltage.setter
    def voltage(self, value):
        if self._voltage == value:
            return
        self._voltage = value
        self.voltage_changed.emit(value)
