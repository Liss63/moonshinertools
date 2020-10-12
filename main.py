import sys
# Класс QUrl предоставляет удобный интерфейс для работы с Urls
from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QApplication, QWidget
# Класс QQuickView предоставляет возможность отображать QML файлы.
from PyQt5.QtQuick import QQuickView
from PyQt5.QtQml import QQmlApplicationEngine
from PyQt5.QtCore import pyqtSignal, QObject, pyqtProperty


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
        print(value)
        self._total = value
        self.total_changed.emit(value)

    @pyqtProperty(float, notify=voltage_changed)
    def voltage(self):
        return self._voltage

    @voltage.setter
    def voltage(self, value):
        if self._voltage == value:
            return
        print(value)
        self._voltage = value
        self.voltage_changed.emit(value)




if __name__ == '__main__':
    sys.argv += ['--style', 'Fusion']
    app = QApplication(sys.argv)
    foo = Foo()
    engine = QQmlApplicationEngine(parent=app)
    engine.rootContext().setContextProperty("foo", foo)
    engine.load(QUrl('main.qml'))
    sys.exit(app.exec_())
