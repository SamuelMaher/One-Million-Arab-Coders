import urllib.request
import urllib.parse

def read_file():
    open_file = open(r"E:\Udacity Full stack foundation\Text_translate.txt")
    read_file = open_file.read()
    print(read_file)
    open_file.close()
    text_translate(read_file)

def text_translate(text):
    data = urllib.parse.urlencode(text)
    url = "https://translate.google.com"
    req = urllib.request.Request(url,data)
    response = urllib.request.urlopen(req)
    output= response.read()
    print (output)
    req.close()
    
read_file()
