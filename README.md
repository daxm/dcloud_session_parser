# dCloud Session Parser
This little program extracts information from the SessionDetails.csv file (which is downloaded from dCloud)
to create a 'docx' file containing access instructions for each running session.

**Note:** This program is fairly rudimentary and needs you to modify the Python file for each event to customize the
output text.

# Installation
* Download the **session_parser.py** and **requirements.txt** files.
* Issue the command **pip install -r requirements.txt** and PIP will grab the necessary modules.

# Setup
* Download the **SessionDetails.csv** file from dCloud into the same directory as **session_parser.py**
* Edit the **session_parser.py** file to at least update the values for the **anyconnect_url** and **title** variables.
* (Optional) Modify the **build_document** subroutine to change the 'docx' text.

# Use
* Issue the command **python3 session_parser.py** to run the program.
* The program will create a series of 'docx' files into a folder called **ToPrint** in the same directory as the
session_parser.py file.
* Now it is up to you to print which files you want out of the ToPrint folder!
