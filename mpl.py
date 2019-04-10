import matplotlib.pyplot as plt
import numpy as np


def draw_plots(x, y1, y2, ErrorType):
    fig = plt.figure(figsize=(14,5))
    
    l1 = plt.plot(x,y1,color='blue',label="Tarantula")
    l2 = plt.plot(x,y2,color='red',label="Crosstab")

    plt.title('Debugger Comparison (' + ErrorType + ')')
    
    plt.xlim((-10,100))
    plt.ylim((0,1))
    
    plt.xlabel("SCORE")
    plt.ylabel("Percentage")
    
    plt.legend(loc = 'upper left')
    
    ##x_ticks = np.linspace(0,90,10) # set ticks for X
    ##plt.xticks(x_ticks)
    x_tick = []
    for i in range(10):
        x_tick.append(str(i*10) + r"%-" + str(i*10 + 10) + "%")
    plt.xticks([0,10,20,30,40,50,60,70,80,90], x_tick) # set ticks for X
    y_ticks = np.linspace(0,1,11)
    plt.yticks(y_ticks)

    for a,b in zip(x, y1):
        plt.text(a, b, b, ha='center', va='bottom', color='blue')
    for a,b in zip(x, y2):
        plt.text(a, b, b, ha='center', va='bottom', color='red')
    plt.savefig(r'debugger.png') # after plt.show() is called, a new figure is created
    plt.show()


def main():
    ErrorType = "Unknown ErrorType"
    x = [0,10,20,30,40,50,60,70,80,90]
    y1 = [0.1,0.1,0.5,0.5,0.2,0.9,0.6,0.3,0.4,0.6]
    y2 = [0.5,0.1,0.6,0.2,0.3,0.7,0.8,0.2,0.2,0.9]
    # The variables above should be generated from summarize.py
    draw_plots(x, y1, y2, ErrorType)


if __name__ == '__main__':
    main()
