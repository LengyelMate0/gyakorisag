import random

def isitPerfect():
    pass

def randomGenerator(s,e,a):
    numbers=list()
    for i in range(a):
        numbers.append(random.randint(s,e))
    return numbers
    
def makeNumber(text):
                            #isCorrect = False
    while True:              #not isCorrect:
        n = input (text)
        try:
            n = int(n)
            isCorrect = True
            return n
        except ValueError:
            print("Helytelen érték.")


startMessage = "Kezdő érték: "
endMessage = "Végső érték: "
amountMessage = "Értékek száma: "

start = makeNumber(startMessage)
end = makeNumber(endMessage)
amount = makeNumber(amountMessage)

randomGenerator(start,end,amount)