def plus_2(element):
    return element + 2
def mapxelit(func, sia):
    axalisia= []
    for elementi in sia:
        axalisia.append(func(elementi))
    return axalisia
chemisia = [2,3,4,5]
print (mapxelit(plus_2, chemisia))
