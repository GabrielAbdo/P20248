"""
12.

"""


import os.path
import string

var_file="eksetastiki.txt"

if not os.path.isfile(var_file):
    print("Δε βρέθηκε το αρχείο")
else:

    f1=open(var_file,"r",encoding='utf-8')

    flag=1
    word=""
    while flag:

        x=f1.readline()
        print(x)
        
        if x=="":
            flag=0
        else:
            for i in x:
                if i in string.punctuation:
                    word+=" "
                elif i in string.ascii_letters:
                    word+="A"
                elif i in string.digits:
                    word+="1"
                elif ord(i) <= 128:
                    word+="p"
                else:
                    word+="?"

                if len(word) == 16:
                    print(word)
                    word=""    
                     
        
    print(word)
            
    f1.close()