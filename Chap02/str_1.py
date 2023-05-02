word = input("Your word: ")

index = word.find('a')
print(index)

print(word[:index+1])
print(word[index+1:])