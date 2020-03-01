import h5py
import numpy as np
import datetime
import matplotlib.pyplot as plt
import os

cwd = os.getcwd()

def formatdate(date):
    list_date = date.split('-')
    return list_date[2] + list_date[0] + list_date[1]


def create_date_object(date):
    return datetime.datetime(int(date[0:4]), int(date[4:6]), int(date[6:8]))

def detect_outlier(data_1):
    list_of_x_values = []
    list_of_y_values = []
    threshold = 2.5
    mean_1 = np.mean(data_1)
    std_1 = np.std(data_1)

    for idx, y in enumerate(np.array(data_1)[1]):
        z_score = (y - mean_1) / std_1
        if np.abs(z_score) > threshold:
            list_of_x_values.append(data_1[0][idx])
            list_of_y_values.append(y)
    return [list_of_x_values, list_of_y_values]


def create_graph():
    start_date = input('Enter the starting date as MM-DD-YYYY:')
    start_date_obj = create_date_object(formatdate(start_date))
    end_date = input('Enter the end date as MM-DD-YYYY:')
    end_date_obj = create_date_object(formatdate(end_date))
    channel = 'ch_' + input('Enter the channel number you would like to view:')

    list_of_files = os.listdir(cwd + '/competitionfiles')
    num_files_with_channel = 0
    for file in list_of_files:
        filepath = os.path.relpath(file)
        if start_date_obj <= create_date_object(filepath[8:16]) <= end_date_obj:
            chan_ids = h5py.File(cwd + '/competitionfiles/' + filepath, 'r')['DYNAMIC DATA']
            if channel in chan_ids.keys():
                outliers = detect_outlier(chan_ids[channel]['MEASURED'])
                plt.plot(outliers)
                plt.title(channel + '|' + str(num_files_with_channel) + '|' + start_date + ' to ' + end_date)
                plt.xlabel("Datapoint #")
                plt.ylabel("Value")
                plt.savefig(
                    './plotDates/' + channel + '_' + str(
                        num_files_with_channel) + '_' + start_date + 'To' + end_date + '.png')
                plt.show()



def get_graph():
    return create_graph()


create_graph()
