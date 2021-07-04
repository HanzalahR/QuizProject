from tkinter import * #This is the built-in widget
import random

question = [ # list of questions
  "Which is the best source of calcium?",
  "What does calcium do?",
  "What is the best way to avoid getting a cold?",
  "What does it take to keep your mind alert?",
  "What is the best way to rehydrate after exercise?"
]
questions_answers = [ # List of options for answers
  ["Meat" , "Yogurt" , "Bread", "Potatoes"],
  ["Builds and repairs muscles", "Makes you fat", "Strengthens the bones", "Helps you feel full"],
  ["Washing hands regularly", "Wearing a mask", "Staying indoors", "Workout"],
  ["Energy", "Calcium", "Carbohydrates", "Protein"],
  ["Eat fruits", "Energy drnks", "Water", "Milk"],
]
answers=[1, 2, 0, 0, 2] #these numbers correspond to the value of Radiobutton

score = 0

gameOver = False
asked = []
def randomiser(): #the questions will be randomised
    global qnum, quiz_instance, gameOver
    try:
      if gameOver == False:
        qnum = random.randint(0, 4)
        if qnum not in asked:
            asked.append(qnum)
        elif qnum in asked:
            randomiser()
    except RecursionError:
      print("GAMEOVER")
      quiz_instance.gameOver()
      gameOver = True;


class QuizStarter:
    def __init__(self, parent):
        background_color = "Black" # The background colour
        primary_color = "#FEE715" #font colour for the starting page
        self.quiz_frame = Frame(parent, bg = background_color, padx = 100, pady = 100)
        self.quiz_frame.grid()
        
        self.heading_label = Label(self.quiz_frame, text = "Health and Fitness quiz", font = ("Myriad", "20", "italic", "bold"), fg = primary_color, bg = background_color)
        self.heading_label.grid(row = 0, padx = 20)

        self.user_label = Label(self.quiz_frame, text = "Enter username please:", font = ("Myriad", "16"), fg = primary_color, bg = background_color)
        self.user_label.grid(row = 1, padx = 20, pady = 20)

        self.entry_box = Entry(self.quiz_frame)
        self.entry_box.grid(row = 2, padx = 20, pady = 20)

        self.continue_button = Button(self.quiz_frame, text = "Start", font = ("Myriad", "13"), bg = primary_color, command=self.name_collection)
        self.continue_button.grid(row = 3, padx = 20, pady = 10)
      
    def name_collection(self):
      global name, quiz_instance
      name = self.entry_box.get()
      if len(name) == 0:
        name = 'Anonymous User'
      self.quiz_frame.destroy()
class QuizQ:
  def __init__(self,parent):
    self.background_color = "Black" # The background colour
    self.primary_color = "#FEE715" #font colour
    self.var1 = IntVar()
    self.checkAnswerState = 1

    self.quiz_frame = Frame(parent, bg = self.background_color, padx = 100, pady = 100)
    self.quiz_frame.grid()

    self.askQuestion = Label(self.quiz_frame, text = question[qnum] , font = ("Myriad", "16"), fg = self.primary_color, bg = self.background_color)
    self.askQuestion.grid(row = 1, padx = 20, pady = 10)

    self.buttons=[1, 2, 3, 4] #this numbers serve as placeholders
    for i in range(4):  #list all options for selected question
      self.buttons[i] = Radiobutton(self.quiz_frame,text=questions_answers[qnum][i],font=("Myriad", "12"), bg=self.background_color,value=i,padx=10,pady=10, variable=self.var1, fg = self.primary_color, selectcolor=self.background_color)
      self.buttons[i].grid(row=i+2, sticky=W)
  
    #confirm Button
    self.quiz_instance=Button(self.quiz_frame,text="Confirm",font=("Myriad","13", "italic"), bg=self.primary_color, command=self.checkAnswer)
    self.quiz_instance.grid(row=7, padx=5, pady=5)

  def checkAnswer(self):
    global score
    if self.checkAnswerState == 1:
      if self.var1.get() == answers[qnum]:
        self.askQuestion['text']='Correct!'
        score +=1
      else:
        self.askQuestion['text']="Sorry, that's incorrect"
        score -=1
      self.quiz_instance['text'] = "Next Question"
    elif self.checkAnswerState == -1:
      self.quiz_frame.destroy()
      randomiser()
      quiz_instance = QuizQ(root)
    self.checkAnswerState*=-1 #alternate between 2 states

  randomiser()
if __name__ == "__main__":
  root = Tk()
  root.title("Health and fitness quiz")
  root.resizable(False, False) #fix
  quiz_instance = QuizStarter(root)
  root.mainloop()