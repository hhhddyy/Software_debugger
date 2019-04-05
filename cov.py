import coverage
from xml.dom import minidom
import os
import pandas as pd
import numpy as np
import test

def getCoverageReport(testcase):
    cov = coverage.Coverage()
    cov.start()

    test.bubbleSort(testcase)

    cov.stop()
    cov.save()
    cov.xml_report()

def getCoverageList():
    doc = minidom.parse('coverage.xml')
    lines = doc.getElementsByTagName('line')
    cov_ls = []
    for line in lines:
        hits=int(line.attributes['hits'].value)
        cov_ls.append(hits)

    os.remove('coverage.xml')
    return cov_ls

def initial_var(mode,length):
    global testcase_num
    testcase_num=10 #每个矩阵有10行
    global file_path
    file_path='text_'+mode+str(length)+'.xls'
    global mod
    mod=mode
    global lens
    lens=length



def getMatrix():
    matrix = [[] for i in range(testcase_num)]
    testfile=pd.read_excel(file_path)
    nrows=testfile.shape[0]
    for begin in range(0,nrows-4980,testcase_num):
        print("processing test",mod," ",lens,'  ',begin)
        testcases=[]

        for offset in range(testcase_num):
            testcases.append((testfile.iloc[begin+offset]).tolist())
        for i in range(testcase_num):
            testcase = testcases[i]
            true_l=[]
            for j in testcase:
                true_l.append(j)
            true_l.sort()
            print("test_case",testcase)
            print("true:",true_l)
            # get coverage report
            getCoverageReport(testcase)

            # read coverage information by reading xml
            row = getCoverageList()

            # get execution result
            r = 0 if testcase == true_l else 1  # success:0; fail:1
            row.append(r)
            matrix[i] = row

        stm_num = len(row) - 1

        # save in csv file
        data = np.array(matrix)
        col = ['s' + str(i + 1) for i in range(stm_num)]
        col.append('r')
        df = pd.DataFrame(data, columns=col)
        if not os.path.exists('result/'+mod+'/'+str(lens)+'/'):
            os.makedirs('result/'+mod+'/'+str(lens)+'/')
        df.to_csv('result/'+mod+'/'+str(lens)+'/info_'+str(int(begin/testcase_num))+'.csv', index=False)

        






def main():
    initial_var('random',5)
    matrix = getMatrix()

if __name__ == "__main__":
    main()
