import pandas as pd
import mpl


def read_data(path):
    df = pd.read_excel(path, header=None)
    score_distribution = [0] * 11  # The list currently represents the total frequency of testcases whose score is in
    #  index * 10% - (index+1) * 10%
    count = 0  # Updated to 0 once the line_no has reached a new test case
    line_no = 0
    result_num = 0
    test_sum = 0
    df.columns = ["Statement", "Suspiciousness", "Bug", "Frequency", "ErrorType", "LOC"]
    LOC = int(df.loc[1, "LOC"])
    ErrorType = df.loc[1, "ErrorType"]
    try:
        while True:
            if df.loc[line_no, "Statement"] == "Statement":
                result_num += 1
                count = 0
                bug = int(df.loc[line_no+1, "Bug"])
                freq = int(df.loc[line_no+1, "Frequency"])
                test_sum += freq
                print("Result " + str(result_num) + ":" + " Bug appears at line " + str(bug) + "." + " Frequency is " +
                      str(freq) + ".")
            elif df.loc[line_no, "Statement"] == bug:
                print("The number of statements we need to examine is: " + str(count))
                score = float(LOC - count) / float(LOC)
                index = 10 - int(score * 10)
                score_distribution[index] += freq
            else:
                count += 1

            line_no += 1

    except KeyError:  # KeyError is for loc, IndexError is for iloc
        print("All testcases read. The total number of testcases is:", test_sum)
    dst = [round(a/test_sum, 2) for a in score_distribution]
    sum = 0
    result = []
    for i in range(11):
        sum += dst[i] * 100
        result.append(sum)
    return result, ErrorType


def main():
    path = "result.xlsx"
    path2 = "result1.xlsx"
    y1tuple = read_data(path)
    y1 = y1tuple[0]
    errortype1 = y1tuple[1]
    y2 = read_data(path2)[0]
    mpl.cmp_debugger(y1, y2, errortype1)


if __name__ == "__main__":
    main()
