import time
import datetime
from GeneralParser import returnconnectedclients
import ClientsParse
import DataSaver
import requests


def savecsvdata():
        currenttime = datetime.datetime.utcnow().strftime("%Y-%m-%d, %H:%M:%S")
        connectedclients = returnconnectedclients()
        atc = str(len(ClientsParse.returnatc()))
        pilots = str(len(ClientsParse.returnpilots()))
        with open('ClientSaves.txt', 'a') as f:
            f.write('\n' + connectedclients + ', ' + atc + ', ' + pilots + ', ' + currenttime)
        print('File: "' + f.name + '" saved!')


def savelocalvatdata():
        pagecontents = requests.get(DataSaver.returnvalidlink()).text
        localsave = open('data.vatsim.txt', 'w')
        localsave.write(pagecontents)
        localsave.close()
        print("data.vatsim.txt updated at: " + datetime.datetime.now().strftime("%Y-%m-%d|%H:%M:%S"))


if __name__ == "__main__":
    with open('ClientSaves.txt', 'w') as f:
        f.write('Total Connected Clients, ATC, Pilots, Date, Time (UTC)')
    while True:
        savelocalvatdata()
        savecsvdata()
        time.sleep(1800)
