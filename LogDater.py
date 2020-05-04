from sys import exit
import tkinter as tk
from tkinter import filedialog, messagebox

root = tk.Tk()
root.withdraw()
log_file = 'Logs/asdo-10.177.176.21.log'
log_file = 'Logs/tmp.log'
# log_file = filedialog.askopenfilename(#
#     initialdir = "C:\Logs",
#     filetypes = (("log files","*.log"),("all files","*.*")))
if not log_file:
    tk.messagebox.showerror("Error", "Error: must select a log file")
    exit(1)
print("Reading data from {}".format(log_file))

# Open (in readonly) log_file file for parsing
import re

from datetime import datetime
from datetime import timedelta

time_now = datetime(0)

log_data = open(log_file, 'r')
for line in log_data:
    print('line: {}'.format(line))
    [the_datetime, rest] = re.split('[\+]', line.strip(), 1)
    print('the_datetime={}'.format(the_datetime))

    datetime_object = datetime.strptime(the_datetime, '%Y-%m-%dT%H:%M:%S')
    print('datertime_object={}'.format(datetime_object))

    diff = (datetime_object - time_now).total_seconds()
    print('diff={}'.format(diff))
    time_now = datetime_object

    input("Press Enter to continue...")
