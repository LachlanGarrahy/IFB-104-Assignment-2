#-----Statement of Authorship----------------------------------------#
#
#  This is an individual assessment item for QUT's teaching unit
#  IFB104, "Building IT Systems", Semester 1, 2022.  By submitting
#  this code I agree that it represents my own work.  I am aware of
#  the University rule that a student must not act in a manner
#  which constitutes academic dishonesty as stated and explained
#  in QUT's Manual of Policies and Procedures, Section C/5.3
#  "Academic Integrity" and Section E/2.1 "Student Code of Conduct".
#
student_number = 11244682 # put your student number here as an integer
student_name   = 'Lachlan Garrahy' # put your name here as a character string
#
#  NB: Files submitted without a completed copy of this statement
#  will not be marked.  All files submitted will be subjected to
#  software plagiarism analysis using the MoSS system
#  (http://theory.stanford.edu/~aiken/moss/).
#
#--------------------------------------------------------------------#



#-----Assignment Description-----------------------------------------#
#
#  Tickets, Please!
#
#  In this assignment you will combine your knowledge of HTMl/CSS
#  mark-up languages with your skills in Python scripting, pattern
#  matching, databases and Graphical User Interface design to produce
#  a robust, interactive application that allows its user to view
#  and save data from multiple online sources.
#
#  See the client's briefings accompanying this file for full
#  details.
#
#--------------------------------------------------------------------#



#-----Initialisation Steps-------------------------------------------#
#

# Import standard Python 3 modules needed to complete this assignment.
# You should not need to use any modules other than those provided
# in a standard Python 3 installation for your solution.
#
# In particular, you may NOT use any Python modules that need to be
# downloaded and installed separately, such as "Beautiful Soup" or
# "Pillow", because the markers will not have access to such modules
# and will not be able to run your code.  Only modules that are part
# of a standard Python 3 installation may be used.

# A function for exiting the program immediately (renamed
# because "exit" is already a standard Python function).
from sys import exit as abort
from turtle import down

from html import *

# A function for opening a web document given its URL.
# [You WILL need to use this function in your solution,
# either directly or via the "download" function below.]
from urllib.request import urlopen

# Some standard Tkinter functions.  [You WILL need to use
# SOME of these functions in your solution.]  You may also
# import other widgets from the "tkinter" module, provided they
# are standard ones and don't need to be downloaded and installed
# separately.  (NB: Although you can import individual widgets
# from the "tkinter.tkk" module, DON'T import ALL of them
# using a "*" wildcard because the "tkinter.tkk" module
# includes alternative versions of standard widgets
# like "Label" which leads to confusion.)
from tkinter import *
from tkinter.scrolledtext import ScrolledText
from tkinter.ttk import Progressbar

# Functions for finding occurrences of a pattern defined
# via a regular expression.  [You do not necessarily need to
# use these functions in your solution, because the problem
# can be solved with the string "find" function, but it will
# be difficult to produce a concise and robust solution
# without using regular expressions.]
from re import *

# A function for displaying a web document in the host
# operating system's default web browser (renamed to
# distinguish it from the built-in "open" function for
# opening local files).  [You WILL need to use this function
# in your solution.]
from webbrowser import open as urldisplay

# All the standard SQLite functions.
from sqlite3 import *

# Confirm that the student has declared their authorship.
# You must NOT change any of the code below.
if not isinstance(student_number, int):
    print('\nUnable to run: No student number supplied',
          '(must be an integer)\n')
    abort()
if not isinstance(student_name, str):
    print('\nUnable to run: No student name supplied',
          '(must be a character string)\n')
    abort()

#
#--------------------------------------------------------------------#



#-----Supplied Function----------------------------------------------#
#
# Below is a function you can use in your solution if you find it
# helpful.  (You are not required to use this function, but it may
# save you some effort.)
#

