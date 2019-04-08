from cov import getMatrix
import numpy as np
import pandas as pd
import math

def count(s, r):
    Ncs, Nus, Ncf, Nuf = 0, 0, 0, 0
    for i in range(len(s)-1):
        if r[i] == 0:
            if s[i] == 1:
                Ncs += 1
            else:
                Nus += 1
        else:
            if s[i] == 1:
                Ncf += 1
            else:
                Nuf += 1
    Nc = Ncs + Ncf
    Nu = Nus + Nuf
    Ns = Ncs + Nus
    Nf = Ncf + Nuf
    N = Nc + Nu
    return Ncs, Nus, Ncf, Nuf, Nc, Nu, Ns, Nf, N

def cal_ChiSquare(Ncs, Nus, Ncf, Nuf, Nc, Nu, Ns, Nf, N):
    Ecf = Nc*Nf/N
    Ecs = Nc*Ns/N
    Euf = Nu*Nf/N
    Eus = Nu*Ns/N
    return (Ncf-Ecf)**2/Ecf + (Ncs-Ecs)**2/Ecs + (Nuf-Euf)**2/Euf + (Nus-Eus)**2/Eus

def cal_ContingencyCoefficient(ChiSquare, N, row=2, col=2):
    return (ChiSquare/N)/math.sqrt((row-1)*(col-1))

def cal_Phi(Ncf, Ncs, Nf, Ns):
    Pf = Ncf / Nf
    Ps = Ncs / Ns
    return Pf / Ps

def cal_Zeta(Ncs, Nus, Ncf, Nuf, Nc, Nu, Ns, Nf, N):
    ChiSquare = cal_ChiSquare(Ncs, Nus, Ncf, Nuf, Nc, Nu, Ns, Nf, N)
    M = cal_ContingencyCoefficient(ChiSquare, N)
    Phi = cal_Phi(Ncf, Ncs, Nf, Ns)
    if Phi > 1:
        return M
    elif Phi < 1:
        return -M
    else:
        return 0

def crosstab():
    matrix = getMatrix()
    m = np.matrix(matrix)
    results = list(matrix[:, -1]) # the last column (r)
    suspiciousness = []
    for i in range(matrix.size-1):
        s_i = list(matrix[:, i])
        Ncs, Nus, Ncf, Nuf, Nc, Nu, Ns, Nf, N = count(s_i, results)

        # calculate the Zeta value, the larger it is, the more suspicious the statement
        Zeta = cal_Zeta(Ncs, Nus, Ncf, Nuf, Nc, Nu, Ns, Nf, N)
        suspiciousness.append(Zeta)

    # rank the statements based on their suspiciousness in a descending order
    sorted_index = list(np.argsort(-np.array(suspiciousness)))
    sorted_susp = sorted(suspiciousness, reverse=True)

    # write to csv file
    data = np.array([[sorted_index[i]+1, sorted_susp[i]] for i in range(len(sorted_susp))])
    df = pd.DataFrame(data, index=[i+1 for i in range(len(sorted_susp))], columns=['Statement', 'Suspiciousness'])
    df.to_csv('rank_crosstab.csv')
    # df.to_csv('rank.csv', index=False)

    # print the rank
    # print(df)

    return df


if __name__ == "__main__":
    print(crosstab())