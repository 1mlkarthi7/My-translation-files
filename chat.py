import time
now=time.ctime()
qna={"hello":"Hii", "how are you?":"Fine! thank you", "Where are you working?":"I'm working at Zabda", "How many employees?":"There are 20", "What is your name?":"My name is Karthika", "What is current time":now}
while True:
    qs=input()
    if(qs==quit):
        break
    else:
        print(qna[qs])