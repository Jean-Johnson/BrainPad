from tkinter import Text, Frame, Button, Menubutton
from tkinter import filedialog
class TextEditor:
    def __init__(self, root,llm):
        self.llm = llm
        self.text = Text(root)
        self.text.grid()

    def save_as(self):
        t = self.text.get("1.0", "end-1c")
        save_location = filedialog.asksaveasfilename()
        if save_location:
            with open(save_location, "w+") as file1:
                file1.write(t)
    def open_file(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            with open(file_path, "r") as file:  
                content = file.read()
                self.text.delete("1.0", "end")
                self.text.insert("1.0", content)
    def summarize(self):
        text_content = self.text.get("1.0", "end-1c")
        if text_content:
            uppercased_text = text_content.upper()
            self.text.insert("end", "\n Summary create by llm")
            self.text.insert("end", "\n"+uppercased_text)
    def generate(self):
        text_content = self.text.get("1.0", "end-1c")
        self.llm.generate(self.text,text_content)
        # generated = self.llm.call("HI",self.text)
        # if text_content:
        #     self.text.insert("end", generated)

    def set_font_helvetica(self):
        self.text.config(font="Helvetica")

    def set_font_courier(self):
        self.text.config(font="Courier")