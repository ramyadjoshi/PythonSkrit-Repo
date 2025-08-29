import tkinter as tk
from tkinter import messagebox

def process_sandhi():
    word1 = entry1.get().strip()
    word2 = entry2.get().strip()
    
    if not word1 or not word2:
        messagebox.showerror("Error", "Please enter both words")
        return
    
    ik = ['i','I','u','U','q','Q','L']
    ac = ['a','i','u','q','L','A','I','U','Q','e','E','o','O']
    ec = ['e','E','o','O']
    a_lst = ['a','A']
    e_lst = ['e','E']
    o_lst = ['o','O']
    q_lst = ['q','Q']
    i_lst = ['i','I']
    u_lst = ['u','U']
    
    result = ""
    
    # Savarna Deergha Sandhi
    if word1[-1] in a_lst and word2[0] in a_lst:
        result = word1[:-1] + 'A' + word2[1:]
        sandhi_type = "Savarna Deergha Sandhi"
    elif word1[-1] in i_lst and word2[0] in i_lst:
        result = word1[:-1] + 'I' + word2[1:]
        sandhi_type = "Savarna Deergha Sandhi"
    elif word1[-1] in u_lst and word2[0] in u_lst:
        result = word1[:-1] + 'U' + word2[1:]
        sandhi_type = "Savarna Deergha Sandhi"
    elif word1[-1] in q_lst and word2[0] in q_lst:
        result = word1[:-1] + 'Q' + word2[1:]
        sandhi_type = "Savarna Deergha Sandhi"
    
    # Poorvarupa Sandhi
    elif word1[-1] == 'e' and word2[0] == 'a':
        result = word1[:-1] + 'e' + word2[1:]
        sandhi_type = "Poorvarupa Sandhi"
    elif word1[-1] == 'o' and word2[0] == 'a':
        result = word1[:-1] + 'o' + word2[1:]
        sandhi_type = "Poorvarupa Sandhi"
    
    # Yana Sandhi
    elif word1[-1] in ik and word2[0] in ac:
        replace_dict = {'i': 'y', 'I': 'y', 'u': 'v', 'U': 'v', 'q': 'r', 'Q': 'r', 'L': 'l'}
        result = word1[:-1] + replace_dict.get(word1[-1], '') + word2
        sandhi_type = "Yan Sandhi"
    
    # Yanadesha Sandhi
    elif word1[-1] in ec and word2[0] in ac:
        replace_dict = {'e': 'ay', 'E': 'Ay', 'o': 'av', 'O': 'Av'}
        result = word1[:-1] + replace_dict.get(word1[-1], '') + word2
        sandhi_type = "Yanadesha Sandhi"
    
    # Guna Sandhi
    elif (word1[-1] in a_lst) and (word2[0] in ik):
        replace_dict = {'i': 'e', 'I': 'e', 'u': 'o', 'U': 'o', 'q': 'ar', 'Q': 'ar', 'L': 'al'}
        result = word1[:-1] + replace_dict.get(word2[0], '') + word2[1:]
        sandhi_type = "Guna Sandhi"
    
    # Vruddhi Sandhi
    elif word1[-1] in a_lst:
        replace_dict = {'e': 'E', 'E': 'E', 'o': 'O', 'O': 'O', 'q': 'Ar', 'Q': 'Ar', 'L': 'Al'}
        result = word1[:-1] + replace_dict.get(word2[0], '') + word2[1:]
        sandhi_type = "Vruddhi Sandhi"
    
    else:
        sandhi_type = "No Sandhi applicable"
        result = word1 + word2
    
    result_label.config(text=f"{sandhi_type}: {result}")

# Creating GUI
root = tk.Tk()
root.title("अच् Sandhi Processor")
root.geometry("400x300")

# Labels and Entry Fields
tk.Label(root, text="Word 1:").pack(pady=5)
entry1 = tk.Entry(root)
entry1.pack(pady=5)

tk.Label(root, text="Word 2:").pack(pady=5)
entry2 = tk.Entry(root)
entry2.pack(pady=5)

# Process Button
process_btn = tk.Button(root, text="Process Sandhi", command=process_sandhi)
process_btn.pack(pady=10)

# Result Label
result_label = tk.Label(root, text="", fg="blue")
result_label.pack(pady=10)

# Run GUI
root.mainloop()
# Yan sandhi:

# L + AkqwiH
# XAwq + amSah
# suXI + upAsyaH
# maXu + ariH

# Yaantavantaadesha: 

# hare + AgacCa
# guro + AdiSa
# xasyE + ixam
# bAlakO + AgatO

# Guna:
# xeva + inxraH
# sUrya + uxayaH

# Vruddhi:

# eka + ekam
# gafgA + oGaH

# Savarna deergha:
# giri + ISaH
# vixyA + Ala yah
# piwR + RNam