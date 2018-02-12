import urllib.request as ur
def read_text():
        file =open(r"E:\Udacity Full stack foundation\Mariam.txt")
        content_of_file = file.read()
        print(content_of_file)
        file.close()
        check_profanity(content_of_file)
def check_profanity(text_to_check):
        connection = ur.urlopen("http://www.wdylike.appspot.com/?="+text_to_check)
        output = connection.read()
        print(output)
        connection.close()
        
read_text()
