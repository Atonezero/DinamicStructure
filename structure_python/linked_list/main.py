from LinkedList import LinkedList

if __name__ == "__main__":
    #testing LinkedList
    L1 = LinkedList()
    L1.add(25)
    L1.add(26)
    L1.append(27)

    print(L1)

    print(L1.contains(26))

    L1.remove(25)

    print(L1)