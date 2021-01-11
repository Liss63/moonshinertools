import sys
from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtQml import QQmlApplicationEngine
from PyQt5.QtCore import pyqtSignal, QObject, pyqtProperty
from MoonshinerCore import MoonshinerModel

# все нахуй снести и переделать UI
class Foo(QObject):

    def __init__(self):
        QObject.__init__(self)

        self._total = "12"
        self._voltage = 0.9

    total_changed = pyqtSignal(str)
    voltage_changed = pyqtSignal(float)

    @pyqtProperty(str, notify=total_changed)
    def total(self):
        return self._total

    @total.setter
    def total(self, value):
        if self._total == value:
            return
        self._total = value
        self.total_changed.emit(value)

    @pyqtProperty(float, notify=voltage_changed)
    def voltage(self):
        return self._voltage

    @voltage.setter
    def voltage(self, value):
        if self._voltage == value:
            return
        self._voltage = value
        self.voltage_changed.emit(value)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    foo = Foo()
    engine = QQmlApplicationEngine()
    model = MoonshinerModel()
    engine.rootContext().setContextProperty("foo", foo)
    engine.rootContext().setContextProperty("mmodel", model)
    engine.load(QUrl('main.qml'))
    sys.exit(app.exec_())
