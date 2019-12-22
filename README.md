# CommenterPY

Python command line tool to add comments to .jpg and .png files in a given directory using OCR.

You probably have a folder with a lot of photos with names like IMG3403... not really useful if you want to be able to search them, right? And renaming them one by one isn't a good idea either as it'd take too much time!

CommenterPY scans each photo and searchs for text in it using [pytesseract](https://pypi.org/project/pytesseract/ "Pytesseract"), then adds a comment to the file with [AppleScript](https://en.wikipedia.org/wiki/AppleScript).

## Getting started
Follow these instructions to (hopefully) install a working copy of the project.
### Prerequisites
As said before CommenterPY uses

* pytesseract
* AppleScript (for Python)

You can install them with
```
pip install pytesseract
```
and 
```
pip install applescript
```

### Installing
Just download the Commenter.py file.

### How to use
Type ```python3 [path to Commenter.py file]``` in the terminal. Press enter.

You'll now be asked to insert the path to the directory where the images are stored. If you don't know the right path just drag the folder into the terminal window.

![Terminal Screenshot](/Users/alex/AppsMine/CommenterPY/Screens/pathTerminal.gif)

You can choose to *print all the info* (which is practically a debug mode). This allows you to see in real time what image CommenterPY is analyzing and what comments it has added.

If you have a lot of images I reccomend to not use this option. A progress bar will appear instead.

When every image has been analyzed and commented a final message will be sent to the user telling him the number of:

1. The commented files
2. The compatible files in the given directory (.png, .jpg, .jpeg)
3. All the files in the given directory

![Terminal Screenshot](/Users/alex/AppsMine/CommenterPY/Screens/termfinal.png)

If we now check a file in the given directory we'll se that it has a new comment!

![Info Screenshot](/Users/alex/AppsMine/CommenterPY/Screens/info.png)

This allows us to search for words in that image and find the file just using Finder:

![Finder Screenshot](/Users/alex/AppsMine/CommenterPY/Screens/search.png)

## Future Updates
The text in an image is not always important. I'm planning to develop a function to comment files using what the image represents, rather than what's written in it. For example a meme with a certain format should output the keywords of that format.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
