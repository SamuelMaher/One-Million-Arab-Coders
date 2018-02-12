import urllib.request as ur

def read_file():
    open_file = open(r"E:\Udacity Full stack foundation\movie_quotes.txt")
    read_file = open_file.read()
    print(read_file)
    open_file.close()
    check_profanity(read_file)

def check_profanity(text):
    connect = ur.urlopen("http://www.wdyl.com/profanity?q="+text)
    response = connect.read()
    connect.close()
    if "true" in response:
        print ("Profanity alert!")
    elif "false" in response:
        print ("This document has no curse words")
    else:
        print ("Could not scan the document properly")
        
read_file()

