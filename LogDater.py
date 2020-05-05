from sys import exit
import tkinter as tk
from tkinter import filedialog, messagebox

'''
Function to open file chooser and prompt user to enter log file
returns the opened log file, or exits
'''
def openFileChooser():
    root = tk.Tk()
    root.withdraw()
    file = 'Logs/asdo-10.177.176.21.log'
    file = 'Logs/tmp.log'
    file = filedialog.askopenfilename(#
        initialdir = "C:\Logs",
        filetypes = (("log files","*.log"),("all files","*.*")))
    if not file:
        tk.messagebox.showerror("Error", "Error: must select a log file")
        exit(1)
    return file

'''
Usage: LogDater [logfile]...
Use either the cmd ine arg file, or open file chooser
'''
import sys
print('len={}'.format(len(sys.argv)))
if len(sys.argv) == 2:
    log_file = sys.argv[1]
else:
    log_file = openFileChooser()

print("Reading data from {}".format(log_file))

import re
import time
from datetime import datetime
from datetime import timedelta

time_now = datetime(2020, 1, 1)
previous_line = ''
max_interval = 5 # If inter-line delay > max_interval, report the diff

# Open (in readonly) log_file file for parsing
log_data = open(log_file, 'r')
line = 1
for line in log_data:
    # print('[{}] line: {}'.format(count, line))
    [the_datetime, this_line] = re.split('[\+]', line.strip(), 1)
    datetime_object = datetime.strptime(the_datetime, '%Y-%m-%dT%H:%M:%S')
    # print('datetime_object={}'.format(datetime_object))

    diff = (datetime_object - time_now).total_seconds()
    if diff > max_interval:
        # print('        {} {}'.format(datetime_object, this_line))
        # print('{:06d}: {} {}'.format(count, datetime_object, before_line))
        # print('diff  = {}s'.format(time.strftime('%H:%M:%S', time.gmtime(diff))))

        # print the line number and diff (s) in CSV
        print('{},{}'.format(line, diff))
        # input("Press Enter to continue...")

    time_now = datetime_object
    previous_line = this_line
    line += 1

    # input("Press Enter to continue...")
