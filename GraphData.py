import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style


style.use('Solarize_Light2')
fig = plt.figure()
ax1 = fig.add_subplot(1, 1, 1)


def animate(i):
    clientpoints = []
    atcpoints = []
    pilotpoints = []
    timepoint = []

    #TODO Change from network location to website
    with open('//Pi/homepi/Desktop/DataSaver/ClientSaves.txt', 'r') as f:
        subsection = f.read().split('\n')

    for i in range(1, len(subsection), 1):
        newsubsection = [subsection[i].split(',')]
        for i in range(0, len(newsubsection), 1):
            clientpoints.append(int(newsubsection[i][0]))
            atcpoints.append(int(newsubsection[i][1]))
            pilotpoints.append(int(newsubsection[i][2]))
            timepoint.append(newsubsection[i][3] + '\n' + newsubsection[i][4])

    ax1.clear()
    ax1.plot(timepoint, clientpoints, marker='o')
    ax1.plot(timepoint, atcpoints, marker='o')
    ax1.plot(timepoint, pilotpoints, marker='o')

    plt.legend(['Clients', 'ATC', 'Pilots'])


if __name__ == "__main__":
    ani = animation.FuncAnimation(fig, animate, interval=60000)
    plt.show()
