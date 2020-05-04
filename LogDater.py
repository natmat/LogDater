from sys import exit
import tkinter as tk
from tkinter import filedialog, messagebox

root = tk.Tk()
root.withdraw()
log_file = 'Logs/asdo-10.177.176.21.log'
# log_file = filedialog.askopenfilename(#
#     initialdir = "C:\Logs",
#     filetypes = (("log files","*.log"),("all files","*.*")))
if not log_file:
    tk.messagebox.showerror("Error", "Error: must select a log file")
    exit(1)
print("Reading data from {}".format(log_file))

# Open (in readonly) log_file file for parsing
import re
s_nums = 'one1two22three333four'
print(re.split('\d+', s_nums))

log_data = open(log_file, 'r')
for line in log_data:
    print('line: {}'.format(line))
    l = re.split('2.', line.strip())
    print("l:    {}".format(l))
    input("Press Enter to continue...")
