# ©Alex Perathoner 21/12/2019

import pytesseract
import os
import applescript

from PIL import Image

#function by Greenstick (https://stackoverflow.com/questions/3173320/text-progress-bar-in-the-console)
def printProgressBar (iteration, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█', printEnd = "\r"):

    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print('\r%s |%s| %s%% %s' % (prefix, bar, percent, suffix), end = printEnd)
    # Print New Line on Complete
    if iteration == total: 
        print()

#function by Michael Garito (https://stackoverflow.com/questions/27759204/how-to-write-os-x-finder-comments-from-python)
def set_comment(file_path, comment_text):
    import applescript
    applescript.tell.app("Finder", f'set comment of (POSIX file "{file_path}" as alias) to "{comment_text}" as Unicode text')


print("Insert images path: ")
directory_in_str = input()

if(directory_in_str.endswith(" ")):
	directory_in_str = directory_in_str.rstrip(' ')


if(not directory_in_str.endswith("/")):
	directory_in_str = directory_in_str + "/"


directory = os.fsencode(directory_in_str)

totalCountOfFiles = 0
for file in os.listdir(directory):
	filename = os.fsdecode(file)
	if filename.endswith(".jpeg") or filename.endswith(".png") or filename.endswith(".jpg"):
		totalCountOfFiles += 1


print("Would you like to see the info for every image? y/n")
answer = input()
if(answer == "yes"):
	answer = "y"
else:
	printProgressBar(0, totalCountOfFiles, prefix = 'Progress:', suffix = 'Complete', length = 50)

i1 = 0
i2 = 0
i3 = 0

for file in os.listdir(directory):
	filename = os.fsdecode(file)
	i3+=1
	if filename.endswith(".jpeg") or filename.endswith(".png") or filename.endswith(".jpg"):
		value=Image.open(directory_in_str + filename)
		text=pytesseract.image_to_string(value,config='--tessdata-dir "/usr/local/Cellar/tesseract/4.1.0/share/tessdata"')
		#print("text present in images:",text)
		value.close()
		i2+=1
		if(text != ""):
			set_comment(directory_in_str + filename, text)
			i1+=1
		if(answer == "y"):
			print(" -- Added comment\n\"" + text + "\"\n\tto file " + directory_in_str + filename + "\n\n")
		else:
			printProgressBar(i2, totalCountOfFiles, prefix = 'Progress:', suffix = 'Complete', length = 50)



print("Added comments to " + str(i1) + " files out of " + str(i2) + " compatible files (" + str(i3) + " files in directory)")

