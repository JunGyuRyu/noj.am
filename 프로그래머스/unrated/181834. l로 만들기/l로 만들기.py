def solution(myString):
    for i in myString:
        if i < 'l':
            myString = myString.replace(i, 'l')
    return myString