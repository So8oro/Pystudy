text = input()

happy = 0
sad = 0
idx = 0

while idx < len(text):
    if text[idx]==':' and text[idx+1]=='-':
        if text[idx+2]==')':
            happy += 1
            idx += 3
        elif text[idx+2]=='(':
            sad += 1
            idx += 3
        else:
            idx += 2
    else:
        idx += 1

if happy==0 and sad==0:
    print('none')
elif happy > sad:
    print('happy')
elif happy < sad:
    print('sad')
else:
    print('unsure')