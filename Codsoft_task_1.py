from tkinter import *
from tkinter import ttk

class Todo:
    def __init__(self, root):
        self.root = root
        self.root.title('To-Do List')
        self.root.geometry("650x410+300+150")
        
        

        self.label = Label(self.root, text="To-Do List App",
                           font='Arial 25 bold', width=10, bd=5, bg='red', fg='black')
        self.label.pack(side='top', fill=BOTH)
        
        

        self.label2 = Label(self.root, text="Add Task",
                    font='Arial 18 bold', width=10, bd=5, bg='red', fg='black')
        self.label2.place(x=40, y=54)
        
        

        self.label3 = Label(self.root, text="Tasks",
                    font='Arial 18 bold', width=15, bd=5, bg='red', fg='black')
        self.label3.place(x=200, y=54)
        
        

        self.main_text = Listbox(self.root, height=15, bd=5, width=45, font='Arial 10 bold')
        self.main_text.place(x=300, y=100)
        
        

        self.text = Text(self.root, bd=5, height=2, width=30, font='Arial 10 bold')
        self.text.place(x=20, y=120)
        
        

        self.button = Button(self.root, text="Add", font="Arial 20 bold italic",
                             width=10, bd=5, bg="red", fg="black", command=self.add)
        self.button.place(x=30, y=180)
        
        

        self.button2 = Button(self.root, text="Delete", font="Arial 20 bold italic",
                              width=10, bd=5, bg="red", fg="black", command=self.delete)
        self.button2.place(x=30, y=250)
        
        

        self.button3 = Button(self.root, text="Update", font="Arial 20 bold italic",
                              width=10, bd=5, bg="red", fg="black", command=self.update)
        self.button3.place(x=30, y=320)
        
        

        self.load_tasks()
        
        

    def add(self):
        content = self.text.get(1.0, END).strip()
        if content:
            self.main_text.insert(END, content)
            with open('data.txt', 'a') as file:
                file.write(content + '\n')
            self.text.delete(1.0, END)
            
            

    def delete(self):
        try:
            selected_task_index = self.main_text.curselection()[0]
            selected_task = self.main_text.get(selected_task_index)

            with open('data.txt', 'r') as file:
                tasks = file.readlines()

            with open('data.txt', 'w') as file:
                for task in tasks:
                    if task.strip("\n") != selected_task:
                        file.write(task)

            self.main_text.delete(selected_task_index)
        except IndexError:
            pass  
        
        

    def update(self):
        try:
            selected_task_index = self.main_text.curselection()[0]
            selected_task = self.main_text.get(selected_task_index)
            
            
            self.text.delete(1.0, END)
            self.text.insert(END, selected_task)
            
            
            self.button.config(text="Save Update", command=lambda: self.save_update(selected_task_index))
        except IndexError:
            pass  
        
        

    def save_update(self, task_index):
        updated_task = self.text.get(1.0, END).strip()
        if updated_task:
            self.main_text.delete(task_index)
            self.main_text.insert(task_index, updated_task)
            
            with open('data.txt', 'r') as file:
                tasks = file.readlines()

            tasks[task_index] = updated_task + '\n'
            
            with open('data.txt', 'w') as file:
                file.writelines(tasks)
                
            self.text.delete(1.0, END)
            self.button.config(text="Add", command=self.add)

    def load_tasks(self):
        try:
            with open('data.txt', 'r') as file:
                tasks = file.readlines()
            for task in tasks:
                self.main_text.insert(END, task.strip())
        except FileNotFoundError:
            open('data.txt', 'w').close()  



def main():
    root = Tk()
    ui = Todo(root)
    root.mainloop()

if __name__ == "__main__":
    main()
