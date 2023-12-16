import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
import os
import subprocess

def ass2csv():
    path = filedialog.askdirectory(title='Path to the directory containing the ASS files')
    out_path = filedialog.askdirectory(title='Path to the output directory')
    args = ['python', 'ass2csv.py', '--path', path, '--out_path', out_path]
    if skip_comments.get():
        args.append('--skip_comments')
    if check_wav.get():
        args.append('--check_wav')
    subprocess.run(args)

def ass2json():
    path = filedialog.askdirectory(title='Path to the directory containing the ASS files')
    out_path = filedialog.askdirectory(title='Path to the output directory')
    args = ['python', 'ass2json.py', '--path', path, '--out_path', out_path]
    if skip_comments.get():
        args.append('--skip_comments')
    subprocess.run(args)

def merge2ass():
    csv_path = filedialog.askdirectory(title='Select CSV directory')
    json_path = filedialog.askdirectory(title='Select JSON directory')
    ass_path = filedialog.askdirectory(title='Save ASS directory')
    subprocess.run(['python', 'merge2ass.py', '--csv_path', csv_path, '--json_path', json_path, '--ass_path', ass_path])

def ass2lab():
    path = filedialog.askdirectory(title='Path to the directory containing the ASS files')
    out_path = filedialog.askdirectory(title='Path to the output directory')
    args = ['python', 'ass2lab.py', '--path', path, '--out_path', out_path]
    if skip_comments.get():
        args.append('--skip_comments')
    subprocess.run(args)

root = tk.Tk()
root.title('dataset-tools mod4ass')

notebook = ttk.Notebook(root)

tab1 = tk.Frame(notebook)
button1 = tk.Button(tab1, text='trans', command=ass2csv)
button1.pack()
skip_comments = tk.IntVar(value=0)
checkbutton1 = tk.Checkbutton(tab1, text='Skip comments', variable=skip_comments)
checkbutton1.pack()
check_wav = tk.IntVar(value=0)
checkbutton2 = tk.Checkbutton(tab1, text='Check wav', variable=check_wav)
checkbutton2.pack()
notebook.add(tab1, text='ass2csv')

tab2 = tk.Frame(notebook)
button2 = tk.Button(tab2, text='trans', command=ass2json)
button2.pack()
skip_comments = tk.IntVar(value=0)
checkbutton3 = tk.Checkbutton(tab2, text='Skip comments', variable=skip_comments)
checkbutton3.pack()
notebook.add(tab2, text='ass2json')

tab3 = tk.Frame(notebook)
button3 = tk.Button(tab3, text='merge', command=merge2ass)
button3.pack()
notebook.add(tab3, text='merge2ass')

tab4 = tk.Frame(notebook)
button4 = tk.Button(tab4, text='trans', command=ass2lab)
button4.pack()
skip_comments = tk.IntVar(value=0)
checkbutton4 = tk.Checkbutton(tab4, text='Skip comments', variable=skip_comments)
checkbutton4.pack()
notebook.add(tab4, text='ass2lab')


notebook.pack()

root.mainloop()