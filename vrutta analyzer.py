# Vrutta analyser

import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

def analyze_shloka():
    shloka = entry.get().strip()
    if not shloka:
        messagebox.showerror("Error", "Please enter a shloka")
        return
    
    indravajra = ['g','g','l','g','g','l','l','g','l','g','g']
    upendravajra = ['l','g','l','g','g','l','l','g','l','g','g']
    vamshastha = ['l','g','l','g','g','l','l','g','l','g','l','g']
    vasanthatilaka = ['g','g','l','g','l','l','l','g','l','l','g','l','g','g']
    malini = ['l','l','l','l','l','l','g','g','g','l','g','g','l','g','g']
    shardulavikriditam = ['g','g','g','l','l','g','l','g','l','l','l','g','g','g','l','g','g','l','g']
    anushtup_cond_1 = ['l','g','g','g']
    anushtup_cond_2 = ['l','g','l','g']
    
    hrs = ['a','i','u','q','L']
    dgs = ['A','I','U','Q','e','E','o','O']
    vyn = ['k','K','g','G','f','c','C','j','J','F','t','T','d','D','N','w','W','x','X','n','p','P','b','B','m','y','r','l','v','S','R','s','h']
    swr = ['a','i','u','q','L','A','I','U','Q','e','E','o','O']
    misc = ['M','H']
    
    gl_lst = []
    c = "".join(shloka.split())
    lst_shl = list(c)
    lst_shl.append('1')
    lst_shl.append('1')
    
    for n in range(len(lst_shl)-2):
        if lst_shl[n] in swr:
            if lst_shl[n] in dgs:
                x = 'g'
            elif lst_shl[n] in hrs:
                if lst_shl[n+1] in swr:
                    x = 'l'
                elif lst_shl[n+1] in misc:
                    x = 'g'
                elif lst_shl[n+1] in vyn:
                    if lst_shl[n+2] in vyn:
                        x = 'g'
                    elif lst_shl[n+2] in swr:
                        x = 'l'
                else:
                    x = 'g'
            gl_lst.append(x)
    
    guru_lagu_output.set("Guru-Laghu Pattern: " + "-".join(gl_lst))
    
    if gl_lst == indravajra:
        result.set("The vrutta is Indravajra")
    elif gl_lst == upendravajra:
        result.set("The vrutta is Upendravajra")
    elif gl_lst == vamshastha:
        result.set("The vrutta is Vamshastha")
    elif gl_lst == vasanthatilaka:
        result.set("The vrutta is Vasanthatilaka")
    elif gl_lst == malini:
        result.set("The vrutta is Malini")
    elif gl_lst == shardulavikriditam:
        result.set("The vrutta is Shardulavikriditam")
    elif len(gl_lst) >= 8 and gl_lst[4:8] == anushtup_cond_1:
        result.set("The vrutta is Anushtup (1st or 3rd pada)")
    elif len(gl_lst) >= 8 and gl_lst[4:8] == anushtup_cond_2:
        result.set("The vrutta is Anushtup (2nd or 4th pada)")
    else:
        result.set("Vrutta not identified. Please check the input.")

def clear_text():
    entry.delete(0, tk.END)
    result.set("")
    guru_lagu_output.set("")

# Create GUI window
root = tk.Tk()
root.title("Vrutta Analyzer")
root.geometry("600x450")
root.configure(bg="#f0f0f0")

frame = ttk.Frame(root, padding=20)
frame.pack(expand=True)

ttk.Label(frame, text="Enter the Shloka:", font=("Arial", 12)).pack(pady=5)
entry = ttk.Entry(frame, width=50, font=("Arial", 12))
entry.pack(pady=5)

ttk.Button(frame, text="Analyze", command=analyze_shloka).pack(pady=5)
ttk.Button(frame, text="Clear", command=clear_text).pack(pady=5)

result = tk.StringVar()
ttk.Label(frame, textvariable=result, wraplength=500, font=("Arial", 12), foreground="#FF1493").pack(pady=10)

guru_lagu_output = tk.StringVar()
ttk.Label(frame, textvariable=guru_lagu_output, wraplength=500, font=("Arial", 12), foreground="green").pack(pady=10)

root.mainloop()
# Malini :
# sarasijamanuvixXaM SEvalenApi ramyaM
# Upendravajra :
# laM maahIpAla wava SrameNa
# Vamshastha:
# namOswananwAya sahasramUrwaye

# कौतूहलं यन्त्रविधौ सुजातं
# प्रवर्धमाना मम शेमुशी च ।
# सा कल्पयामास सुसङ्गवासं
# किं नाकरोत् कल्पलतेव कक्ष्या

# kOwUhalaM yanwraviXO sujAwaM
# pravarXamAnA mama SemuSI ca
# sA kalpayAmAsa susafgavAsaM
# kiM nAkarow kalpalaweva kakRyA