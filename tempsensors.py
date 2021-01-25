import os
import threading
import glob
import time
import sys


class NoOneWireError(Exception):
    pass


class NoDS18B20Error(Exception):
    pass


if not os.path.isdir('/sys/bus/w1'):
    raise NoOneWireError('No 1-wire bus')


base_dir = '/sys/bus/w1/devices/'


def read_temp_raw(device_folder):
    device_file = device_folder + '/w1_slave'
    f = open(device_file, 'r')
    lines = f.readlines()
    f.close()
    equals_pos = lines[1].find('t=')
    temp_string = lines[1][equals_pos+2:]
    temp_c = float(temp_string) / 1000.0
    return os.path.basename(device_folder), temp_c


class T(threading.Thread):
    def __init__(self, device_folder):
        threading.Thread.__init__(self)
        self._device_folder = device_folder
        self._T = None

    def run(self):
        self._T = read_temp_raw(self._device_folder)

    @property
    def T(self):
        return self._T


def measure():
    device_folders = glob.glob(base_dir + '28*')
    if len(device_folders) == 0:
        raise NoDS18B20Error('DS18B20 not found on 1-wire bus')

    threads = []

    ds18b20_list = []

    # Создание объектов-потоков для каждого термометра
    for device_folder in device_folders:
        threads.append(T(device_folder))

    # Запуск всех потоков
    for eashT in threads:
        eashT.start()

    # Присоединение потоков к текущему, чтобы ожидать завершение измерения
    for eashT in threads:
        eashT.join()

    # Сбор значений температур термометров
    for eashT in threads:
        ds18b20_list.append(eashT.T)

    # Выдача результатов
    return ds18b20_list, time.time()


def main():
    t = 0
    tmax = 0
    for i in range(1, sys.maxsize):
        time_begin = time.time()
        (DS18B20list, tMeasure) = measure()
        os.system('clear')
        for DS18B20 in DS18B20list:
            print(u"%s\t%3.1f градC" % DS18B20)
        print(u'Время измерения=%ssec' % (tMeasure-time_begin))
        t += (tMeasure-time_begin)
        print(u'Среднее время измерения=%ssec' % (t/i))
        if tmax < (tMeasure - time_begin):
              tmax = tMeasure-time_begin
        print(u'(mt)Максимальная продолжительность измерения=%ssec' % tmax)
        print('')


if __name__ == '__main__':
    main()
