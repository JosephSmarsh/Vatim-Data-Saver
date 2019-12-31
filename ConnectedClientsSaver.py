import time
import DataSaver
import threading


def savelocalvatdata():
    # updates data.vatsim.txt every 2 minutes
    while True:
        try:
            DataSaver.savelocalvatdata()
            time.sleep(120.00 - time.time() % 120.00)
        except:
            print('Something went wrong')
            pass


def savelocalvatusdata():
    # updates status.vatsim.txt every 24 hours
    while True:
        try:
            DataSaver.savevatstatusdata()
            time.sleep(86400 - time.time() % 86400)
        except:
            print('Something went wrong')
            pass


def saveclientdata():
    # updates ClientSaves.txt every 30 minutes
    while True:
        try:
            DataSaver.saveclientdata()
            time.sleep(1800.00 - time.time() % 1800.00)
        except:
            print('Something went wrong')
            pass


if __name__ == "__main__":
    t1 = threading.Thread(target=savelocalvatdata)
    t2 = threading.Thread(target=saveclientdata)
    t3 = threading.Thread(target=savelocalvatusdata)

    t1.start()
    t2.start()
    t3.start()
