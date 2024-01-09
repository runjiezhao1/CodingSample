import pandas as pd
import tkinter as tk
import save_button as sb

#text box size
textWidth = 10
textHeigh = 1

#initialize window
app = tk.Tk()

wrapperData = tk.LabelFrame(app)
wrapperData.pack(fill="both",expand="yes",padx=10,pady=10)

#implement data
data = pd.read_csv("username.csv")

save = tk.Button(text="Save", activebackground="pink", activeforeground="blue")
save.pack(side="bottom" ,anchor="e",padx=10,pady=5)

canvasData = tk.Canvas(wrapperData)



scrollBarData = tk.Scrollbar(wrapperData,orient="vertical",command=canvasData.yview)
scrollBarData.pack(side="right",fill="y")

scrollBarDataX = tk.Scrollbar(wrapperData,orient="horizontal",command=canvasData.xview)
scrollBarDataX.pack(side="bottom",fill="x")

canvasData.pack(side="left",fill="both",expand="yes")

canvasData.configure(yscrollcommand=scrollBarData.set)
canvasData.configure(xscrollcommand=scrollBarDataX.set)
canvasData.bind('<Configure>',lambda e: canvasData.configure(scrollregion=canvasData.bbox('all')))

myFrameData = tk.Frame(canvasData)
myFrameData.pack(fill="both",expand="yes")

canvasData.create_window((0,0),window=myFrameData,anchor="nw")

cols = list(data.columns.values)

keys = cols[0].split(";")

allKeyTexts = [0] * len(keys) 

i = 0
for key in keys:
    textBox = tk.Text(myFrameData, padx=10, pady=5, height=textHeigh, width=textWidth, font=('Sans Serif', 10, 'italic'), background="gray71")
    allKeyTexts[i] = textBox
    textBox.grid(row=0,column=i)
    textBox.insert(tk.INSERT,chars=key)
    i += 1

allValueTexts = list()
i = 0
j = 0
for index in range(data.size):
    values = list(data.iloc[index].values)
    values = values[0].split(";")
    i = 0
    curValueTexts = list()
    for val in values:
        label = tk.Text(myFrameData,pady=5,padx=10,height=textHeigh,width=textWidth,font= ('Sans Serif', 10, 'italic'))
        label.grid(row = index + 1, column= i)
        label.insert(tk.INSERT,chars=val)
        curValueTexts.append(label)
        i += 1
    allValueTexts.append(curValueTexts)

#define save file function which use
def savefile():
    sb.save_file(data=data, allKeyTexts=allKeyTexts, allValueTexts=allValueTexts)

save.configure(command=savefile)

app.title("Simple Database Management System")
app.geometry("1000x400")
app.mainloop()