

def buildgeneralsection():

    with open('data.vatsim.txt', 'r') as f:
        subsection = f.read().split('!')
    generalsection = subsection[11].split('\n')
    return generalsection


def returnversion():

    version = buildgeneralsection()[1].strip("VERSION = ")
    return version


def returnreload():
    reload = buildgeneralsection()[2].strip("RELOAD = ")
    return reload


def returnupdate():
    update = buildgeneralsection()[3].strip("UPDATE = ")
    return update


def returnatisallowmin():
    atisallowmin = buildgeneralsection()[4].strip("ATIS ALLOW MIN = ")
    return atisallowmin


def returnconnectedclients():
    connectedclients = buildgeneralsection()[5].strip("CONNECTED CLIENTS = ")
    return connectedclients
