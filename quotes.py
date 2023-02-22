import requests
import time
from dataclasses import replace

max_length = 30

class Quote:
    def __init__(self):
        self.data = requests.get(f"https://api.quotable.io/random?maxLength=100").json()
        pass
    def update(self):
        self.data = requests.get(f"https://api.quotable.io/random?maxLength=100").json()
        return self.data
    def quote_string(self):
        msg_list = []
        length = 0
        index = 0
        
        quote = self.data["content"]
        print(quote)
        quote = quote.replace(',', ',\n')
        quote = quote.replace(';', ';\n')
        quote = quote.replace(':', ':\n')
        quote = quote.replace('.', '.\n')
        author = self.data["author"]
        
        ls = list(quote.split(' '))
        for i in range(len(ls)):
            length = length + len(ls[i]) + 1
            if length >= max_length or ls[i].find('\n') != -1:
                for j in range(index, i+1):
                    if (j != i):
                        msg_list.append(ls[j] + " ")
                    else:
                        if ls[i].find('\n') != -1:
                            msg_list.append(ls[j])
                        else:
                            msg_list.append(ls[j] + "\n")
                        index = i+1
                length = 0
            elif i == (len(ls)-1):
                for j in range(index, len(ls)):
                    msg_list.append(ls[j] + " ")
                    
        # msg_list.append("- " + author)
        # print(msg_list)          
        quote = ''.join(msg_list)
        quote_author = "- " + author
        print(quote)
        print(quote_author)
        
        return quote, quote_author
    