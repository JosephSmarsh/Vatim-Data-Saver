from GeneralParser import returnconnectedclients


def buildclientssection():
    with open('data.vatsim.txt', 'r') as f:
        subsection = f.read().split('CLIENTS:')
    generalsection = subsection[1].split('\n')
    clientsarray = []
    for i in range(0, int(returnconnectedclients()) + 1, 1):
        clientsarray.append(generalsection[i].split(':'))
    clientsarray.remove(clientsarray[0])
    return clientsarray


def returnpilots():
    connectedclients = int(returnconnectedclients())
    clientsection = buildclientssection()
    pilots = []
    for i in range(0, connectedclients, 1):
        subpilot = 'PILOT'
        if subpilot == clientsection[i][3]:
            pilots.append(clientsection[i])
    return pilots


def returnatc():
    connectedclients = int(returnconnectedclients())
    clientsection = buildclientssection()
    atc = []
    for i in range(0, connectedclients, 1):
        subpilot = 'ATC'
        if subpilot == clientsection[i][3]:
            atc.append(clientsection[i])
    return atc


def searchbycallsign(callsign):
    connectedclients = int(returnconnectedclients())
    clientsection = buildclientssection()
    client = []
    for i in range(0, connectedclients, 1):
        if callsign == clientsection[i][0]:
            client.append(clientsection[i])
            return client[0]


def searchbycid(cid):
    connectedclients = int(returnconnectedclients())
    clientsection = buildclientssection()
    client = []
    for i in range(0, connectedclients, 1):
        if cid == clientsection[i][1]:
            client.append(clientsection[i])
            return client[0]
