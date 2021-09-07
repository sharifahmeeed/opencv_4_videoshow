from tkinter import *
from tkinter import messagebox


##########
# import required module
from playsound import playsound

# for playing note.mp3 file
while(1):
 playsound('note.mp3')
print('playing sound using playsound')

###############

# beep(sound=4)
# tkinter.messagebox.showwarning(title="Warning", message="Error",)

# root = Tk()
# root.title('Error WINDOW')
# Label(root,text='Error Occurred').grid()
#
#
# topWindow = Toplevel(root)
# topWindow.title('System Error')
# Label(topWindow,text='Error! Please restart').grid()
# Button(topWindow, text='[press!]', command=lambda: messagebox.showinfo('foo', 'restart!')).grid()
# beep(sound=4)
# root.mainloop()
#
# root = Tk()
# root.title('Error WINDOW')
# Label(root, text = 'Place the toplevel window over the root window\nThen, push the button and you will see that the root window is again over the toplevel').grid()
#
# topWindow = Toplevel(root)
# topWindow.title('System Error')
# Label(topWindow, text = 'This button will open a messagebox but will\ndo a "focus_force()" thing on the root window').grid()
# Button(topWindow, text = '[Push me !]', command = lambda: messagebox.showinfo('foo', 'bar!')).grid()
#
# # --
#
# root.mainloop()