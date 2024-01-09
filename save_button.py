import pandas as pd
import tkinter as tk

def save_file(data: pd.DataFrame, allKeyTexts: list[tk.Text], allValueTexts: list[list[tk.Text]]):
    index = 0
    newColumnNames = ""
    keyNames = list()
    for i in allKeyTexts:
        newColumnNames = newColumnNames + i.get("1.0",tk.END)
        newColumnNames = newColumnNames.removesuffix("\n") + ";"
        curKeyName = i.get("1.0",tk.END).removesuffix("\n")
        keyNames.append(curKeyName)
        index = index + 1
    newColumnNames = newColumnNames.removesuffix(";")
    data.columns.values[0] = newColumnNames
    print(keyNames)

    open("D:\Study\CodingExample\CodingSample\\temp.csv", "w").close()
    f = open("D:\Study\CodingExample\CodingSample\\temp.csv", "a")
    f.write(newColumnNames + "\n")

    row = 0
    for t in allValueTexts:
        col = 0
        curColumnName = ""
        for j in t:
            curColumnName = curColumnName + j.get("1.0",tk.END)
            curColumnName = curColumnName.removesuffix("\n") + ";"
            col = col + 1
        curColumnName = curColumnName.removesuffix(";")
        data.loc[row, newColumnNames] = curColumnName
        f.write(curColumnName + "\n")
        row = row + 1
    f.close()
    print(data)