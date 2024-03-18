counter=0
characters = ['0', '1', '2', '3', '4', '5', '6' '7', '8', '9',
              'a', 'b', 'c','d', 'e','f','g','h','k','m','n','o','p', 'q', 'i',
              'o', 'p', 'q', 'r', 's', 't', 'u', 'v','w','x','y', 'z']
# print(len(characters)) 

words = open('word.txt','w')

for i in characters:
    for j in characters:
        for k in characters:
            for l in characters:
                guess = str(i)+str(j)+str(k)+str(l)
                words.write(guess)
                words.write("\n")
                counter+=1
            
            
print(f'word.txt has been created with {counter} words')