# A function to download and save a web document.  The function
# returns the downloaded document as a character string and
# optionally saves it as a local file.  If the attempted download
# fails, an error message is written to the shell window and the
# special value None is returned.
#
# Parameters:
# * url - The address of the web page you want to download.
# * target_filename - Name of the file to be saved (if any).
# * filename_extension - Extension for the target file, usually
#      "html" for an HTML document or "xhtml" for an XML
#      document.
# * save_file - A file is saved only if this is True. WARNING:
#      The function will silently overwrite the target file
#      if it already exists!
# * char_set - The character set used by the web page, which is
#      usually Unicode UTF-8, although some web pages use other
#      character sets.
# * incognito - If this parameter is True the Python program will
#      try to hide its identity from the web server. This can
#      sometimes be used to prevent the server from blocking access
#      to Python programs. However we discourage using this
#      option as it is both unreliable and unethical to
#      override the wishes of the web document provider!
#
def download(url = 'http://www.wikipedia.org/',
             target_filename = 'downloaded_document',
             filename_extension = 'html',
             save_file = True,
             char_set = 'UTF-8',
             incognito = False):

    # Import the function for opening online documents and
    # the class for creating requests
    from urllib.request import urlopen, Request

    # Import an exception raised when a web server denies access
    # to a document
    from urllib.error import HTTPError

    # Import an exception raised when a web document cannot
    # be downloaded
    from urllib.error import URLError

    # Open the web document for reading
    try:
        if incognito:
            # Pretend to be a web browser instead of
            # a Python script (NOT RELIABLE OR RECOMMENDED!)
            request = Request(url)
            request.add_header('User-Agent',
                               'Mozilla/5.0 (Windows NT 10.0; Win64; x64) ' +
                               'AppleWebKit/537.36 (KHTML, like Gecko) ' +
                               'Chrome/42.0.2311.135 Safari/537.36 Edge/12.246')
            print("Warning - Request does not reveal client's true identity.")
            print("          This is both unreliable and unethical!")
            print("          Proceed at your own risk!\n")
        else:
            # Behave ethically
            request = url
        web_page = urlopen(request)
    except ValueError:
        print("Download error - Cannot find document at URL '" + url + "'\n")
        return None
    except HTTPError:
        print("Download error - Access denied to document at URL '" + url + "'\n")
        return None
    except URLError:
        print("Download error - Cannot access URL '" + url + "'\n")
        return None
    except Exception as message:
        print("Download error - Something went wrong when trying to download " + \
              "the document at URL '" + url + "'")
        print("Error message was:", message, "\n")
        return None

    # Read the contents as a character string
    try:
        web_page_contents = web_page.read().decode(char_set)
        #removes all line breaks and tabs from the outputted html
        web_page_contents = web_page_contents.replace("\n", "")
        web_page_contents = web_page_contents.replace("\t", "")
    except UnicodeDecodeError:
        print("Download error - Unable to decode document from URL '" + \
              url + "' as '" + char_set + "' characters\n")
        return None
    except Exception as message:
        print("Download error - Something went wrong when trying to decode " + \
              "the document from URL '" + url + "'")
        print("Error message was:", message, "\n")
        return None

    # Optionally write the contents to a local text file
    # (overwriting the file if it already exists!)
    if save_file:
        try:
            text_file = open(target_filename + '.' + filename_extension,
                             'w', encoding = char_set)
            text_file.write(web_page_contents)
            text_file.close()
        except Exception as message:
            print("Download error - Unable to write to file '" + \
                  target_filename + "'")
            print("Error message was:", message, "\n")

    # Return the downloaded document to the caller
    return web_page_contents

#
#--------------------------------------------------------------------#



#-----Student's Solution---------------------------------------------#
#
# Put your solution at the end of this file.
#

# To make it easy for the marker to find, use this filename
# for your ticket in Task 2B
ticket_file = 'your_ticket.html'

# Your code goes here
# Create a window
window = Tk()

# Give the window a title
window.title('Live Entertainmentenator')

#sets the general font for titles
title_font = ('Arial', 20)
#sets the general font for text
general_font = ('Arial', 15)
#sets the text box font for text
text_box_font = ('Arial', 9)
#sets the button width
button_width = 12
#sets the button height
button_height = 1
#sets the radio button width
radio_width = 15
#sets the radio button height
radio_height = 1
#sets the text box width
text_width = 55
#sets the text box height
text_height = 8
#sets the foreground colour
foreground1 = 'magenta3'
#sets the selected colour
foreground2 = 'magenta4'
#sets the background colour
background = 'cyan2'

#sets the windows background colour
window.configure(bg=background)

#sets the logo image
logo_image = PhotoImage(file="logo.gif")

# Tkinter string variable
# able to store any string value
string_variable = StringVar(window, '')

#list of error messages
error_messages = [
    "Please Select a Venue",
    "Event: No data found\nDate: No data found"
]

#placeholder function to show the event
def show_event_function():
    #checks to see if venue has been selected
    if venue_url == '':
        #outputs error message to tell ser to select a venue
        change_text(error_messages[0])
    else:
        #downloads the site data from the venue url
        site = download(url=venue_url)
        #checks to see if the url is valid
        if site != None:
            #if the url is valid calls the function to find the venue information
            event_title, event_date = get_page_data(venue_url)
            #calls the function to change the text box to the venue information
            change_text("Event: " + event_title + "\nDate: " + event_date)
        else:
            #tells the user that the site is unavaliable
            change_text(error_messages[1])

#function to display event details
def display_detials_function():
    #verifies that the url is not null
    if venue_url == '':
        #outputs error message to tell user to select a venue
        change_text(error_messages[0])
    else:
        #opens url in new tab
        urldisplay(venue_url, new=1, autoraise=True)

#placeholder function to print tickets
def print_tickets_function():
    #verifies that the url is not null
    if venue_url == '':
        #outputs error message to tell user to select a venue
        change_text(error_messages[0])
    else:
        print(venue_url)

