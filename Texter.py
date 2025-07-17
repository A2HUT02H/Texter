import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter import messagebox
import time
from tkinter import simpledialog

window = tk.Tk()
window.title('Texter')
window.resizable(width=True, height=False)


framemain = tk.Frame(master=window, width=70, height=50, bg="#494949") 
framemain.pack(fill=tk.BOTH)



field = tk.Text(framemain,bg="#f9f5da",font=("Arial",12))
field.pack(fill=tk.BOTH,padx=15,pady=15)



fontsize = 12

def new():
   if field.get("1.0","end").strip() == "":
      field.delete("1.0","end")
   else:
      confirm = messagebox.askyesnocancel("New","Do you want to save?")
      if confirm == True:
          save()
          window.title("Saved!")
          time.sleep(1)
          window.title("Texter")
      elif confirm == False:
          field.delete("1.0","end")

def save():
    data = field.get("1.0","end-1c")
    print(data)
    saved = open(r"data.txt","w")
    saved.write(data)
    window.title("Saved!")
    time.sleep(1)
    window.title("Texter")
    saved.close()

def opens():
    opens = fd.askopenfilename(filetypes=[("Text Files","*.txt")])
    if opens: 
      with open(opens,"r",encoding="utf-8") as file:
        content = file.read()
        field.delete("1.0","end")
        field.insert("1.0",content)
        
    window.title(opens)

def exit():
   if field.get("1.0","end").strip() == "":
      window.destroy()
   else:
      confirm = messagebox.askyesnocancel("Exit","Do you want to save before exit?")
      if confirm == True:
          save()
          window.title("Exiting...")
          time.sleep(1)
          window.title("Texter")
          window.destroy()
      elif confirm == False:
          window.destroy()
      
def red():
   framemain.config(bg="red")
   field.config(bg="pink")

def green():
   framemain.config(bg="green")
   field.config(bg="light green")

def size():
    global fontsize
    font_size = simpledialog.askinteger("Font size", "Enter font size:")
    if font_size: 
        fontsize = font_size
        field.config(font=(font_family, fontsize))  


font_family = "Arial"
def set_font(family):
    global font_family
    font_family = family 
    field.config(font=(font_family, fontsize))  
   



mainmenu = tk.Menu(window)
theme_menu = tk.Menu(mainmenu,tearoff=0)
file_menu = tk.Menu(mainmenu, tearoff=0)
font_menu = tk.Menu(mainmenu, tearoff=0)

mainmenu.add_cascade(label="File",menu=file_menu)
mainmenu.add_cascade(label="Theme",menu=theme_menu)
mainmenu.add_cascade(label="Font",menu=font_menu)

theme_menu.add_command(label="Red",command=red)
theme_menu.add_command(label="Green",command=green)
theme_menu.add_command(label="Blue",command=lambda:(framemain.config(bg="blue"),field.config(bg="powder blue")))
theme_menu.add_command(label="Yellow",command=lambda:(framemain.config(bg="yellow"),field.config(bg="light yellow")))
theme_menu.add_separator()
theme_menu.add_command(label="Default",command=lambda:(framemain.config(bg="light grey"),field.config(bg="white")))
file_menu.add_command(label="📄New    ",command=new)
file_menu.add_command(label="📂Open   ",command=opens)
file_menu.add_command(label="💾Save   ",command=save)
file_menu.add_separator()
file_menu.add_command(label="❌Exit",command=exit)

font_menu.add_command(label="Font size",command=size)
font_menu.add_separator()
font_menu.add_command(label="Arial", command=lambda: set_font("Arial"))
font_menu.add_command(label="Calibri", command=lambda: set_font("Calibri"))
font_menu.add_command(label="Segoe UI", command=lambda: set_font("Segoe UI"))
font_menu.add_command(label="Impact", command=lambda: set_font("Impact"))
font_menu.add_command(label="Courier New", command=lambda: set_font("Courier New"))
font_menu.add_command(label="Times New Roman", command=lambda: set_font("Times New Roman"))
font_menu.add_separator()
font_menu.add_command(label="Default",command=lambda: field.config(font="Arial"))
window.config(menu=mainmenu)



window.mainloop()