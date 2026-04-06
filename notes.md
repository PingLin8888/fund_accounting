# bnp zip file

at work, we have an operation to compress 4 files into a zip file and put it in a specific folder to share with custodian bank.
there are 3 files that are in the same floder. the 4th file is in another folder.
I want to play around at home myself to mimic the situation and how i could automate this process

##

how to automate? who executes? do we need review? configure file to take path etc?

every time the systems that are involved update, check if file extention changes. eg xlsx to xls.

You could extend it:

Add date to filename
Automatically find latest files
Move zip to shared folder
Add logging

windows os vs mac os

Windows → folder\file.xlsx
Mac/Linux → folder/file.xlsx

### questions

1 what's "os" in this case "import os"
