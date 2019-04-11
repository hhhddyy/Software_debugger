import matplotlib.pyplot as plt
import numpy as np


def cmp_debugger(tarantula, crosstab, ErrorType):
    x = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    fig = plt.figure(figsize=(14, 5))

    l1 = plt.plot(x, tarantula, color='blue', label="Tarantula", marker="+")
    l2 = plt.plot(x, crosstab, color='red', label="Crosstab", marker="x")

    plt.title('Debugger Comparison (' + str(ErrorType) + ')')

    plt.xlim((0, 100))
    plt.ylim((0, 105))

    plt.xlabel("SCORE (% of program need not to be examined)")
    plt.ylabel("% of test runs")

    plt.legend(loc='lower right')

    #  x_ticks = np.linspace(0,90,10) # set ticks for X
    #  plt.xticks(x_ticks)
    x_tick = []
    for i in range(11):
        #  x_tick.append(str(i * 10) + r"%-" + str(i * 10 + 10) + "%")  #  This list is to print str like "0%-10%"
        x_tick.append(str(100 - i * 10) + "%")
    plt.xticks([0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100], x_tick)  # set ticks for X
    y_ticks = np.linspace(0, 100, 11)
    plt.yticks(y_ticks)

    for a, b in zip(x, tarantula):
        plt.text(a, b, b, ha='center', va='bottom', color='blue')
    for a, b in zip(x, crosstab):
        plt.text(a, b, b, ha='center', va='bottom', color='red')
    plt.savefig(r'debugger.png')  # after plt.show() is called, a new figure is created
    #  plt.show()


def cmp_error(data, num, debugger): #  data is a list of lists containing the data, num is the number of error types
    #  debugger is the type of debugger (str)
    x = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    fig = plt.figure(figsize=(14, 5))


def main():
    #  The tarantula crosstab here are only for testing. It is irrelevant to the debuggers.
    ErrorType = "ErrorType"
    tarantula = [10, 10, 20, 30, 60, 80, 90, 100, 100, 100, 100]
    crosstab = [10, 20, 30, 35, 45, 70, 85, 95, 100, 100, 100]
    # The variables above should be generated from summarize.py
    cmp_debugger(tarantula, crosstab, ErrorType)


if __name__ == '__main__':
    main()
