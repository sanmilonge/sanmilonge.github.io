import os
import fp_func_file as fp
import time
import csv_parser as cp
'''
This program handles texts files with extensions txt, pdf, docx and doc
It parses through them to perform the following basic functions:
1-->Read file<--
2-->Total number of characters/words<--
3-->Total number of lines<--
4-->Find character/word/pattern<--
5-->Replace character/word<--
6-->Insert/delete line<--
7-->Copy file<--
8-->Get file info<--
9-->Convert file<--
10-->Sort lines<--
11-->Split or merge files<--
12-->Delete file<--
'''

def entry():
    fp.type_like_effect(f'''
    ------------------------File Parser----------------------------
    Make sure file is in the same directory/folder as programme.
    Current working directory: {os.getcwd()}
    Enter 'list' to see all files in current directory.
    Enter 'exit' to exit the programme.
    ---------------------------------------------------------------\n ''', delay = 0.002)
    while True:
        fp.type_like_effect('Enter file name: ', delay=0.02)
        try:
            global file_name
            file_name = input()
        except KeyboardInterrupt:
            fp.type_like_effect('\nExiting programme...\n', delay=0.02)
            break
        if file_name.lower() == 'list':#Lists out all files/folders in directory
            fp.type_like_effect('Files in current directory:', delay=0.02)
            for i in os.listdir():
                fp.type_like_effect(f'{i}\n', delay=0.02)
            continue
        elif file_name.lower() == 'exit':#Exits program
            fp.type_like_effect('Exiting programme...\n', delay=0.02)
            time.sleep(1)
            exit()
        else:#Runs when a fie name is entered
            try:#Exception block incase an invalid file name is entered
                global file_extension
                global file
                file_extension = fp.get_file_type(file_name)
                if file_extension == 'Text File':
                    file = open(file_name, 'r+')
                    break
                elif file_extension == 'DOCX File':
                    file = fp.read_docx(file_name)
                    break
                elif file_extension == 'PDF File':
                    file = fp.read_pdf(file_name)
                    break
                elif file_extension == 'DOC File':
                    file = fp.convert_doc_to_docx(file_name)
                    file = fp.read_docx(file)
                    break
                else:
                    file_extension = file_name.split('.')[-1]
                    if file_extension == 'csv':
                        file = fp.read_csv(file_name)
                        fp.type_like_effect('''
----------------------------Menu----------------------------
1-->Read file<--
2-->Total number of characters/words<--
3-->Replace<--
4-->Copy file<--
5-->Get file info<--
6-->Delete file<--
7-->Open new file<--
8-->Options<--
9-->Exit<--
Type 'dir' to see all files in the current directory.
---------------------------------------------------------------\n''', delay = 0.02)
                        while True:
                            option = input("Enter your choice: ")
                            if option == "1":
                                try:
                                    cp.display(file_name)
                                except Exception as e:
                                    fp.type_like_effect(f"An error occurred: {e}", delay=0.02)
                            elif option == "2":
                                cp.option_2(file_name)
                            elif option == "3":
                                cp.option_3(file_name)            
                            elif option == "4":
                                fp.copy_file(file_name)
                                fp.type_like_effect(f"File '{file_name}' copied to '{fp.new_file_name}'.", delay=0.02)
                            elif option == "5":
                                cp.display_csv_info(file_name, fp)            
                            elif option == "6":
                                fp.type_like_effect('Deleting file...', delay=0.02)
                                time.sleep(2)
                                os.remove(file_name)
                                fp.type_like_effect(f"File '{file_name}' deleted.", delay=0.02)
                            elif option  == "7":
                                thirteenth_option()
                            
                            elif option == "8":
                                cp.csv_menu()
                            elif option == "9":
                                fp.type_like_effect('Thanks you for using this program.\n', delay = 0.02)
                                time.sleep(1)
                                fp.type_like_effect('Exiting...')
                                exit()
                                break
                            elif option == "dir":
                                fp.type_like_effect('Files in current directory:', delay=0.02)
                                for i in os.listdir():
                                    fp.type_like_effect(f'{i}\n', delay=0.02)
                    else:
                        fp.type_like_effect('File type not supported.\n', delay=0.02)
                        continue
            except Exception as e:
                fp.type_like_effect(f'Error: {e}', delay=0.02)
                continue

