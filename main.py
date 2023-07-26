import os
import shutil
import sys

def groupFilesByLanguage(folderPath):
    #  Get a list of all files in the folder
    allFiles = os.listdir(folderPath)

    for fileName in allFiles:

        if fileName[-4:] == '.txt':
            # Extract the language name from the file name
            language = fileName.split('-')[0]

            # Create sub-folder for the language, if it doesn't exist
            languageFolder = os.path.join(folderPath, language)
            if not os.path.exists(languageFolder):
                os.makedirs(languageFolder)

            # Move the file to the language sub-folder
            sourceFile = os.path.join(folderPath, fileName)
            destinationFile = os.path.join(languageFolder, fileName)
            shutil.move(sourceFile, destinationFile)



folderPath = sys.argv[1]
groupFilesByLanguage(folderPath)
