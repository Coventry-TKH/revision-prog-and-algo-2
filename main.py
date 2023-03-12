class node:
    def __init__(self, value):
        self.prev = None
        self.data = value
        self.next = None


class LL:
    def __init__(self):
        self.head = node(None)
    
    def add(self, value):
        temp = node(value)

        if self.head.next == None:   #emtpy linkedlist
            self.head = temp
            temp.prev = self.head
        else:
            temp.next = self.head.next
            self.head.next = temp
            
        
    def printLL(self):
        print(self.head.next.data)
            
        
linkedlist = LL()
# linkedlist.printLL()
linkedlist.add(5)
# linkedlist.printLL()
linkedlist.add(7)
# linkedlist.printLL()
linkedlist.add(9)
linkedlist.printLL()

node1 = node(5)
node2 = node(7)
node3 = node(9)

node1.next = node2
node2.prev = node1
node2.next = node3
node3.prev = node2

# print(node1.data, " ", node1.next.data, " ", node2.next.data)

























class Map:      # Map ADT
    def __init__(self, key = [], value = []):
        self.key = key
        self.value = value

    def addToMap(self, key, value):
        if key not in self.key: 
            self.key.append(key)
            self.value.append(value)
            print(self.key, self.value)
        else:
            tempIndex = self.key.index(key)
            self.value[tempIndex] = value
            print(self.key, self.value)


    def delFromMap(self, key):
        if key in self.key:
            tempIndex = self.key.index(key)
            self.key.remove(key)
            self.value.remove(self.value[tempIndex])
            print(self.key, self.value)
            
        

# mydict = Map()
# mydict.addToMap("Mohamed", "Crepe")
# mydict.addToMap("mohamed", "Pepsi")
# mydict.delFromMap("mohamed") 



class set:
    def __init__(self, list = []):
        self.list = list
    
    def add(self, value):
        if value in self.list:
            return
        else:
            self.list.append(value)

    def printList(self):
        print("{", end="")
        for val in self.list:
            print(val, end=", ")
        print("}")
        print(self.list)
        

# firstSet = set([1,2,3,4,5,2,1])

# firstSet = set()
# firstSet.add(1)
# firstSet.add(2)
# firstSet.add(3)
# firstSet.add(4)
# firstSet.add(5)
# firstSet.add(2)
# firstSet.add(1)
# firstSet.printList()




class human:
    #created an object 
    def __init__(self, name, age, gender, id):
        self.name = name
        self.age = age
        self.gender = gender
        self.id = id

    #defined some functions
    def eating(self, food):
        print(f"{self.name} is eating {food}")

# human1 = human("Adham", 19, "M", 1234567890)

# human1.eating("Crepe")







def greetings(name):
    print(f"Hello, {name}")

message = "Nope"

# control statement => the statments are executed one time onlyyyy

# if message == "No":
#     print("She said No!")
# elif message == "Yes":
#     print("Lucky Me")
# else:
#     print("Error")

# print(type(message))


# loops doing something in a number of certain times

# for iteration in range(0, 5):
    # print(iteration)

# count = 0
# while count < 5:
#     # print(count)
#     count = count + 1


listOfNums = [1, 2, 3, 4, 5, 6]
listOfAlpha = "Lorem Ipsum is simply dummy text of the printing and typesetting industry."




# print(listOfNums)
listOfNums[2] = 99
# print(listOfNums)

tupleOfNumbers = (1, 2, 3, 4, 5, 6)

# print(tupleOfNumbers)


semester = {'Mohamed' : 'prog-&-algo-2',
            'Omar' : 'prog-&-algo-2',
            'Mohamed' : 'Math'}

semester['Omar'] = 'Adv. pen-testing'
# print(semester)

name = "Ziad"       #OOP
# greetings(name)
