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
if len(sys.argv) == 2:
    log_file = sys.argv[1]
else:
    log_file = openFileChooser()

print("Reading data from {}".format(log_file))

import re
import time
from datetime import datetime
from datetime import timedelta

# If inter-line delay > max_interval, report the diff
max_interval = 5

# Open (in readonly) log_file file for parsing
log_data = open(log_file, 'r')
output_log_data = open(log_file +'.csv', 'w')
line_number = 1
log_file_date_time_format = '%Y-%m-%dT%H:%M:%S'

[time_now_object, rest_of_line] = re.split('[\+]', log_data.readline().strip(), 1)
prev_datetime = datetime.strptime(time_now_object, log_file_date_time_format)
start_time = prev_datetime
# time_now = datetime(2020, 1, 1)

log_data.seek(0)

for line in log_data:
    # print('[{}] line: {}'.format(count, line))
    [the_datetime, this_line] = re.split('[\+]', line.strip(), 1)
    current_datetime = datetime.strptime(the_datetime, log_file_date_time_format)
    # print('datetime_object={}'.format(datetime_object))

    diff = (current_datetime - prev_datetime).total_seconds()
    if diff > max_interval:
        print('        {} {}'.format(current_datetime, this_line))
        print('{:06d}: {} {}'.format(line_number, prev_datetime, previous_line))
        # print('diff  = {}s'.format(time.strftime('%H:%M:%S', time.gmtime(diff))))

        # print the line number and diff (s) in CSV
        run_time = (current_datetime - start_time).total_seconds()
        print('{},{},{}'.format(line_number, run_time,diff))
        output_log_data.writelines('{},{},{}\n'.format(line_number, run_time,diff))
        # input("Press Enter to continue...")

    prev_datetime = current_datetime
    previous_line = this_line
    line_number += 1

    # input("Press Enter to continue...")

output_log_data.close()