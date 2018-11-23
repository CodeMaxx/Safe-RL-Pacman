# Total losses, Losses in last 10 episodes, unsafe actions in last 10 episodes, average score, 10 window average score, episodes so far, cumulative time

from matplotlib import pyplot as plt
import matplotlib.ticker as mticker
import sys

def main():
    myLocator = mticker.MultipleLocator(100)
    filepath = sys.argv[1]
    episodes = []
    times = []
    losses = []
    window_losses = []
    window_unsafe = []
    avg_score = []
    window_avg_score = []
    with open(filepath) as f:
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

    # print(losses)
    # print(episodes)
    plt.plot(episodes, losses)
    # plt.axes.set_major_locator(myLocator)
    plt.tight_layout()
    plt.show()
    plt.close()

if __name__ == '__main__':
    main()