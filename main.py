def bubbleSort(w): # this function is used to sort list items
  for j in range(len(w) - 1):
    for k in range(len(w) - 1 - j):
      if w[k] > w[k + 1]:
        w[k], w[k + 1] = w[k + 1], w[k]


def textSorting():
        while True:
                print("\n"+" -- Code for sorting words -- " + "\n")
                print("[1] Enter words one by one" + "\n" +
                    "[2] Copy a list of words" + "\n" + "[0] Stop the code")
                
                o = input("Enter your choice: ")
                
                if o.isnumeric() == False:
                    print("\n    ERROR:"+"Your choice must be a number."+"\n")
                    
                else:
                    option = int(o)
                    print("\n")
                    if option == 0:
                        break
                    elif option == 1:
                        w = []
                        while True:
                                i = input("Enter the word: ")
                                if i.isnumeric():
                                        break
                                else:
                                        w.append(i.lower())
                                        continue
                                        
                                bubbleSort(w)
                                
                                print("Here are the words you entered sorted alphabetically:")
                                
                                for i in range(0, len(w)):
                                        word = w[i]
                                        letter = word[0]
                                        print(letter.upper() + " - " + word)
                    
                    elif option == 2:
                            print("You can copy the list but each item of the list has to be separated with #. ")
                            list = input("Copy the list here: ")
                            w= list.split("#")
                            bubbleSort(w)
                            print("Here are the words you entered sorted alphabetically:")
                            for i in range(0, len(w)):
                                    word = w[i]
                                    letter = word[0]
                                    print(letter.upper() + " - " + word)


textSorting()
