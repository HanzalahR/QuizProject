from tkinter import * #This is the built-in widget
import random

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


      randomiser()
if __name__ == "__main__":
  root = Tk()
  root.title("Health and fitness quiz")
  root.resizable(False, False) #fix
  quiz_instance = QuizStarter(root)
  root.mainloop()