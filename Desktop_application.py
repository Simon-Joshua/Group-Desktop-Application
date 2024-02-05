from tkinter import Tk, Entry, Button, Label, StringVar

window = Tk()
window.geometry("600x250")
window.title("French Dictionary")
result = StringVar()
result_Label = Label(window, textvariable=result)
entry_text = Entry(window)
entry_text.pack()
french_dict = {
    "come" : "viens",
    "go" : "aller",
    "sit" : "s'asseoir",
    "eat" : "manger",
    "hello" : "bonjour",
    "stand" : "rester",
    "chair" : "chaise",
    "computer" : "ordinateur",
    "book" : "livre",
    "door" : "porte",
    "world": "monde",
    "python": "python",
    "code": "code",
    "language": "langue",
    "programming": "programmation",
  