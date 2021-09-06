from tkinter import *
from tkinter import messagebox


##########
from pydub import AudioSegment
from pydub.playback import play
song = AudioSegment.from_mp3("note.mp3")
print('playing sound using  pydub')
play(song)
###############

root = Tk()
root.title('Error WINDOW')
Label(root, text = 'Place the toplevel window over the root window\nThen, push the button and you will see that the root window is again over the toplevel').grid()

topWindow = Toplevel(root)
topWindow.title('System Error')
Label(topWindow, text = 'This button will open a messagebox but will\ndo a "focus_force()" thing on the root window').grid()
Button(topWindow, text = '[Push me !]', command = lambda: messagebox.showinfo('foo', 'bar!')).grid()

# --

root.mainloop()