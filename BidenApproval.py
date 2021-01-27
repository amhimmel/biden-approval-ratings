Approval = [0.55, 0.48, 0.63, 0.56, 0.48, 0.48]
Disapproval = [0.32, 0.45, 0.37, 0.34, 0.47, 0.47]
Date = [2, 3, 3, 4, 5, 6]
Quality = [0.5, 0.8, 1.0, 1.0, 0.8, 0.8] #TODO: Put together an actual database of pollsters in the program to be able to reference instead of having to hardcode this in.
PollsterID = [1, 2, 3, 4, 2, 2] #TODO: Do something with this to discount earlier polls from the same pollster.

def Average(day):
    AppSum = 0
    DisSum = 0
    Divisor = 0
    RecencyWeight = []
    QualityWeight = []
    CompositeWeight = []
    test = False
    for i in range(len(PollsterID)):
        for j in range(len(PollsterID)):
            if PollsterID[i] == PollsterID[j] and i != j:
                if Date[j] <= day and Date[i] <= day:
                    Approval.remove(Approval[i])
                    Disapproval.remove(Disapproval[i])
                    Date.remove(Date[i])
                    Quality.remove(Quality[i])
                    PollsterID.remove(PollsterID[i])
                    test = True
                    break
        if test == True:
            break
    for i in range(len(Date)):
        if Date[i] <= day:
            delta = day - Date[i]
            RecencyWeight.append(0.5**(delta/21))
        else:
            break
    for i in range(len(RecencyWeight)):
        QualityWeight.append(0.1 * (-2 * Quality[i] + 6.8))
    for i in range(len(RecencyWeight)):
        CompositeWeight.append(RecencyWeight[i] * QualityWeight[i])
    for i in range(len(RecencyWeight)):
        AppSum += (Approval[i] * CompositeWeight[i])
        DisSum += (Disapproval[i] * CompositeWeight[i])
        Divisor += CompositeWeight[i]
    AppAverage = AppSum/Divisor
    DisAverage = DisSum/Divisor
    Margin = AppAverage - DisAverage
    return str("Day " + str(day) + ": " + str([AppAverage, DisAverage, Margin]))

for i in range(2, 8):
    print(Average(i))
