import h5py
import os
import numpy as np
import matplotlib.pyplot as plt

cwd = os.getcwd()
channel = 'ch_40'
plt.title(channel)

for filename in os.listdir(cwd + '\\competitionfiles'):
    filepath = cwd + '\\competitionfiles\\' + filename
    f = h5py.File(filepath, 'r')

    chanIDs = f['DYNAMIC DATA']

    startTimeStr = str(chanIDs.attrs['FIRST ACQ TIMESTAMP'])[14:-1]
    splitStartTimeStr = startTimeStr.split(':')
    startTime = int(splitStartTimeStr[0]) * 3600000 + \
                int(splitStartTimeStr[1]) * 60000 + \
                int(splitStartTimeStr[2][0:2]) * 1000 + \
                int(splitStartTimeStr[2][3:])
    timeInterval = 0.12 * 1000

    chan40Data = chanIDs[channel]['MEASURED']

    chan40DataNp = np.array(chan40Data)
    chan40IndicesNp = np.arange(len(chan40Data))
    marker = None

    if np.array_equal(chan40DataNp, np.zeros(len(chan40DataNp))):
        print(filename)

    plt.scatter(chan40IndicesNp, chan40DataNp)
    f.close()

plt.show()