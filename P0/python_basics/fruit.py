fruitPrices = {'apples':20.0, 'pear': 10.0, 'orange': 11.0}

def buyFruit(fruit, numPounds):
    if fruit not in fruitPrices:
        print "Sorry we dont have %s in store" % (fruit)
    else:
        cost = numPounds * fruitPrices[fruit]
        print "Your total will be %f please" % (cost)

# Main function 
if __name__ == '__main__':
    buyFruit('apples', 2)
    buyFruit('orange', 3)
    buyFruit('grape', 2)
