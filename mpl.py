import matplotlib.pyplot as plt
import numpy as np


def cmp(data, labels, num, title, path):
    #  data is a list of lists containing the data, num is the number of error types
    #  debugger is the type of debugger (str)
    colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k']
    x = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    fig = plt.figure(figsize=(14, 5))
    plt.title(title)

    plt.xlabel("SCORE (% of program need not to be examined)")
    plt.ylabel("% of test runs")

    plt.xlim((0, 100))
    plt.ylim((0, 105))

    for i in range(num):
        plt.plot(x, data[i], color=colors[i], label=labels[i], marker="x")
        for a, b in zip(x, data[i]):
            plt.text(a, b, b, ha='center', va='bottom', color=colors[i])

    plt.legend(loc='lower right')

    x_tick = list()
    for i in range(11):
        #  x_tick.append(str(i * 10) + r"%-" + str(i * 10 + 10) + "%")  #  This list is to print str like "0%-10%"
        x_tick.append(str(100 - i * 10) + "%")
    plt.xticks([0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100], x_tick)  # set ticks for X
    y_ticks = np.linspace(0, 100, 11)
    plt.yticks(y_ticks)

    plt.savefig(path)


def main():
    # The tarantula & crosstab here are only for testing. They are irrelevant to the debuggers.
    # ErrorType = "mergeSort"
    # tarantula = [10, 10, 20, 30, 60, 80, 90, 100, 100, 100, 100]
    # crosstab = [10, 20, 30, 35, 45, 70, 85, 95, 100, 100, 100]
    # The variables above should be generated from summarize.py
    # cmp_debugger(tarantula, crosstab, ErrorType)

    # data = list()
    # data.append([10, 15, 26, 37, 48, 70, 88, 100, 100, 100, 100])
    # data.append([30, 45, 57, 68, 80, 96, 100, 100, 100, 100, 100])
    # data.append([25, 44, 70, 90, 100, 100, 100, 100, 100, 100, 100])
    # labels = ["boundary", "process", "computation"]
    # cmp_error(data, labels, num=3, debugger="tarantula")
    pass


if __name__ == '__main__':
    main()
