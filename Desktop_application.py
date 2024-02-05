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
    "software": "logiciel",
    "internet": "internet",
    "data": "données",
    "science": "science",
    "machine": "machine",
    "learning": "apprentissage",
    "artificial": "artificielle",
    "intelligence": "intelligence",
    "developer": "développeur",
    "keyboard": "clavier",
    "mouse": "souris",
    "screen": "écran",
    "algorithm": "algorithme",
    "database": "base de données",
    "function": "fonction",
    "variable": "variable",
    "loop": "boucle",
    "conditional": "conditionnelle",
    "statement": "déclaration",
    "debugging": "débogage",
    "comment": "commentaire"

}
def search(word):
    if word in french_dict:
        result.set("french_dict[word]")
        print(french_dict[word])
    else:
        result.set("Not Found")
        print("Not Found")
search_btn = Button(window, text="search", command=lambda :search(entry_text.get()))
search_btn.pack()
result_Label.pack()
window.mainloop()
  
