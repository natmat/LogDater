from sys import exit
import tkinter as tk
from tkinter import filedialog, messagebox

import sys
print('len={}'.format(len(sys.argv)))
if len(sys.argv) == 2:
    log_file = sys.argv[1]
else:
    root = tk.Tk()
    root.withdraw()
    log_file = 'Logs/asdo-10.177.176.21.log'
    log_file = 'Logs/tmp.log'
    log_file = filedialog.askopenfilename(#
        initialdir = "C:\Logs",
        filetypes = (("log files","*.log"),("all files","*.*")))
    if not log_file:
        tk.messagebox.showerror("Error", "Error: must select a log file")
        exit(1)

print("Reading data from {}".format(log_file))

# Open (in readonly) log_file file for parsing
import re

import time
from datetime import datetime
from datetime import timedelta

time_now = datetime(2020, 1, 1)
before_line = ''

log_data = open(log_file, 'r')
count = 1
for line in log_data:
    # print('[{}] line: {}'.format(count, line))
    count += 1
    [the_datetime, this_line] = re.split('[\+]', line.strip(), 1)
    datetime_object = datetime.strptime(the_datetime, '%Y-%m-%dT%H:%M:%S')
    # print('datetime_object={}'.format(datetime_object))

    diff = (datetime_object - time_now).total_seconds()
    if diff > 5:
        # print('        {} {}'.format(datetime_object, this_line))
        # print('{:06d}: {} {}'.format(count, datetime_object, before_line))
        # print('diff  = {}s'.format(time.strftime('%H:%M:%S', time.gmtime(diff))))

        # print the line number and diff (s) in CSV
        print('{},{}'.format(count, diff))
        # input("Press Enter to continue...")

    time_now = datetime_object
    before_line = this_line

    # input("Press Enter to continue...")
