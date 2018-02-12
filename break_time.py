import time
import webbrowser

count=0
print("This Program start @ " + time.ctime())
while(count<3):
    time.sleep(7200)
    webbrowser.open("https://www.youtube.com/watch?v=yzko3DSPPc8")
    count+=1
