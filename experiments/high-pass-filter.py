import os
import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import butter, filtfilt


def read_data_from_txt(file_path):
    try:
        with open(file_path, 'r') as file:
            data = [float(line.strip()) for line in file if line.strip().isdigit()]
        return data
    except Exception as e:
        print(f"Error reading file: {e}")
        return []


def high_pass_filter(data, cutoff, fs, order=5):
    nyquist = 0.5 * fs
    normal_cutoff = cutoff / nyquist
    b, a = butter(order, normal_cutoff, btype='high', analog=False)
    filtered_data = filtfilt(b, a, data)
    return filtered_data

def fft(data):
    return np.abs(np.fft.fft(data))


def plot_filtered_data(base_dir, categories, cutoff_frequency, sampling_frequency):
    # Set up large figure with better proportions for rectangular subplots
    num_files_per_category = {}
    data_per_category = {}

    # Gather data from files in each category
    for category in categories:
        dir_path = os.path.join(base_dir, category)
        if not os.path.exists(dir_path):
            print(f"Directory {dir_path} does not exist.")
            continue

        file_list = sorted(os.listdir(dir_path))
        num_files_per_category[category] = len(file_list)
        data_per_category[category] = []

        for file_name in file_list:
            file_path = os.path.join(dir_path, file_name)
            data = read_data_from_txt(file_path)
            if data:
                filtered_data = high_pass_filter(data, cutoff_frequency, sampling_frequency)
                #filtered_data = fft(data)
                data_per_category[category].append((file_name, filtered_data))

    # Set the number of rows and columns to make the subplots more rectangular
    ncols = 5  # Fixed number of columns for a better aspect ratio
    nrows = max((sum(num_files_per_category.values()) + ncols - 1) // ncols, 1)

    # Create the figure
    fig, axes = plt.subplots(nrows=nrows, ncols=ncols, figsize=(20, 12))
    fig.tight_layout(pad=5.0)
    axes = axes.flatten() if isinstance(axes, np.ndarray) else [axes]

    # Plot data
    plot_idx = 0
    for category, files_data in data_per_category.items():
        for file_name, filtered_data in files_data:
            if plot_idx < len(axes):
                ax = axes[plot_idx]
                ax.plot(filtered_data, linestyle='--')
                ax.set_title(f"{category} - {file_name}")
                ax.set_ylim([-800, 800])
                ax.grid()
                plot_idx += 1

    # Hide any unused subplots
    for idx in range(plot_idx, len(axes)):
        fig.delaxes(axes[idx])

    plt.show()


# Configuration
base_directory = "./img"
categories = ["90", "300"]
cutoff_frequency = 0.1
sampling_frequency = 3

# Plot data
plot_filtered_data(base_directory, categories, cutoff_frequency, sampling_frequency)
