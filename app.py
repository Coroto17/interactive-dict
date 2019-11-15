#  Dynamic Dictionary
import json
import difflib as dl

data = json.load(open("data.json"))

def translate(word):
    if word in data:
        return data[word]
    elif len(dl.get_close_matches(word, list(data), cutoff=0.7)) > 0:
        matches = dl.get_close_matches(word, list(data), cutoff=0.7)[0]
        yes_no = input(f"Did you mean {matches} instead? ").lower()
        if yes_no == "y":
            return data[matches]
        elif yes_no == "n":
            return "Please try again with another word"
        else:
            "You didn't answer with 'y' or 'n'. Please run the program again"
    else:
        return "Word not found. Please try again! " 

query = input("Enter word: ").lower()
output = translate(query)

if type(output) == list:
    for l in output:
        print(l)
else:
    print(output)