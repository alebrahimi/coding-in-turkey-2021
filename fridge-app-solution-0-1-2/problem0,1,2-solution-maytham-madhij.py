#  
# The Fridge app uses Dictionary data structure instead of Array
# 

items = {'tomato': 9, 'banana': 7, 'apple': 4, 'onion': 8, 'cucumber': 3}

def printFridgeItems():
    print("-------------------------------")
    print("items            |    count")
    print("-------------------------------")
    for i in items:
        print(i , (15 - len(i)) * " ", "|     " , items[i])
    print("-------------------------------")

def addItem():
    userInput = input("\nEnter item name and the count seprated by comma ( Example:  carrot,5 ) : ")
    i, c = userInput.split(",")
    c = int(c)
    items.update({ i : c + items[i] if i in items else c })

def removeItem():
    userInput = input("\nEnter item name and the count seprated by comma ( Example:  banana,5 ) : ")
    i, c = userInput.split(",")
    c = int(c)

    if i not in items:
        print("-------------------------------")
        print("There is no (", i, ") in the fridge")
        return
    elif items[i] == c:
        items.pop(i)
    elif items[i] > c:
        items.update({ i : items[i] - c })
    else:
        print("-------------------------------")
        print("This quantity is not avilable, you only have ", items[i], " ", i)

def findItem():
    i = input("\nEnter item name to search : ")
    print("-------------------------------")
    if i in items:
        print("You have (", items[i], i, ") in the fridge")
    else:
        print("You don't have any (", i, ") in the fridge")

def validateRecipe():
    userInput = input("\nEnter the recipe items names and the counts seprated by comma and space ( Example:  banana,5 tomato,2 onion,1 ) : ")
    recipe = userInput.split()
    canCook = True
    for r in recipe:
        i, c = r.split(",")
        c = int(c)
        if i not in items or items[i] < c:
            canCook = False

    print("-------------------------------")
    if canCook:
        print("You can cook, you have all the recipe items")
    else:
        print("You can't cook, you have a missing items")

def emptyFridge():
    items.clear()
    print("-------------------------------")
    print("The Fridge empty now")


def fridge(option):
    if(option == 1):
        printFridgeItems()
    elif(option == 2):
        addItem()
    elif(option == 3):
        removeItem()
    elif(option == 4):
        findItem()
    elif(option == 5):
        validateRecipe()
    elif(option == 6):
        emptyFridge()
    elif(option == 7):
        print("-------------------------------")
        print("Good Bye")
        print("-------------------------------")
    else:
        print("-------------------------------")
        print("Not an option!")
        print("-------------------------------")


def app():
    print("\n************************************")
    userInput = input("\nEnter option number : ")

    if(str(userInput).isnumeric()):
        option = int(userInput)
        if(option == 7 ):
            fridge(option)
            return
        else:
            fridge(option)
            app()
    else:
        print("Please Enter numeric option!")
        app()

print("\n************************************")
print("(( The Fridge ))")
print("************************************\n")
print("1 - To print fridge Items.")
print("2 - To add new Item(s) to the fridge.")
print("3 - To remove item(s) from the fridge.")
print("4 - To find Item(s) in the fridge.")
print("5 - To validate recipe.")
print("6 - To empty the fridge.")
print("7 - To close the fridge.")

app()