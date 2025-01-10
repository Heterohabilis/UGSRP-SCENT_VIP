import subprocess
import os
import matplotlib.pyplot as plt

def plot_from_txt(i, is_300):
    # Read the data from the text file
    if is_300:
        with open('(exp)onDesk_concentration_plot_recog_sets/eth_data_set_on_desk/300cm/'+str(i), 'r') as file:
            data = file.readlines()
    else:
        with open('(exp)onDesk_concentration_plot_recog_sets/eth_data_set_on_desk/90cm/'+str(i), 'r') as file:
            data = file.readlines()

    # Convert the data into a list of values
    data = [float(line.strip()) for line in data]

    # Visualize the data
    plt.figure(figsize=(10, 6))
    plt.plot(data, marker='o')
    plt.ylim(27000, 34000)  # Set the y-axis range

    #Remove axes, grid, and text
    plt.axis('off')
    #plt.show()
    if is_300:
        plt.savefig('(exp)onDesk_concentration_plot_recog_sets/tests/_far'+str(i)+'.png')
    else:
        plt.savefig('(exp)onDesk_concentration_plot_recog_sets/tests/_near'+str(i)+'.png')

def plot_from_arr():
    arr_close = [33239.5251396648, 33094.237430167595, 32924.26536312849, 32885.175977653635, 33072.56703910614,
                 32788.427374301675, 32826.22067039106, 32879.74022346369, 32825.58659217877]
    arr_far = [32852.36312849162, 32538.974860335195, 32754.067039106147, 32529.826815642456, 32628.72067039106,
               32777.49441340782, 32766.22067039106, 32672.625698324024, 32639.08938547486]
    trials = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    # Plotting the data
    plt.plot(trials, arr_far, marker='o', label='475.5 cm')
    plt.plot(trials, arr_close, marker='s', label='90 cm')

    # Adding labels and title
    plt.xlabel('Trials')
    plt.ylabel('Values')
    plt.title('Comparison of Two Conditions')

    # Adding legend
    plt.legend(title='Conditions')

    # Adding x-axis tick labels
    plt.xticks(trials, [f'Trial {i}' for i in trials])

    #for i, value in enumerate(arr_far):
       # plt.annotate(str(value), (trials[i], arr_far[i]), textcoords="offset points", xytext=(0, 10), ha='center')
    #for i, value in enumerate(arr_close):
       # plt.annotate(str(value), (trials[i], arr_close[i]), textcoords="offset points", xytext=(0, 10), ha='center')

    # Display the plot
    plt.show()

def plot_grad():

    # Example data
    distances = ['pass', 90.5, 121.5, 152.5, 213.5, 274.5, 335.5, 396.5]
    data = [33339.24860335195, 32955.332402234635, 32884.622905027936, 32830.76190476191, 32763.832402234635,
            32808.262569832405, 32714.13687150838, 32767.53351955307]
    for i in range(len(data)):
        data[i] = 40000-data[i]


   # data.sort(reverse=True)
   # distances.sort(reverse=True)
    # Create the plot
    plt.plot(distances, data, marker='o')

    # Add labels and title
    plt.xlabel('Distance to the VOC source (cm)')
    plt.ylabel('Concentration')
    plt.title('Concentration vs Distance')

    # Show the plot
    plt.show()


def batch_txt_plot():
    _1st_dir = os.listdir('(exp)onDesk_concentration_plot_recog_sets/eth_data_set_on_desk/')
    for dist in _1st_dir:
        files_and_dirs = os.listdir('(exp)onDesk_concentration_plot_recog_sets/eth_data_set_on_desk/'
                                    +str(dist))
        n = len(files_and_dirs)
        for i in range(n):
            if dist == '90cm':
                plot_from_txt(i+1, False)
            else:
                plot_from_txt(i+1, True)

if __name__ == '__main__':
    plot_grad()