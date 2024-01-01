import speech_recognition as sr
import openai
import langchain
import os
import time
import pyttsx3
import wikipedia
import subprocess as sup
import webbrowser as web

def voice():
    rec=sr.Recognizer()

    with sr.Microphone() as mic:
        engine.say("you can start talking now")
        engine.runAndWait()
        print("you can start talking now")

        audio=rec.listen(mic)

        engine.say("time is over")
        engine.runAndWait()
        print("time is over")

    try:
        global vc
        vc=rec.recognize_google(audio)
        print(vc)
        # engine.say(rec.recognize_google(audio))
        # engine.runAndWait()

    except:
        engine.say("it just exploded")
        engine.runAndWait()
        print("it just exploded!!!")
    

engine=pyttsx3.init()
# engine.say("good afternoon sir")
# engine.runAndWait()

t=time.strftime("%H")
# strf creates a string 

if (int(t)>17):
    engine.say("good evening sir!")
    engine.runAndWait()
    print("good evening sir!")
elif (int(t)<12):
    engine.say("good morning sir!")
    engine.runAndWait()
    print("good morning sir!")
else:
    engine.say("good afternoon sir!")
    engine.runAndWait()
    print("good afternoon sir!")

time1="Time is",time.strftime("%H:%M:%S")
engine.say(time1)
engine.runAndWait()
print(time1)

def exit():
    a=input("Enter any key to exit: ")
    if (a=="apocalypse"):
        return exit()
    else:
        print("Later")


# print("Welcome Ghost! The time is",t)

# print(os.getenv("OPENAI_API_KEY"))
# print("hi")
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
def langai():
    engine.say("To speak enter 1 else enter any key:")
    engine.runAndWait()
    xc=int(input("To speak enter 1 else enter any key:"))
    if xc==1:
        voice()
        # rec=sr.Recognizer()

        # with sr.Microphone() as mic:
        #     engine.say("you can start talking now")
        #     engine.runAndWait()
        #     print("you can start talking now")

        #     audio=rec.listen(mic)

        #     engine.say("time is over")
        #     engine.runAndWait()
        #     print("time is over")

        # try:
        #     print(rec.recognize_google(audio))
        #     # engine.say(rec.recognize_google(audio))
        #     # engine.runAndWait()

        # except:
        #     engine.say("it just exploded")
        #     engine.runAndWait()
        #     print("it just exploded!!!")

        # llm = OpenAI(openai_api_key="OPENAI_API_KEY")
        text=vc
        # text=input("enter you Prompt: ")
        llm = OpenAI(temperature=0.3)
        # print(x)

        prompt=PromptTemplate.from_template("{place}?")
        # chain=LLMChain(llm=llm,prompt=prompt)
        output=prompt.format(place=text)
        # print(output)
        x=llm.predict(output)
        print(x)
        engine.say(x)
        engine.runAndWait()
        print("\n")
        return options()
        # import os
        # api_key = os.environ.get('OPENAI_API_KEY')
        # from langchain.llms import OpenAI

        # llm = OpenAI(openai_api_key=api_key,model_name="text-davinci-003",temperature=0.9)
        # x = llm(prompt='"What would be a good company name for a company that makes colorful socks?"')

        # print(x)

    else:
        txt=input("enter your prompt: ")
        text=txt
        # text=input("enter you Prompt: ")
        llm = OpenAI(temperature=0.3)

        # print(x)

        prompt=PromptTemplate.from_template("{place}?")
        # chain=LLMChain(llm=llm,prompt=prompt)
        output=prompt.format(place=text)
        # print(output)
        x=llm.predict(output)
        print(x)
        engine.say(x)
        engine.runAndWait()
        print("\n")
        return options()
        # return langai()
    # langai()

def imagebot():
    rec=sr.Recognizer()

    with sr.Microphone() as mic:

        engine.say("you can start talking now")
        engine.runAndWait()
        print("you can start talking now")
        audio=rec.listen(mic)
        engine.say("time is over")
        engine.runAndWait()
        print("time is over")

    try:
        print(rec.recognize_google(audio))
    except:
        print("it just exploded!!!")

    openai.api_key = os.getenv("OPENAI_API_KEY")

    # engine.say("enter your prompt:")
    # engine.runAndWait()
    # text=input("Enter your prompt: ")

    response = openai.Image.create(prompt=rec.recognize_google(audio),n=2,size="1024x1024")
    image_url=response['data'][0]['url']
    print(image_url)
    print("\n")
    return options()
#imaagebot()
def wiki():
    tst=input("Enter your prompt for Wikipedia: ")
    result = wikipedia.page(tst)
    print(result.summary)
    options()

def aopen():
    zx="Currently you can open following applications: \n1.Calculator\n2.Command prompt\n3.Youtube"
    engine.say(zx)
    engine.runAndWait()
    print(zx)
    engine.say("Which application you want to open: ")
    engine.runAndWait()
    print("Which application you want to open: ")
    rec=sr.Recognizer()

    with sr.Microphone() as mic:
        # engine.say("you can start talking now")
        # engine.runAndWait()
        # print("you can start talking now")

        audio=rec.listen(mic)

        # engine.say("time is over")
        # engine.runAndWait()
        # print("time is over")

    try:
        global vc
        vc=rec.recognize_google(audio)
        print(vc)
        # engine.say(rec.recognize_google(audio))
        # engine.runAndWait()

    except:
        engine.say("it just exploded")
        engine.runAndWait()
        print("it just exploded!!!")
    if vc=="calculator":
        print("true")
        sup.call("calc.exe")
    elif vc=="command prompt":
        print("true")
        sup.call("cmd.exe")
    elif vc=="youtube" or vc=="YouTube":
        web.open("www.youtube.com")
    else:
        print("false")
        return aopen()

x=0
def options():
    global x
    x=x+1
    engine.say("currently we have 4 options")
    engine.runAndWait()
    print("""currently we have 4 options: \n1.Chatbot\n2.Imagebot
3.Wikipedia(under construction)\n4.To open an application\n99. Exit""")
    engine.say("choose an option from above")
    engine.runAndWait()
    option=int(input("Choose an option from above: "))
    if x==3:
        engine.say("too many attempts")
        engine.runAndWait()
        print("too many attempts")
    else:
        if option==1:
            langai()
        elif option==2:
            imagebot()
        elif option==3:
            wiki()
        elif option==4:
            aopen()
        elif option==99:
            return 0
        else:
            engine.say("invalid input")
            engine.runAndWait()
            print("invalid input\n\n")
            return options()
options()
engine.runAndWait()