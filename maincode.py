import tkinter
from tkinter import*
from tkinter import messagebox
def maincode():
    import random, sys
    import matrix1, matrix2,  matrix3, matrix4, matrix5, matrix6, matrix7
    import pygame
    root=Tk()
    root.geometry("300x600")
    root.title("Statistics")
    check=True
    lst=[]
    while check:
        n = random.randint(1,7)
        if n == 1 and n not in lst:
            matrix1.puzzle1()
            w=Label(root, text = matrix1.stats(), font='50')
            w.pack()
            check = messagebox.askyesno("PLAY!","Congratulations! You won! Do you wish to continue?")
            lst.append(n)
        if n == 2 and n not in lst:
            matrix2.puzzle2()
            w=Label(root, text = matrix2.stats(), font='50')
            w.pack()
            check = messagebox.askyesno("PLAY!","Congratulations! You won! Do you wish to continue?")
            lst.append(n)
        if n == 3 and n not in lst:
            matrix3.puzzle3()
            w=Label(root, text = matrix3.stats(), font='50')
            w.pack()
            check = messagebox.askyesno("PLAY!","Congratulations! You won! Do you wish to continue?")
            lst.append(n)
        if n == 4 and n not in lst:
            matrix4.puzzle4()
            w=Label(root, text = matrix4.stats(), font='50')
            w.pack()
            check = messagebox.askyesno("PLAY!","Congratulations! You won! Do you wish to continue?")
            lst.append(n)
        if n == 5 and n not in lst:
            matrix5.puzzle5()
            w=Label(root, text = matrix5.stats(), font='50')
            w.pack()
            check = messagebox.askyesno("PLAY!","Congratulations! You won! Do you wish to continue?")
            lst.append(n)
        if n == 6 and n not in lst:
            matrix6.puzzle6()
            w=Label(root, text = matrix6.stats(), font='50')
            w.pack()
            check = messagebox.askyesno("PLAY!","Congratulations! You won! Do you wish to continue?")
            lst.append(n)
        if n == 7 and n not in lst:
            matrix7.puzzle7()
            w=Label(root, text = matrix7.stats(), font='50')
            w.pack()
            check = messagebox.askyesno("PLAY!","Congratulations! You won! Do you wish to continue?")
            lst.append(n)
        if len(lst) == 7:
            break
        print(lst)
    else:
        print("Thank you!")
        pygame.quit()
        sys.exit()
