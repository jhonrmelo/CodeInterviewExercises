def secondGreatest(array):
    secondestGreat = None
    greatest = None
    iterator = 0
    for element in array:
        if iterator == 0:
            greatest = element
        elif element > greatest:
                secondestGreat = greatest
                greatest = element
        elif secondestGreat == None:
            secondestGreat = element
        elif element > secondestGreat:
                secondestGreat = element
            
        
        iterator = iterator + 1
        
    print(secondestGreat)

secondGreatest([2,2,1])
    