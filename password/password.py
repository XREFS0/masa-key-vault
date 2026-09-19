"""
MASA 12_Password Tools Using Python
Developer: MASA
"""

try:
    import tkinter as tk
    from tkinter import *
    from tkinter import filedialog
    import random
    import os
    import passfunctions

except ImportError:
    raise ImportError("function is not here")


def gui_input(prompt):

    root = tk.Toplevel()
    var = tk.StringVar()

    label = tk.Label(root, text=prompt)
    entry = tk.Entry(root, textvariable=var)
    label.pack(side="left", padx=(20, 0), pady=20)
    entry.pack(side="right", fill="x", padx=(0, 20), pady=20, expand=True)

    entry.bind("<Return>", lambda event: root.destroy())

    root.wait_window()

    value = var.get()
    return value


def generatesinglepass():

    displaypasswords.delete(1.0, END)
    chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@£$%^&*().,?0123456789"

    number = int("1")

    while True:
        try:
            length = int(gui_input("Please enter how long you would like each password to be (e.g. 20)"))
        except ValueError:
            print("Not a valid number")
            continue
        else:
            break

    print("\nhere are the generated password:")

    for pwd in range(number):
        password = ""
        for c in range(length):
            password += random.choice(chars)
        print(password)
    displaypasswords.insert(1.0, password)


def generatepass():
    displaypasswords.delete(1.0, END)
    chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@£$%^&*().,?0123456789"

    while True:
        try:
            number = int(
                gui_input("Please enter the number of passwords you would like to generate (e.g. 2)")
            )
        except ValueError:
            print("Not a valid number")
            continue
        else:
            break

    while True:
        try:
            length = int(gui_input("Please enter how long you would like each password to be (e.g. 20)"))
        except ValueError:
            print("Not a valid number")
            continue
        else:
            break

    print("\nhere are the generated passwords:")
    savepass = filedialog.asksaveasfilename(
        initialdir="/home",
        title="Enter save file name",
        filetypes=(("text files", "*.txt"), ("all files", "*.*")),
    )

    with open(savepass, "w") as text_file:
        for pwd in range(number):
            password = ""
            for c in range(length):
                password += random.choice(chars)
            print(password)

            text_file.writelines(password + "\n")

            displaypasswords.insert("end", password + "\n")

        displaypasswords.insert("end", "\nPassword's have been outputted to text file")


def strength():
    displaypasswords.delete(1.0, END)
    password = gui_input("Please enter password you would like to check strength of")

    def strongPassword(password):

        passfunctions.regexcompile(password)

    if passfunctions.regexcompile(password) == True:
        print("Strong Password")
        displaypasswords.insert("end", "Password is strong")
    else:
        print("This is not a strong password")
        displaypasswords.insert("end", "Password is not strong")


def multiplestrength():
    displaypasswords.delete(1.0, END)

    def strong_password(password):
        passfunctions.regexcompile(password)

    textfile = filedialog.askopenfilename(
        initialdir="/home",
        title="Select text file containing passwords",
        filetypes=(("text files", "*.txt"), ("all files", "*.*")),
    )
    with open(textfile, mode="r", encoding="utf-8") as pass_file:
        if os.stat(textfile).st_size == 0:
            print("no password in file")
        else:
            savefile = filedialog.asksaveasfilename(
                initialdir="/home",
                title="Enter save file name for pass strength results",
                filetypes=(("text files", "*.txt"), ("all files", "*.*")),
            )
            with open(savefile, "w") as strength_file:
                for line in pass_file.readlines():
                    print("\nPassword: {}".format(line.strip()), file=strength_file)
                    displaypasswords.insert("end", "\nPassword: {}".format(line.strip()))
                    if passfunctions.regexcompile(line):
                        displaypasswords.insert("end", "\nStrong Password\n")
                        print("Strong Password", file=strength_file)
                        continue
                    displaypasswords.insert("end", "\nThis is not a strong password\n")
                    print("This is not a strong password", file=strength_file)


def quit():
    root.quit()


root = tk.Tk()
root.geometry("350x350")
root.wm_title("Password Tools")
maintitle = tk.Label(root, text="Password Tools", font=("Comic Sans MS", 18))
generatesingle = tk.Button(root, text="Generate Single Password", command=generatesinglepass)
generatemulti = tk.Button(root, text="Generate Multiple Password to Text File", command=generatepass)
checkstrength = tk.Button(root, text="Check Password Strength", command=strength)
checkstrengthfromtext = tk.Button(
    root, text="Check Password Strength from Text File", command=multiplestrength
)
quit = tk.Button(root, text="Quit Program", command=quit)
outputlabel = tk.Label(root, text="Output")
displaypasswords = Text(root)
maintitle.pack()
generatesingle.pack()
generatemulti.pack()
checkstrength.pack()
checkstrengthfromtext.pack()
quit.pack()
outputlabel.pack()
displaypasswords.pack()
root.mainloop()
