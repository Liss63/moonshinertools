#!/usr/bin/env python3
import multiprocessing

import time
import random
from threading import Timer
import platform
from moonshinermenu import MoonshineMenuItem

if platform.machine() == 'armv6l':
    import tempsensors
else:
    import fake_rpi
    import sys
    sys.modules['RPi'] = fake_rpi.RPi  # Fake RPi
    sys.modules['RPi.GPIO'] = fake_rpi.RPi.GPIO  # Fake GPIO

import RPi.GPIO as GPIO


# button board mode pin 11,13,15


class RepeatTimer(Timer):
    def run(self):
        while not self.finished.wait(self.interval):
            self.function(*self.args, **self.kwargs)
# usage
# def dummyfn(msg="foo"):
#     print(msg)
#
# timer = RepeatTimer(1, dummyfn)
# timer.start()
# time.sleep(5)
# timer.cancel()


def temp_sensors_process(sensors_dict):
    while True:
        if platform.machine() == 'armv6l':  # rasberrypi zero detect
            (DS18B20list, tMeasure) = tempsensors.measure()
            for sensor in DS18B20list:
                sensors_dict[sensor[0]] = sensor[1]
        else:
            sensors_dict['1'] = 23.4 + random.random()
            sensors_dict['2'] = 27.5 + random.random()
        time.sleep(0.1)


def button_callback(channel):
    print('This is a edge event callback function!')
    print('Edge detected on channel %s' % channel)
    print('This is run in a different thread to your main program')


def button_config():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(11, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)  # green button
    GPIO.setup(13, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)  # red button
    GPIO.setup(15, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)  # white button
    GPIO.add_event_detect(11, GPIO.RISING, callback=button_callback, bouncetime=200)
    GPIO.add_event_detect(13, GPIO.RISING, callback=button_callback, bouncetime=200)
    GPIO.add_event_detect(15, GPIO.RISING, callback=button_callback, bouncetime=200)


def menu_config():
    m = MoonshineMenuItem("Меню")
    m.add_submenu(MoonshineMenuItem("Датчики"))
    m.add_submenu(MoonshineMenuItem("Настройки"))
    return m


if __name__ == '__main__':
    print("start")
    button_config()
    menu = menu_config()
    print(menu)
    manager = multiprocessing.Manager()
    d = manager.dict()
    p = multiprocessing.Process(target=temp_sensors_process, args=(d, ))
    p.start()
    while True:
        try:
            print(d)
            time.sleep(5)
        except KeyboardInterrupt:
            p.terminate()
            break
    p.join()
