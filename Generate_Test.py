import random
import xlwt
def randomarray(max,mode):
    result=[]
    for i in range(max):
        result.append(random.randint(0,5000))
    if mode=='sorted':
        result.sort()
        return result
    elif mode=='random':
        return result
    elif mode=='nearly':
        result.sort()
        index=random.randint(0,max-2)
        while(result[index]==result[index+1]):
            index = random.randint(0, max - 2)
        temp=result[index]
        result[index]=result[index+1]
        result[index+1]=temp

        return result

def savedata():
    for mode in ['nearly']:
        for j in [5, 15, 30]:  # each line has
            f = xlwt.Workbook()  # open workbook
            sheet1=f.add_sheet('sheet1')  # create sheet
            for i in range(5000): #5000 lines
                result = randomarray(j, mode)
                print(result)
                for s in range(len(result)):
                    sheet1.write(i,s,result[s])
            f.save('text_'+mode+str(j)+'.xls')
savedata()







