import pandas as pd
import matplotlib


def read_data():
    df = pd.read_excel("result.xlsx", header=None)
    count = 0  # Updated to 0 once the line_no has reached a new test case
    line_no = 0
    result_num = 0
    test_sum = 0
    df.columns = ["Statement", "Suspiciousness", "Bug", "Frequency"]
    try:
        while True:
            if df.loc[line_no, "Statement"] == "Statement":
                result_num += 1
                count = 0
                bug = df.loc[line_no+1, "Bug"]
                freq = df.loc[line_no+1, "Frequency"]
                test_sum += freq
                print("Result " + str(result_num) + ":" + " Bug appears at line " + str(bug) + "." + "Frequency is " +
                      str(freq) + ".")
            elif df.loc[line_no, "Statement"] == bug:
                print("The number of statements we need to examine is: " + str(count))
            else:
                count += 1

            line_no += 1

    except KeyError:  # KeyError is for loc, IndexError is for iloc
        print("Reached the end of file.")


def main():
    read_data()


if __name__ == "__main__":
    main()