def thirteenth_option():
    fp.type_like_effect(f'''
    ------------------------File Parser----------------------------
    Make sure file is in the same directory/folder as programme.
    Current working directory: {os.getcwd()}
    Enter 'list' to see all files in current directory.
    Enter 'exit' to exit the programme.
    ---------------------------------------------------------------\n ''', delay = 0.002)
    while True:
        fp.type_like_effect('Enter file name: ', delay=0.02)
        try:
            global file_name_2
            file_name_2 = input()
        except KeyboardInterrupt:
            fp.type_like_effect('\nExiting programme...\n', delay=0.02)
            break
        if file_name_2.lower() == 'list':#Lists out all files/folders in directory
            fp.type_like_effect('Files in current directory:', delay=0.02)
            for i in os.listdir():
                fp.type_like_effect(f'{i}\n', delay=0.02)
                continue
        elif file_name_2.lower() == 'exit':#Exits program
            fp.type_like_effect('Exiting programme...\n', delay=0.02)
            time.sleep(1)
            exit()
        else:#Runs when a fie name is entered
            try:#Exception block incase an invalid file name is entered
                global file_extension_2
                global file_2 
                try:
                    file_extension_2 = fp.get_file_type(file_name_2)
                except:
                    file_extension_2 = file_name_2.split('.')[-1]
                if file_extension_2 == 'Text File':
                    file_2 = open(file_name_2, 'r+')
                    break
                elif file_extension_2 == 'DOCX File':
                    file_2 = fp.read_docx(file_name_2)
                    break
                elif file_extension_2 == 'PDF File':
                    file_2 = fp.read_pdf(file_name_2)
                    break
                elif file_extension_2 == 'DOC File':
                    file_2 = fp.convert_doc_to_docx(file_name_2)
                    file_2 = fp.read_docx(file_2)
                    break
                elif file_extension_2 == 'csv':
                    file_2 = fp.read_csv(file_name)
                    fp.type_like_effect('''
----------------------------Menu----------------------------
1-->Read file<--
2-->Total number of characters/words<--
3-->Replace<--
4-->Copy file<--
5-->Get file info<--
6-->Delete file<--
7-->Open new file<--
8-->Options<--
9-->Exit<--
Type 'dir' to see all files in the current directory.
---------------------------------------------------------------\n''', delay = 0.02)
                    while True:
                        option = input("Enter your choice: ")
                        if option == "1":
                            try:
                                cp.display(file_name)
                            except Exception as e:
                                fp.type_like_effect(f"An error occurred: {e}", delay=0.02)
                        elif option == "2":
                            cp.option_2(file_name)
                        elif option == "3":
                            cp.option_3(file_name)            
                        elif option == "4":
                            fp.copy_file(file_name)
                            fp.type_like_effect(f"File '{file_name}' copied to '{fp.new_file_name}'.", delay=0.02)
                        elif option == "5":
                            cp.display_csv_info(file_name, fp)            
                        elif option == "6":
                            fp.type_like_effect('Deleting file...', delay=0.02)
                            time.sleep(2)
                            os.remove(file_name)
                            fp.type_like_effect(f"File '{file_name}' deleted.", delay=0.02)
                        elif option  == "7":
                            thirteenth_option()
                            
                        elif option == "8":
                            cp.csv_menu()
                        elif option == "9":
                            fp.type_like_effect('Thanks you for using this program.\n', delay = 0.02)
                            time.sleep(1)
                            fp.type_like_effect('Exiting...')
                            exit()
                            break
                        elif option == "dir":
                            fp.type_like_effect('Files in current directory:', delay=0.02)
                            for i in os.listdir():
                                fp.type_like_effect(f'{i}\n', delay=0.02)
                else:
                    fp.type_like_effect('File type not supported.\n', delay=0.02)
                    continue
            except FileNotFoundError:
                fp.type_like_effect('File not found.\n', delay=0.02)
                continue
    fp.menu()
    file_parser(file_2, file_name_2, file_extension_2)

def file_parser(file, file_name, file_extension):
    while True:
        fp.type_like_effect('Enter action (option ->11<- for options and option ->12<- to exit program): ', delay=0.02)
        action = input()
        if action == '1':#Read file
            if file_extension == 'Text File':
                file.seek(0)
                fp.type_like_effect(f'{file.read()}\n', delay=0.02)
            else:#File formats pdf and docx are stored as lists
                fp.type_like_effect(f'{file}\n', delay=0.02)
            time.sleep(1)
        elif action == '2':#Total number of characters/words
            fp.second_option(file, file_extension)
        elif action == '3':#Total number of lines
            fp.third_option(file, file_extension)
        elif action == '4':#Find character/word/pattern
            fp.fourth_option_menu()
            fp.fourth_option(file, file_extension)
        elif action == 'dir':
            fp.type_like_effect('Files in current directory: \n', delay = 0.02)
            for i in os.listdir():
                fp.type_like_effect(f'{i}\n', delay=0.002)
            continue
        elif action == '5':
            fp.fifth_option(file, file_name, file_extension)
        elif action == '6':#Copy file
            fp.sixth_option(file_name)
        elif action == '8':
            fp.eighth_option(file_name)
        elif action == '10':#Open new file
            thirteenth_option()
        elif action == '11':
            fp.menu()
            file_parser(file, file_name, file_extension)
        elif action == '7':
            fp.seventh_option(file_name)
        elif action == '9':#Delete file
            fp.type_like_effect('Deleting file...\n', delay=0.02)
            time.sleep(1)
            os.remove(file_name)
            fp.type_like_effect('File deleted successfully!\n', delay=0.02)
            time.sleep(1)
            while True:
                fp.type_like_effect('Would you like to do anything else? (y/n): ', delay=0.02)
                option = input()
                if option.lower() == 'y':
                    entry()
                    file_parser(file, file_name, file_extension)
                elif option.lower() == 'n':
                    fp.type_like_effect('Exiting programme...\n', delay=0.02)
                    time.sleep(1)
                    exit()
                else:
                    fp.type_like_effect('Invalid option.\n', delay=0.02)
                    continue          
        elif action == '12':
            fp.type_like_effect('Thanks you for using this program.\n', delay = 0.02)
            time.sleep(1)
            fp.type_like_effect('Exiting...')
            exit()
            break
        else:
            fp.type_like_effect('Invalid input...\nPlease try again.\n', delay = 0.02)
            file_parser(file,file_name, file_extension)
        fp.end()

entry()
fp.menu()#Prints options
file_parser(file, file_name, file_extension)
