book ={}
book['Ani'] ={
    'name':'Ani',
    'Address':'Hindupur',
    'phone':'9632215145'
}
book['Prabha'] ={
    'name':'Prabha',
    'Address':'Bengaluru',
    'phone':'9876543210'
}

import json
s = json.dumps(book)
# print(s)
with open('address.txt','w') as f:
    f.write(s)