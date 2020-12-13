from tkinter import *
from tkinter.ttk import *
from functools import partial
import os



# file global variable declaration
speedFile = open("piperWarriorVSpeeds.txt", "r")
fileString = speedFile.read()
lineList = fileString.split('\n')
spaceList = []
for i in lineList:
	if (i == ""):
		break
	spaceList.append(i.split(' '))


speedFile.close()
# spaceList:	[line][0]:	full name
#				[line][1]:	abbreviation
#				[line][2]:	speed in KTS

# global functions
def changeButtonText(x, set, type):
	if type == "fn":
		if (set[x]["text"] == "Name"):
			set[x]["text"] = spaceList[x][0].replace('_', ' ')
		else:
			set[x]["text"] = "Name"
	if type == "v":
		if (set[x]["text"] == "Speed"):
			set[x]["text"] = spaceList[x][2]
		else:
			set[x]["text"] = "Speed"

def abbrLabelsBuildPush(master):
	for i in range(11):
		tempLabel = Label(master, text = spaceList[i][1], font = "Helvetica 9 bold")
		tempLabel.grid(sticky = W, row = i, column = 0, padx = 20)

def fnButtonsBuildPush(master):
	fnSet = {}
	for i in range(0, 11):
		fnButton = Button(master, text = "Name", command = lambda x = i, set = fnSet, type = "fn": changeButtonText(x, set, type), width = 28)
		fnButton.grid(row = i, column = 1)
		fnSet[i] = fnButton

def enterEntry(master, input, x):
	if input == spaceList[x][2]:
		Label(master, text = "ye", foreground = "green").grid(row = x, column = 4)
	else:
		Label(master, text = "naah", foreground = "red").grid(row = x, column = 4)

# classes (seperate pages)
class Flashcards():
	def __init__(self, master):
		self.master = master

		abbrLabelsBuildPush(master)
		fnButtonsBuildPush(master)

		# widget declaration
		self.vSet = {}
		for i in range(11):
			self.vButton = Button(master, text = "Speed", command = lambda x = i, set = self.vSet, type = "v": changeButtonText(x, set, type), width = 7)
			self.vButton.grid(row = i, column = 3)
			self.vSet[i] = self.vButton

		self.switchButton = Button(master, text = "Flashcards", command = self.windowShift)
		self.locationLabel = Label(master, text = os.path.realpath(speedFile.name), font = 'Helvetica 9 italic')

		# widget/frame configure functionality
		master.grid_rowconfigure(12, minsize = 30)
		master.grid_rowconfigure(14, minsize = 30)

		# push widgets to root frame
		self.switchButton.grid(row = 13, column = 3)
		self.locationLabel.grid(sticky = W, row = 15, columnspan = 4)


	def windowShift(self):
		self.master.withdraw()
		topLevel = Toplevel(self.master)
		topLevel.geometry("400x390")
		topLevel.title("Written Test")
		topLevel.iconbitmap('plane.ico')
		newWin = WrittenTest(topLevel)



class WrittenTest:
	def __init__(self, master):
		self.master = master

		abbrLabelsBuildPush(master)
		fnButtonsBuildPush(master)

		# widget declaration
		self.vSet = []
		self.vEntry_1 = Entry(master, width = 3)
		self.vSet.append(self.vEntry_1)
		self.vEntry_2 = Entry(master, width = 3)
		self.vSet.append(self.vEntry_2)
		self.vEntry_3 = Entry(master, width = 3)
		self.vSet.append(self.vEntry_3)
		self.vEntry_4 = Entry(master, width = 3)
		self.vSet.append(self.vEntry_4)
		self.vEntry_5 = Entry(master, width = 3)
		self.vSet.append(self.vEntry_5)
		self.vEntry_6 = Entry(master, width = 3)
		self.vSet.append(self.vEntry_6)
		self.vEntry_7 = Entry(master, width = 3)
		self.vSet.append(self.vEntry_7)
		self.vEntry_8 = Entry(master, width = 3)
		self.vSet.append(self.vEntry_8)
		self.vEntry_9 = Entry(master, width = 3)
		self.vSet.append(self.vEntry_9)
		self.vEntry_10 = Entry(master, width = 3)
		self.vSet.append(self.vEntry_10)
		self.vEntry_11 = Entry(master, width = 3)
		self.vSet.append(self.vEntry_11)
		self.switchButton = Button(master, text = "Flashcards", command = self.windowShift)
		self.locationLabel = Label(master, text = os.path.realpath(speedFile.name), font = 'Helvetica 9 italic')

		# widget/frame configure functionality
		self.vEntry_1.bind("<Return>", (lambda event: enterEntry(master, self.vEntry_1.get(), 0)))
		self.vEntry_2.bind("<Return>", (lambda event: enterEntry(master, self.vEntry_2.get(), 1)))
		self.vEntry_3.bind("<Return>", (lambda event: enterEntry(master, self.vEntry_3.get(), 2)))
		self.vEntry_4.bind("<Return>", (lambda event: enterEntry(master, self.vEntry_4.get(), 3)))
		self.vEntry_5.bind("<Return>", (lambda event: enterEntry(master, self.vEntry_5.get(), 4)))
		self.vEntry_6.bind("<Return>", (lambda event: enterEntry(master, self.vEntry_6.get(), 5)))
		self.vEntry_7.bind("<Return>", (lambda event: enterEntry(master, self.vEntry_7.get(), 6)))
		self.vEntry_8.bind("<Return>", (lambda event: enterEntry(master, self.vEntry_8.get(), 7)))
		self.vEntry_9.bind("<Return>", (lambda event: enterEntry(master, self.vEntry_9.get(), 8)))
		self.vEntry_10.bind("<Return>", (lambda event: enterEntry(master, self.vEntry_10.get(), 9)))
		self.vEntry_11.bind("<Return>", (lambda event: enterEntry(master, self.vEntry_11.get(), 10)))
		master.grid_rowconfigure(12, minsize = 30)
		master.grid_rowconfigure(14, minsize = 30)

		# push widgets to root frame
		for i in range(11):
			self.vSet[i].grid(row = i, column = 3)
		self.switchButton.grid(row = 13, column = 3)
		self.locationLabel.grid(sticky = W, row = 15, columnspan = 4)


	def windowShift(self):
		self.master.withdraw()
		topLevel = Toplevel(self.master)
		topLevel.title("Flashcards - Piper Warrior V-Speeds")
		topLevel.iconbitmap('plane.ico')
		newWin = Flashcards(topLevel)




root = Tk()
root.style = Style()
root.style.theme_use("winnative")

# root configurations
root.title("Flashcards")
root.iconbitmap('plane.ico')

cls = Flashcards(root)

root.mainloop()
