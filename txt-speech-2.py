from gtts import gTTS
from tkinter import *
import playsound
import  speech_recognition as sr
import pyttsx3

r=sr.Recognizer()
text="Sorry "



def dic(word):
    a={"hi":"Hello","hello":"Hey",
       "how are you":"I am fine",
       "what is your name":
       "my name is Jarvis",
       "how old are you":"I am 20 year old",
       "what you do for living":"I'm an assistant. I can help you with things get done.",
       "crack a joke":"why won't shrimps share their treasure?? because they are shellfish.",
       "how is the weather":"It's pretty cold outside. You wanna go grab a coffee??",
       "what is your favourite dish":"If I could I would love to eat rajma chawal everyday.",
       "you prefer tea or coffee":" I prefer a cup of expresso over anything anytime",
       " do you have a girlfriend":"I,m happy to say I feel whole all on my own",
       "are you a human":"I can talk like a person but I'm not a human",
       "tell me a joke":"What is the most shocking city in the world??? Electricity",
       "what kind of music you like":"I love the bollywood music and sound of chimes",
       "tell me a fun fact":"koalas can sleep upto 20 hours a day ."
       }
    if word in a:
        return a[word]
    elif word=="ok bye":
        return "good bye"
    else:
        return "not known"
def SpeakText(command):
        
        # Initialize the engine
        engine = pyttsx3.init()
        engine.say(command)
        engine.runAndWait()
        
def clicked():
    myobj=gTTS(text=txt.get(),lang="en",slow=False)
    myobj.save("converted.mp3")
    playsound.playsound("converted.mp3",True)
   
txt=""
txt2=""
def Takecommand():
    txt.delete('0',END)
    txt1.delete('0',END)
    SpeakText("I am listening.")
    flag= True
    r = sr.Recognizer()
    #r.dynamic_energy_threshold = False
    #r.energy_threshold = 4000
    with sr.Microphone() as source:
        
        print("Listening...")
        r.adjust_for_ambient_noise(source , duration=4)
        audio = r.listen(source)

    try:
        print("Recognizing..")
        query = r.recognize_google(audio, language='en-in')
        print(f"user Said :{query}\n")
        query = query.lower()
        txt.insert(0,query)
        t=dic(query)
        txt1.insert(0,t)
        SpeakText(t)
    except Exception as e:
        print(e)

    
window=Tk()
window.title("text to speech")
window.geometry('1360x690+-5+0')

background_image=PhotoImage(file="last.png")
img1= PhotoImage(file='robot.png')
img2= PhotoImage(file='button-green.png')
img3= PhotoImage(file='icon.png')
img4= PhotoImage(file='terminal.png')
img5= PhotoImage(file='robot.png')

f = Frame(window,width = 1300, height = 690)
f.place(x=0,y=0)
f.tkraise()
front_image = PhotoImage(file="front.png")
okVar = IntVar()
btnOK = Button(f, image=front_image,command=lambda: okVar.set(1))
btnOK.place(x=0,y=0)
f.wait_variable(okVar)
f.destroy()

background_label = Label(window, image=background_image)
background_label.place(x=0, y=0)

canvas = Canvas(window, width = 800, height = 596)
canvas.place(x=10,y=10)
canvas.create_image(0, 0, image=img1, anchor=NW)

question_button = Button(window,image=img2, bd=0, command=Takecommand)
question_button.place(x=200,y=625)

lbl1=Label(window,text="INTELLIGENT CHATBOT",font=('lacto black',17,'bold'),bg ="sky blue")
lbl1.grid(column=0,row=0)
#lbl2=Label(window,text="    using python",font=('lacto black',17,'bold'),fg ="blue")
#lbl2.grid(column=1,row=0)


frame=Frame(window,width=500,height=596)
frame.place(x=825,y=10)


txt=Entry(frame,textvariable=txt,font=('lacto black',30,'normal'),bg="yellow")
txt.grid(column=5,row=5)

txt1=Entry(frame,textvariable=txt,font=('lacto black',30,'normal'),bg="yellow")
txt1.grid(column=5,row=50)


lbl2=Label(window,text="speak now",font=('lacto black',30,'bold'),fg ="blue")
lbl2.grid(column=25,row=5)
           


lbl2=Label(window,text="",font=('lacto black',18,'bold'),fg ="red")
lbl2.grid(column=0,row=5)



window.mainloop()

           

