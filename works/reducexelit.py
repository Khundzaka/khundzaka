def plus_2(base, element):
    return element + base
def reducexelit(func, sia):
    axalisia = 0
    for elementi in sia:
        axalisia = func(axalisia, elementi)
    return axalisia
chemisia = [2,3,4,5]
print (reducexelit(plus_2, chemisia))
