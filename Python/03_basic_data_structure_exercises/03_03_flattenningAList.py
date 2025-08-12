List = [1,2,[1,2,3]]

def listFlattenner(List):
    flatList = []
    for i in List:
        if type(i) == list:
            for j in i:
                flatList.append(j)
        else:
            flatList.append(i)
    return flatList

print(listFlattenner(List))