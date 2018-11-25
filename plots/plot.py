# Total losses, Losses in last 10 episodes, unsafe actions in last 10 episodes, average score, 10 window average score, episodes so far, cumulative time

from matplotlib import pyplot as plt
import matplotlib.ticker as mticker
import sys
import os

def main():
    myLocator = mticker.MultipleLocator(100)
    filepath_shield = sys.argv[1]
    filepath_noshield = sys.argv[2]
    episodes = []
    times = []
    losses = []
    window_losses = []
    window_unsafe = []
    avg_score = []
    window_avg_score = []

    shield_episodes = []
    shield_times = []
    shield_losses = []
    shield_window_losses = []
    shield_window_unsafe = []
    shield_avg_score = []
    shield_window_avg_score = []
    with open(filepath_noshield) as f:
        lines = f.read()
        lines = lines.split("\n")[:-1]
        for line in lines:
            data = line.split()
            # print(data)
            losses.append(data[0])
            window_losses.append(data[1])
            window_unsafe.append(data[2])
            avg_score.append(data[3])
            window_avg_score.append(data[4])
            episodes.append(data[5])
            times.append(int(float(data[6])*1000))

    with open(filepath_shield) as f:
        lines = f.read()
        lines = lines.split("\n")[:-1]
        for line in lines:
            data = line.split()
            shield_losses.append(data[0])
            shield_window_losses.append(data[1])
            shield_window_unsafe.append(data[2])
            shield_avg_score.append(data[3])
            shield_window_avg_score.append(data[4])
            shield_episodes.append(data[5])
            shield_times.append(int(float(data[6])*1000))

    foldername = filepath_shield[5:-4] + "/"
    os.system('mkdir ' + foldername)

    plt.plot(episodes, losses, label='Normal', linewidth=3)
    plt.plot(shield_episodes, shield_losses, label='Shield', linewidth=3)
    plt.xlabel("No. of Episodes")
    plt.ylabel("Total losses")
    name = filepath_shield[5:-4] + "-losses-episodes.png"
    plt.legend(loc='upper left')
    plt.title(filepath_shield[5:-4])
    plt.title(filepath_shield[5:-4])
    plt.savefig(foldername + name, label=name)
    plt.gcf().clear()

    plt.plot(episodes, window_losses, label='Normal', linewidth=3)
    plt.plot(shield_episodes, shield_window_losses, label='Shield', linewidth=3)
    plt.xlabel("No. of Episodes")
    plt.ylabel("Total losses in last 10 episodes")
    name = filepath_shield[5:-4] + "-window-losses-episodes.png"
    plt.legend(loc='upper right')
    plt.title(filepath_shield[5:-4])
    plt.savefig(foldername + name, label=name)
    plt.gcf().clear()

    plt.plot(episodes, window_unsafe, label='Normal', linewidth=3)
    plt.plot(shield_episodes, shield_window_unsafe, label='Shield', linewidth=3)
    plt.xlabel("No. of Episodes")
    plt.ylabel("Total Unsafe Actions in last 10 Episodes")
    name = filepath_shield[5:-4] + "-window-unsafe-episodes.png"
    plt.legend(loc='upper right')
    plt.title(filepath_shield[5:-4])
    plt.savefig(foldername + name, label=name)
    plt.gcf().clear()

    plt.plot(episodes, avg_score, label='Normal', linewidth=3)
    plt.plot(shield_episodes, shield_avg_score, label='Shield', linewidth=3)
    plt.xlabel("No. of Episodes")
    plt.ylabel("Running Average Score")
    name = filepath_shield[5:-4] + "-avg-score-episodes.png"
    plt.legend(loc='lower right')
    plt.title(filepath_shield[5:-4])
    plt.savefig(foldername + name, label=name)
    plt.gcf().clear()

    plt.plot(episodes, window_avg_score, label='Normal', linewidth=3)
    plt.plot(shield_episodes, shield_window_avg_score, label='Shield', linewidth=3)
    plt.xlabel("No. of Episodes")
    plt.ylabel("Average Score in last 10 Episodes")
    name = filepath_shield[5:-4] + "-window-avg-score-episodes.png"
    plt.legend(loc='lower right')
    plt.title(filepath_shield[5:-4])
    plt.savefig(foldername + name, label=name)
    plt.gcf().clear()

    plt.plot(times, avg_score, label='Normal', linewidth=3)
    plt.plot(shield_times, shield_avg_score, label='Shield', linewidth=3)
    plt.xlabel("Time (in ms)")
    plt.ylabel("Running Average Score")
    name = filepath_shield[5:-4] + "-avg-score-times.png"
    plt.legend(loc='lower right')
    plt.title(filepath_shield[5:-4])
    plt.savefig(foldername + name, label=name)
    plt.gcf().clear()

    plt.plot(times, window_avg_score, label='Normal', linewidth=3)
    plt.plot(shield_times, shield_window_avg_score, label='Shield', linewidth=3)
    plt.xlabel("Time (in ms)")
    plt.ylabel("Average Score in last 10 Episodes")
    name = filepath_shield[5:-4] + "-window-avg-score-times.png"
    plt.legend(loc='lower right')
    plt.title(filepath_shield[5:-4])
    plt.savefig(foldername + name, label=name)
    plt.gcf().clear()


if __name__ == '__main__':
    main()