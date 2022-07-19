import json
from difflib import get_close_matches
data = json.load(open("data.json"))
print("========================= [ DICTIONARY ] =========================")
def translate(word):
    word=word.lower()
    if word in data:
        return(data[word])
    elif word.title() in data:
        return(data[word.title()])
    elif word.upper() in data:
        return(data[word.upper()])
    elif len(get_close_matches(word,data.keys())) > 0 :
        print("Did you Mean %s instead..." %get_close_matches(word, data.keys())[0])
        decide = input("Press Y for Yes and N for No...")
        if decide == 'Y' or decide == 'y' :
            return data[get_close_matches(word, data.keys())[0]]
        elif decide == 'N' or decide == 'n' :
            print("Pugger your Paw steps on Wrong Keys...")
        else:
             print("You have Entered Wrong Input plese Enter just Y or N ...")
    else:
        print("Pugger your Paw steps on Wrong Keys...")
ch = 'y'
while ch == 'y' or ch == 'Y' :
    word = input("Enter the Word you want to Search :  ")
    output = translate(word)
    if output != None:
        if type(output) == list:
            print("Meaning - ")
            for item in output:
                print(" => "+ item)
        else:
            print("Meaning - ")
            print(" => "+ output)
    ch = input("Want to Search more Words from the Dictionary...[Y/N]... : ")
