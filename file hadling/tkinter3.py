import tkinter as tk
root = tk.Tk()

root.title("Main Window")
root.geometry("1920x1080")

entry=tk.Text(root,height=10,width=40,font=("monotype corsiva",20))
entry.pack(pady=20)

def show_input():
    user_input=entry.get("1.0",tk.END)
    label.config(text=f"User entered:{user_input}",bg="red",fg="black")

button = tk.Button(root,text="show",command=show_input)
button.pack()

label=tk.Label(root,text="",font=20)
label.pack(pady=10)

root.mainloop()