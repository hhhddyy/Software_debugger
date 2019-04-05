#!/usr/bin/python
# -*- coding: UTF-8 -*-
import pandas as pd
def Tarantula(resultMatrix_Address):
    df = pd.read_csv(resultMatrix_Address)
    nrows=df.shape[0]
    ncols=df.shape[1]
    print(nrows,ncols)
    nstatement=ncols #the statement in the algorithm
    ntestcase=nrows #the number of the test cases
    result=df.iloc[0:,ncols-1:ncols].values;
    list_matrix=df.values
    suspiciousness=[] #the result list
    totalpassed=0
    totalfailed=0
    for i in range(ntestcase):
        if result[i][0]==0:
            totalfailed=totalfailed+1
        else:
            totalpassed=totalpassed+1


    for i in range(nstatement):
        passed=0
        failed=0
        for j in range(ntestcase):
            if list_matrix[j][i]==1: #has been run
                if result[j][0]==0:
                    failed=failed+1
                else:
                    passed=passed+1
        if totalfailed==0:
            suspiciousness.append(1)
        elif totalpassed==0:
            suspiciousness.append(0)
            
        else:
            suspiciousness.append(1-(failed/totalfailed)/((passed/totalpassed)+(failed/totalfailed)))
    print(suspiciousness)
    suspiciousness.sort(reverse=True)
    print(suspiciousness)
    print("the most suspious statement is ",suspiciousness[0])
Tarantula("info.csv")







