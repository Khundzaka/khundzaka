def plus_2(base, element):
    return element + base
def reducexelit(func, sia):
    axalisia = sia[0]
    lengthof = len(sia) -1
    d=1
    while(d <= lengthof):
        axalisia = func(axalisia, sia[d])
        d+=1
    return axalisia
chemisia = [2,3,4,5]
print (reducexelit(plus_2, chemisia))
