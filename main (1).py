def bubbleSort(w):
  for j in range(len(w) - 1):
    for k in range(len(w) - 1 - j):
      if w[k] > w[k + 1]:
        w[k], w[k + 1] = w[k + 1], w[k]


def textSorting():
  print(
    "This code will alphabetically sort the words that you enter. Stop entering words with any number."
  )

  w = []
  while True:
    i = input("Enter the word: ")
    if i.isnumeric():
      break
    else:
      w.append(i.lower())
      continue

  bubbleSort(w)
  #print(w)
  print("Here are the words you entered sorted alphabetically:")

  for i in range(0, len(w)):
    word = w[i]
    letter = word[0]
    print(letter.upper() + " - " + word)


textSorting()
