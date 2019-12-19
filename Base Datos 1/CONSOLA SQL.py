from pyautogui import typewrite, hotkey


        
def Macro_2():
    hotkey('winleft','r')
    typewrite("C:\\Program Files\\PostgreSQL\\11\\scripts\\runpsql.bat")
    typewrite(["enter"], interval = 0.1)
    typewrite("201.238.213.114")
    typewrite(["enter"])
    typewrite("grupo5")
    typewrite(["enter"])
    typewrite("54321")
    typewrite(["enter"])
    typewrite("grupo5")
    typewrite(["enter"])
    typewrite("0BMxCm")
    typewrite(["enter"])

def ERROR_1252():
    hotkey("winleft","r")
    typewrite("notepad.exe")
    typewrite(["enter"], interval = 0.1)
    hotkey("ctrl","o")
    typewrite("C:\\Program Files\\PostgreSQL\\11\\scripts\\runpsql.bat")
    typewrite(["enter"])
    typewrite(["down", "enter", "up"], interval = 0.01) 
    typewrite("cmd /c chcp 1252")
    hotkey("ctrl","s")
print("Don't touch your keyboard or mouse")
Macro_2()
    
