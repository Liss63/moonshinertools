import multiprocessing

import time
import random
from threading import Timer
import platform

if platform.machine() == 'armv6l':
    import tempsensors

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
    return


if __name__ == '__main__':
    print("start")
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