#placeholder function to save the bookings
def save_bookings_function():
    #verifies that the url is not null
    if venue_url == '':
        #outputs error message to tell user to select a venue
        change_text(error_messages[0])
    else:
        print(venue_url)

#function to get the page data
def get_page_data(venue_url):
    #opens the document where the website data is saved
    #and converts all utf-8 characters to ascii characters
    site_data = unescape(open('downloaded_document.html', 'r').read())
    #uses the dictionary to determine which site is selected
    for (title, function) in values.items():
        if function[0] == venue_url:
            #calls the function to find the event title and event date from the website
            event_title, event_date = function[2](site_data)
            #returns the event title and event date to the original function to alter the text
            return event_title, event_date    

#function to get the data from the tivoli site
def get_tivoli_data(site_data):
    #uses the search function to find the image title and date from the tivoli site
    event_title = search('class="image-title">(.+?)\<.*', site_data).group(1)
    event_date = search('class="image-subtitle">(.+?)\<.*', site_data).group(1)
    
    #returns the event title and event date
    return event_title, event_date

def get_brisbane_data(site_data):
    #uses the search function to find the image title and date from the tivoli site
    event_title = search('name--content">(.+?)\<.*', site_data).group(1)
    event_date = search('--heavy eds-text-bm">(.+?)\<.*', site_data).group(1)
    
    #returns the event title and event date
    return event_title, event_date

def get_suncorp_data(site_data):
    #uses the search function to find the image title and date from the tivoli site
    event_title = search('class="event-title">(.+?)</h6>', site_data).group(1)
    event_date = search('class="event-date text-uppercase">(.+?)</h7>', site_data).group(1)

    #returns the event title and event date
    return event_title, event_date

#function to change the text of the text box
def change_text(text):
    #allows the text box to be edited
    event_details_textbox.configure(state=NORMAL)
    #clears the text box
    event_details_textbox.delete('1.0', END,)
    #adds the string to the text box
    event_details_textbox.insert(END, text)
    #disables the text box so users can not edit it
    event_details_textbox.configure(state=DISABLED)

#function to get the venue sites url
def get_url():
    #allows other functions to access the variable
    global venue_url
    #gets the value of the selected radiobutton
    venue_url = string_variable.get()

# Dictionary to create radio buttons
values = {"The Tivoli theatre": ['https://thetivoli.com.au/events', 0, get_tivoli_data],
          "Brisbane City": ['https://www.eventbrite.com.au/d/australia--brisbane-city/events/', 1, get_brisbane_data],
          "Suncorp Stadium": ['https://suncorpstadium.com.au/what-s-on.aspx', 2, get_suncorp_data]}

#dictionary to create option buttons
buttons = {"Show Event": [show_event_function, 0],
    "Display Details": [display_detials_function, 1],
    "Print Tickets": [print_tickets_function, 2],
    "Save Bookings": [save_bookings_function, 3]}

#frame for title and image
title_label_frame = LabelFrame(window, text='Live Entertainmentenator', font = title_font, bg=background)
title_label_frame.grid(column=0, row=0, rowspan=2, sticky=N)

#sets the image within the title label fram
logo = Label(title_label_frame, image = logo_image, background=foreground1).grid(column=0, row=0)

#sets the frame for the venues
venues_label_frame = LabelFrame(window, text='Venues', font = title_font, bg=background)
venues_label_frame.grid(column=1, row=0, sticky=N)

# loop to create each radiobutton from dictionary
for (text, radio_details) in values.items():
    Radiobutton(venues_label_frame, text=text, variable=string_variable, width=radio_width, height=radio_height, font=general_font,
    value=radio_details[0], indicator=0, selectcolor=foreground2, background=foreground1, command=get_url).grid(column=0, row=radio_details[1])

#sets the frame for the option buttons
button_label_frame = LabelFrame(window, text='Options', font = title_font, bg=background)
button_label_frame.grid(column=2, row=0, sticky=N)

#loop to create each button from dictionary
for (text, button_details) in buttons.items():
    Button(button_label_frame, text=text, width=button_width, height=button_height, font=general_font,
    background=foreground1, command=button_details[0]).grid(column=0, row=button_details[1])

#sets the frame for the text box that shows the event details
text_box_frame = LabelFrame(window, text='Chosen Event', font = title_font, bg=background)
text_box_frame.grid(column=1, row=1, columnspan=2)

#creates the event details text box
event_details_textbox = Text(text_box_frame, width = text_width, height = text_height, font = text_box_font,
borderwidth = 2, relief = 'groove', background=foreground1)
event_details_textbox.grid(column=0, row=0)
#placeholder data for the event details text box
event_details_textbox.insert(END, "Event name will appear here\n"
                                  "Event date(s) will appear here\n"
                                  ".\n"
                                  ".\n"
                                  ".\n"
                                  ".")
#stops the user from editing the text box
event_details_textbox.configure(state=DISABLED)

#calls the function to set the url to blank upon launch
get_url()

# Start the event loop to react to user inputs
window.mainloop()

