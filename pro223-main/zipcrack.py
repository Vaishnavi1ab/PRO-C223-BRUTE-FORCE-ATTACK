import zipfile
import time 

file_path = input("enter your zip file path:")
zipf = zipfile.ZipFile(file_path)

global result
global tried
result =0 
tried = 0
c=0

if not zipf:
    print(f'the file {file_path} is not encrypted . you can open it ')
else:
    start_time = time.time()
    wordListFile = open('word.txt', 'r',errors='ignore')
    body = wordListFile.read().lower()
    words = body.split('\n')

    for i in range(len(words)):
        word = words[i]
        password=word.encode('utf8').strip()
        c=c+1
        print('Trying to decode password by: {}'.format(word))
        try:
            with zipfile.ZipFile(file_path,'r') as zf:
                zf.extractall(pwd=password)
                print("Success! The password is: "+ word)
                end_time = time.time()            #Save the end time
                result = 1                       #Set result variable to 1 on success
            break
        except:
             pass
     
    if(result == 0):
        duration = end_time - start_time
        print("Sorry, password not found. A total of "+str(c)+"+ possible combinations tried in "+str(duration)+" seconds. Password is not of 4 characters.")
    else:
        duration = end_time - start_time
        print('Congratulations!!! Password found after trying '+str(c)+' combinations in '+str(duration)+' seconds')
