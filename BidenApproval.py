import datetime
Approval = [0.55, 0.48, 0.63, 0.56]
Disapproval = [0.32, 0.45, 0.37, 0.34]
Date = [datetime.datetime(2021, 1, 21), datetime.datetime(2021, 1, 22), datetime.datetime(2021, 1, 22), datetime.datetime(2021, 1, 23)]
Quality = [0.5, 0.8, 1.0, 1.0] #TODO: Put together an actual database of pollsters in the program to be able to reference instead of having to hardcode this in.
RecencyWeight = []
QualityWeight = []
CompositeWeight = []

for i in range(len(Date)):
    delta = int(str(datetime.datetime.now() - Date[i])[0]) #TODO: Fix this to be futureproof for double and triple digit numbers of days. Also eventually make a verion of this program that just calculates a polling average for every day instead of calculating a new one after each and every poll that erases the old.
    RecencyWeight.append(0.5**(delta/21))
for i in range(len(Quality)):
    QualityWeight.append(0.1 * (-2 * Quality[i] + 6.8))
for i in range(len(RecencyWeight)):
    CompositeWeight.append(RecencyWeight[i] * QualityWeight[i])

def Average():
    AppSum = 0
    DisSum = 0
    Divisor = 0
    for i in range(len(Approval)):
        AppSum += (Approval[i] * CompositeWeight[i])
        DisSum += (Disapproval[i] * CompositeWeight[i])
        Divisor += CompositeWeight[i]
    AppAverage = AppSum/Divisor
    DisAverage = DisSum/Divisor
    Margin = AppAverage - DisAverage
    return [AppAverage, DisAverage, Margin]
print(Average())