#!/usr/bin/env python3
"""
cover letter gui
https://likegeeks.com/python-gui-examples-tkinter-tutorial/
"""

from tkinter import *
from tkinter import messagebox
from tkinter import Scrollbar
from tkinter import filedialog


from replacecover import replace

title = "Cover Letter Auto Fill v1.0"
infile = "initsample.txt"
result = ""

def handleRunClick(details, samplecover):
	return replace(details, samplecover)


def main():

	window = Tk()
	window.title(title)
	window.geometry('500x300')

	headingLabel = Label(window, text="Thanks for using Cover Letter Auto Fill v1.0. Enjoy!", font=("Comic Sans",9))
	headingLabel.grid(column=0, row=0)

	def startRun():
		runLabel.configure(text="Generating cover letter...")
		chooseBtn.config(state="disabled")
		runBtn.config(state="disabled")

	def reset():
		runLabel.configure(text="Click 'Run' to generate cover letter")
		chooseBtn.config(state="normal")
		runBtn.config(state="normal")

	def clickSave():
		print("Save file button clicked.")
		global result
		f = filedialog.asksaveasfile(mode='w', defaultextension=".txt")
		# asksaveasfile return `None` if dialog closed with "cancel".
		if f is not None:
			text2save = str(result.get(1.0, END))
			f.write(text2save)
			f.close()

	def clickRun():
		print("Run button clicked.")
		startRun()
		global result
		global inputTxt
		defaulttitle, result = handleRunClick(inputTxt.get(), infile)
		messagebox.showinfo(title,'Done!')

		outfileLabel.configure(text=defaulttitle)
		saveBtn.config(state="normal")

		reset()

	def clickChoose():
		print("Choose File button clicked.")
		global infile
		infile = filedialog.askopenfilename(initialdir = "./",title = "Choose sample",filetypes = (("Text Files","*.txt"),("All Files","*.*")))
		fileLabel = infile.split('/')
		infileLabel.configure(text=fileLabel[-1])
		runBtn.configure(state="normal")



	runLabel = Label(window, text="Click 'Run' to generate cover letter")
	runLabel.grid(row=40)

	runBtn = Button(window, text="Run", bg="green", fg="white", command=clickRun, state="disabled")
	runBtn.grid(row=41)

	outfileLabel = Label(window, text="No file")
	outfileLabel.grid(row=50)

	saveBtn = Button(window, text="Save As", command=clickSave, state="disabled")
	saveBtn.grid(row=51)

	infileLabel = Label(window, text="No file")
	infileLabel.grid(row=24)

	chooseBtn = Button(window, text="Choose Sample Cover Letter", command=clickChoose)
	chooseBtn.grid(row=25)

	inputLabel = Label(window, text="Input format:\n<companyname>,<companyaddress>,<jobtitle>,<employmenttype>,<hiringmanager>", padx=5)
	inputLabel.grid(row=10)

	scrollbar = Scrollbar(orient="horizontal")
	inputTxt = Entry(window, width=30, xscrollcommand=scrollbar.set)
	inputTxt.grid(row=11)
	inputTxt.focus()
	scrollbar.grid(row=12, sticky="EW")
	scrollbar.config(command=inputTxt.xview)

	window.mainloop()


if __name__ == '__main__':
	main()