import GeneralParser
import DataSaver
import time
import datetime
import requests
import ClientsParse
from timeit import default_timer


# TODO Make it so the graph only displays the most recent 24 hours of data (or a selected time period)
# TODO Add Points where the time is to the line
# TODO Snap the cursor to the line at those points
# TODO Arrange files into appropriate projects!!!
# TODO Improve connectedclients script to handle errors (internet out, etc)
# TODO Create a list of lists of all lats and longs of pilots
# TODO plot all of the lat longs of pilots on a map with Basemap and matplotlib (Sentdex tutorial)


def main():


    #                   ------GENERAL PARSER TEST-----
    # _______________________________________________________________________
    # while True:
    #     print("Version: " + GeneralParser.returnversion())
    #     print("Connected Clients: " + GeneralParser.returnconnectedclinets())
    #     print("ATIS Allow Min: " + GeneralParser.returnatisallowmin())
    #     print("Reload: " + GeneralParser.returnreload())
    #     print("Update: " + GeneralParser.returnupdate())
    #     print("Time: " + datetime.datetime.now().strftime("%Y%m%d-%H%M%S"))
    #     print("---------------------------------------------------")
    #     time.sleep(120)
    # ______________________________________________________________________
    #                        ----DATASAVER TESTS----
    # ______________________________________________________________________
    #                         --SAVEVATDATA TEST--
    # ______________________________________________________________________
    saveperiod = int(input("Please Enter A Save Period (Sec): "))
    savepath = input("Please Enter A Save Directory: ")
    DataSaver.savevatdata(saveperiod, savepath)
    ______________________________________________________________________
    #                      --SAVELOCALVATDATA TEST--
    # ______________________________________________________________________
    # DataSaver.savelocalvatdata()
    # ______________________________________________________________________
    #                        --SAVEVATSTATUSDATA--
    # ______________________________________________________________________
    # DataSaver.savevatstatusdata()
    # ______________________________________________________________________
    #                       --RETRUNVALIDLINKTEST--
    # ______________________________________________________________________
    # link = DataSaver.returnvalidlink()
    # if str(requests.get(link)) != '<Response [200]>':
    #     print('The link: ' + link + ' is not working properly')
    # else:
    #     print('Everything is working with the link: ' + link)


if __name__ == "__main__":
    main()
