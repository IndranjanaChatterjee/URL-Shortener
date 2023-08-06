import tkinter

import pyshorteners

def shorten():
    short=pyshorteners.Shortener()
    short_url=short.tinyurl.short(url_entry.get())
    shorted_url.insert(0,short_url)
window=tkinter.Tk()
window.title("Url Shortener")
window.geometry('500x500')
window.configure(bg='#011638')
frame=tkinter.Frame()
frame.configure(bg='#011638')
head=tkinter.Label(frame,text="Url Shortener",font=("Arial",30),bg='#011638',fg='#DFF8EB')
Long=tkinter.Label(frame,text="Enter the Url:",font=("Arial",20),bg='#011638',fg='#DFF8EB')
url_entry=tkinter.Entry(frame,font=("Arial",15))
result=tkinter.Label(frame,text="Shorted url:",font=("Arial",20),bg='#011638',fg='#DFF8EB')
shorted_url=tkinter.Entry(frame,font=("Arial",15))

button=tkinter.Button(frame,text="Shorten it",command=shorten,font=("Arial",20),activebackground="#CDCDCD",activeforeground="#210F04")
head.grid(row=0,column=0,columnspan=2)
Long.grid(row=1,column=0,padx=20,pady=20)
url_entry.grid(row=1,column=1)
result.grid(row=2,column=0,padx=20,pady=20)
shorted_url.grid(row=2,column=1)
button.grid(row=3,column=0,columnspan=2)
frame.pack()
window.mainloop()