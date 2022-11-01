#will pull data from directory & we'll be opening text
import os
#will pull a class that has weighted-font.
from color_class import color

def createfile(x):
    try:
        #Will change into a certain directory to create a file.
        os.chdir('/Users/giovanni/PycharmProjects/random_texts')
        file = open(x,"x")
        print("done")
    except:
        print("Error. Not valid")

def writeinfile(filename, text):
    file = open(filename, "a")
    file.write(text)
    file.close()

def readfile(filename):
    file = open(filename,"r")
    print(file.read())



while True:
    try:
        option = int(input("NOTE: Type 1,2,3. "
                   "\nOPTION 1: Create New file "
                   "\nOPTION 2: Write in your file "
                   "\nOPTION 3: Read file "
                   "\nYour choice: \n"))
    except:
        print(color.BOLD,"\n\nEnter an integer.\n",color.END)
        continue

    if option == 1:
        option1_res = input("Would you like to create a file? ")
        option1_res = option1_res.lower()
        if option1_res == "yes":
            #Giving a notice that files cannot have the same name.
            print("NOTE: You cannot create a file with the same name."
                  "Here is a list of the current files in the directory.")
            #Changes the directory, and prints out all files in that folder.
            new_dir = os.chdir('/Users/giovanni/PycharmProjects/random_texts')
            print(os.listdir(new_dir))
            #Create & Name file
            filename = input("what would you like to name the file? ")
            creation = createfile(filename)
            continue
        elif option1_res =="no":
            continue

    elif option == 2:
        option2_res = input("Do you want to write in a file? ")
        option2_res = option2_res.lower()
        if option2_res == "yes":
            # Changes the directory, and prints out all files in that folder.
            new_dir = os.chdir('/Users/giovanni/PycharmProjects/random_texts')
            print(os.listdir(new_dir))
            file_to_func = str(input("What file would you like to open? "))
            res_to_func = str(input("What would you like to type?\n "))
            writeinfile(file_to_func, res_to_func)
            openfile = open(file_to_func, "r")
            print(openfile.read())
            break
        elif option2_res == "no":
            continue

    elif option == 3:
        option3_res = input("Do you want to read a file? ")
        option3_res = option3_res.lower()
        if option3_res == "yes":
            # Changes the directory, and prints out all files in that folder.
            new_dir = os.chdir('/Users/giovanni/PycharmProjects/random_texts')
            print(os.listdir(new_dir))
            file_chosen = input("What file would you like to open? ")
            readfile(file_chosen)
            break
        elif option3_res == "no":
            continue
    else:
        #Will bold the text
        print(color.BOLD, "\n\nChoose one of the three options. \n", color.END)




