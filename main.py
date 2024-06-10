import os
from dotenv import load_dotenv
from tkinter import *
from tkinter import Text, Frame, Button, Menubutton
from tkinter import filedialog
from core.Editor.TextEditor import TextEditor
from core.engines.phi3 import LLM

load_dotenv()

def commands():
    pass
class ApplicationWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("BrainPad")
        self.llm = LLM(os.getenv("KEY"))
        self.text_editor = TextEditor(root,self.llm)
        self.button_frame = Frame(root)
        self.button_frame.grid()
        self.open = Button(self.button_frame, text="Open", command=self.text_editor.open_file)
        self.open.pack(side=LEFT)
        self.save_button = Button(self.button_frame, text="Save", command=self.text_editor.save_as)
        self.save_button.pack(side=LEFT)
        self.summarize = Button(self.button_frame, text="Summarize", command=self.text_editor.summarize)
        self.summarize.pack(side=LEFT)
        self.generate = Button(self.button_frame, text="generate", command=self.text_editor.generate)
        self.generate.pack(side=LEFT)

if __name__ == "__main__":
    root = Tk()
    app = ApplicationWindow(root)
    root.mainloop()
