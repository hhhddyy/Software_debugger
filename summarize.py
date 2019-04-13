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
                bug = int(df.loc[line_no + 1, "Bug"])
                freq = int(df.loc[line_no + 1, "Frequency"])
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
    return [score_distribution, test_sum]

    # dst = [round(a/test_sum, 2) for a in score_distribution]
    # sum = 0
    # result = []
    # for i in range(11):
    #    sum += dst[i] * 100
    #    result.append(sum)
    # return result, ErrorType


def integrate(*args):  # Each argument is a list [score_distribution, test_sum]
    result = [[0] * 11, 0]
    for i in args:
        for j in range(11):
            result[0][j] += i[0][j]
        result[1] += i[1]

    dst = [a/result[1] for a in result[0]]

    output = list()
    sum = 0
    for i in range(11):
        sum += dst[i] * 100
        output.append(sum)
    output = [round(a, 2) for a in output]
    return output


def main():
    tt1 = r"output/output/Tarantula/merge_computation.xlsx"
    tt2 = r"output/output/Tarantula/merge_boundary.xlsx"
    tt3 = r"output/output/Tarantula/merge_process.xlsx"
    tt4 = r"output/output/Tarantula/select_computation.xlsx"
    tt5 = r"output/output/Tarantula/select_boundary.xlsx"
    tt6 = r"output/output/Tarantula/select_process.xlsx"

    ct1 = r"output/output/crosstab/merge_computation.xlsx"
    ct2 = r"output/output/crosstab/merge_boundary.xlsx"
    ct3 = r"output/output/crosstab/merge_process.xlsx"
    ct4 = r"output/output/crosstab/select_computation.xlsx"
    ct5 = r"output/output/crosstab/select_boundary.xlsx"
    ct6 = r"output/output/crosstab/select_process.xlsx"

    mstt = [integrate(read_data(tt1), read_data(tt2), read_data(tt3)), integrate(read_data(tt4), read_data(tt5),
                                                                                 read_data(tt6))]
    msct = [integrate(read_data(ct1), read_data(ct2), read_data(ct3)), integrate(read_data(ct4), read_data(ct5),
                                                                                 read_data(ct6))]
    mtt = [integrate(read_data(tt1)), integrate(read_data(tt2)), integrate(read_data(tt3))]
    stt = [integrate(read_data(tt4)), integrate(read_data(tt5)), integrate(read_data(tt6))]
    mct = [integrate(read_data(ct1)), integrate(read_data(ct2)), integrate(read_data(ct3))]
    sct = [integrate(read_data(ct4)), integrate(read_data(ct5)), integrate(read_data(ct6))]
    mc = [integrate(read_data(tt1)), integrate(read_data(ct1))]
    mb = [integrate(read_data(tt2)), integrate(read_data(ct2))]
    mp = [integrate(read_data(tt3)), integrate(read_data(ct3))]
    sc = [integrate(read_data(tt4)), integrate(read_data(ct4))]
    sb = [integrate(read_data(tt5)), integrate(read_data(ct5))]
    sp = [integrate(read_data(tt6)), integrate(read_data(ct6))]
    mpl.cmp(mstt, num=2, labels=["Merge", "Select"], title="Comparison of Merge and Select (Tarantula)",
            path=r'mstt.png')
    mpl.cmp(msct, num=2, labels=["Merge", "Select"], title="Comparison of Merge and Select (Crosstab)",
            path=r'msct.png')
    mpl.cmp(mtt, num=3, labels=["Computation", "Boundary", "Process"], title="Tarantula on Different Errors (Merge)",
            path=r'mtt.png')
    mpl.cmp(stt, num=3, labels=["Computation", "Boundary", "Process"], title="Tarantula on Different Errors (Select)",
            path=r'stt.png')
    mpl.cmp(mct, num=3, labels=["Computation", "Boundary", "Process"], title="Crosstab on Different Errors (Merge)",
            path=r'mct.png')
    mpl.cmp(sct, num=3, labels=["Computation", "Boundary", "Process"], title="Crosstab on Different Errors (Select)",
            path=r'sct.png')
    mpl.cmp(mc, num=2, labels=["Tarantula", "Crosstab"], title="Debugger Comparison on Computation Errors (Merge)",
            path=r'mc.png')
    mpl.cmp(mb, num=2, labels=["Tarantula", "Crosstab"], title="Debugger Comparison on Boundary Errors (Merge)",
            path=r'mb.png')
    mpl.cmp(mp, num=2, labels=["Tarantula", "Crosstab"], title="Debugger Comparison on Process Errors (Merge)",
            path=r'mp.png')
    mpl.cmp(sc, num=2, labels=["Tarantula", "Crosstab"], title="Debugger Comparison on Computation Errors (Select)",
            path=r'sc.png')
    mpl.cmp(sb, num=2, labels=["Tarantula", "Crosstab"], title="Debugger Comparison on Boundary Errors (Select)",
            path=r'sb.png')
    mpl.cmp(sp, num=2, labels=["Tarantula", "Crosstab"], title="Debugger Comparison on Process Errors (Select)",
            path=r'sp.png')


if __name__ == "__main__":
    main()
