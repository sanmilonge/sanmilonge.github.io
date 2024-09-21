import time
import os
import PyPDF2
from docx import Document
import re
import spacy
# Load the spaCy English model
nlp = spacy.load("en_core_web_sm")
# Function to interpret natural language and convert to regex
def get_file_type(file_path):
    with open(file_path, 'rb') as file:
        file_signature = file.read(4)

    # Check for magic numbers
    if file_signature.startswith(b'%PDF'):
        return "PDF File"
    elif file_signature == b'\x50\x4B\x03\x04':  # DOCX starts with PK\x03\x04
        return "DOCX File"
    else:
        with open(file_path, 'rb') as file:
            content = file.read(1024)
            try:
                content.decode('utf-8')
                return "Text File"
            except UnicodeDecodeError:
                return "Unknown File Type"


def interpret_natural_language(nl_description):
    # Dictionary to map natural language to regex components
    nl_to_regex = {
        "digit": r"\d",
        "digits": r"\d+",
        "letter": r"[a-zA-Z]",
        "letters": r"[a-zA-Z]+",
        "word": r"\w+",
        "words": r"\w+",
        "space": r"\s",
        "spaces": r"\s+",
        "optional": r"?",
        "at least one": r"+",
        "zero or more": r"*",
        "start": r"^",
        "end": r"$",
        "anything": r".*",
        "number": r"\d+",
        "any character": r".",
        "lowercase letter": r"[a-z]",
        "uppercase letter": r"[A-Z]",
        "exactly": lambda x: f"{{{x}}}",
        "between": lambda x, y: f"{{{x},{y}}}",
        "or": "|",
        "and": "",
        "not": lambda x: f"[^{x}]",
        "group": "(",
        "endgroup": ")",
        "lookahead": "(?=",
        "endlookahead": ")",
        "lookbehind": "(?<=",
        "endlookbehind": ")",
        "boundary": r"\b",
        "non-boundary": r"\B"
    }
    
    # Process the description with spaCy
    doc = nlp(nl_description)
    
    regex_pattern = ""
    skip_next = False
    
    for i, token in enumerate(doc):
        if skip_next:
            skip_next = False
            continue
        
        word = token.text.lower()
        
        # Handle complex phrases and numbers
        if word == "exactly" and i + 1 < len(doc) and doc[i + 1].like_num:
            count = doc[i + 1].text
            regex_pattern += nl_to_regex["exactly"](count)
            skip_next = True
        elif word == "between" and i + 3 < len(doc) and doc[i + 1].like_num and doc[i + 3].like_num:
            min_count = doc[i + 1].text
            max_count = doc[i + 3].text
            regex_pattern += nl_to_regex["between"](min_count, max_count)
            skip_next = True
        elif word == "at" and i + 3 < len(doc) and doc[i + 1].text == "least" and doc[i + 2].like_num:
            min_count = doc[i + 2].text
            regex_pattern += f"{{{min_count},}}"
            skip_next = True
        elif word == "no" and i + 3 < len(doc) and doc[i + 1].text == "more" and doc[i + 2].text == "than" and doc[i + 3].like_num:
            max_count = doc[i + 3].text
            regex_pattern += f"{{0,{max_count}}}"
            skip_next = True
        elif word in nl_to_regex:
            if callable(nl_to_regex[word]):
                # Handle functions like "not" which require arguments
                if word == "not" and i + 1 < len(doc):
                    negated = doc[i + 1].text
                    regex_pattern += nl_to_regex[word](nl_to_regex.get(negated, re.escape(negated)))
                    skip_next = True
                else:
                    regex_pattern += nl_to_regex[word]
            else:
                regex_pattern += nl_to_regex[word]
        elif token.like_num:
            # Handle standalone numbers as exact matches
            regex_pattern += f"{{{word}}}"
        else:
            # For unrecognized words, assume they are literals or special regex operators
            if word == "group":
                regex_pattern += "("
            elif word == "endgroup":
                regex_pattern += ")"
            elif word == "lookahead":
                regex_pattern += "(?="
            elif word == "endlookahead":
                regex_pattern += ")"
            elif word == "lookbehind":
                regex_pattern += "(?<="
            elif word == "endlookbehind":
                regex_pattern += ")"
            else:
                regex_pattern += re.escape(word)

    return regex_pattern
def type_like_effect(text, delay=0.1): #Makes words appear like they are being typed
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
def first_option(file):  # Pass the file as an argument
    file.seek(0)  # Reset the file pointer to the beginning
    type_like_effect(file.read(), delay=0.002)
def second_option(file):#Displays the total number of characters or words
    type_like_effect("Total number of characters or words: ", delay=0.02)
    option = (input()).lower()
    file.seek(0)  # Reset the file pointer to the beginning
    if option == 'characters':
        file.seek(0)  
        return type_like_effect(f'Total number of characters: {len(file.read())}')
    elif option == 'words':
        file.seek(0)
        return type_like_effect(f'Total number of words: {len(file.read().split())}')
    else:
        type_like_effect("Invalid option. Please try again.\n")
        second_option(file)
def third_option(file):#Displays the total number of lines
    file.seek(0)  
    return type_like_effect(f'Total number of lines: {len(file.readlines())}')
def fourth_option_menu():
     type_like_effect('''
-----------------Please select an option-----------------
1--Total occurrence of selected word/character
2--Display lines containing selected word/character
3--Display lines not containing selected word/character
4--Menu
5--Exit
Option: ''', delay = 0.02)
def fourth_option(file):#Displays the total number of selected word/character, lines not containing selected word/character, lines matching selected pattern
         action = input()
         if action == '1':
             file.seek(0)
             type_like_effect("Enter character/word to find: ", delay=0.02)
             char_to_find = input()
             type_like_effect(f'Total occurrence of {char_to_find}: {file.read().count(char_to_find)}\n', delay = 0.02)
         elif action == '2':
             file.seek(0)
             type_like_effect("Enter character/word to find: ", delay=0.02)
             char_to_find = input()
             type_like_effect(f'Lines containing {char_to_find}: ', delay = 0.02)
             for line in file.readlines():
                 
                 if char_to_find in line:
                     file.seek(0)
                     type_like_effect(line, delay = 0.02)
                 else:
                     type_like_effect("Character/word not found in file.\n", delay = 0.02)
                     fourth_option(file)
         elif action == '3':
             file.seek(0)
             type_like_effect("Enter character/word to find: ", delay = 0.02)
             char_to_find = input()
             for line in file.readlines():
                 if char_to_find not in line:
                     type_like_effect(line, delay = 0.02)
                 else:
                     type_like_effect("Line without specified character/word not found.\n", delay = 0.02)
                     fourth_option(file)
         elif action == '4':
             file.seek(0)
             type_like_effect('Type in the pattern: ', delay = 0.02)
             pattern = input()
             regex_pattern = interpret_natural_language(pattern)
             for line in file.readlines():
                 if re.search(regex_pattern, line):
                     type_like_effect(line, delay = 0.02)
                 else:
                     type_like_effect("Pattern not found in file.\n", delay = 0.02)
                     fourth_option(file)
         if action == '5':
                 fourth_option_menu()
                 file_parser(file)
         elif action == '6':
             exit()
         else:
            type_like_effect("Invalid option. Please try again.\n", delay = 0.02)
            fourth_option(file)
def fifth_option(file):#Replaces selected word/character with new word/character
    counter = 1
    for line in file.readlines():
        file.seek(0)
        type_like_effect(f'{counter}-->{line}', delay = 0.002)
        counter += 1
    type_like_effect('Enter word/character to replace: ', delay = 0.02)
    word_to_replace = input()
    type_like_effect('Enter new word/character: ', delay = 0.02)
    new_word = input()
    type_like_effect('Would you like to replace all occurrences? (y/n): ', delay = 0.02)
    replace_all = input()
    if replace_all.lower() == 'y':
        file.seek(0)
        file_content = file.read()
        file_content = file_content.replace(word_to_replace, new_word)
        file.seek(0)
        file.write(file_content)
        file.truncate()
        type_like_effect(f'{word_to_replace} replaced with {new_word} successfully.', delay = 0.02)
    elif replace_all.lower() == 'n':
        file.seek(0)
        type_like_effect('Enter line number to replace: ', delay = 0.02)
        line_number = int(input())
        if line_number < 1 or line_number > len(file.readlines()):
            type_like_effect("Invalid line number. Please try again.\n")
            fifth_option(file)
        if (word_to_replace in file.readlines()[line_number - 1]) == False:
            type_like_effect("Word/character not found in file. Please try again.\n")
            fifth_option(file)
        if (word_to_replace in file.readlines()[line_number - 1]).count(word_to_replace) > 1:
            type_like_effect("Word/character found multiple times in file. Would you like to replace all occurrences? (y/n): ", delay = 0.02)
            ace_all = input()
            if ace_all.lower() == 'y':
                file.seek(0)
                lines = file.readlines()
                lines[line_number - 1] = lines[line_number - 1].replace(word_to_replace, new_word)
                file.seek(0)
                file.writelines(lines)
                file.truncate()
                type_like_effect(f'{word_to_replace} replaced with {new_word} successfully.\n', delay = 0.02)
            elif ace_all.lower() == 'n':
                type_like_effect('Type the number of occurrence to replace: ', delay = 0.02)
                occurrence_number = int(input())
                if occurrence_number < 1 or occurrence_number > (file.readlines()[line_number - 1].count(word_to_replace)):
                    type_like_effect("Invalid occurrence number. Please try again.\n")
                    fifth_option(file)
                lines = file.readlines()
                lines[line_number - 1] = lines[line_number - 1].replace(word_to_replace, new_word, occurrence_number)
                file.seek(0)
                file.writelines(lines)
                file.truncate()
                type_like_effect(f'{word_to_replace} replaced with {new_word} successfully.\n', delay = 0.02)
            else:
                type_like_effect("Invalid option. Please try again.\n")
                fifth_option(file)    
        file.seek(0)
        lines = file.readlines()
        lines[line_number - 1] = lines[line_number - 1].replace(word_to_replace, new_word)
        file.seek(0)
        file.writelines(lines)
        file.truncate()
        type_like_effect(f'{word_to_replace} replaced with {new_word} successfully.\n', delay = 0.02)
    else:
        type_like_effect("Invalid option. Please try again.\n")
        fifth_option(file)      
def sixth_option(file):#Inserts/delete new line
    file.seek(0)
    lines = file.readlines()
    counter = 1
    for line in lines:
        file.seek(0)
        type_like_effect(f'{counter}-->{line}', delay = 0.002)
        counter += 1
    type_like_effect('Enter line number to insert/delete: ', delay = 0.02)
    file.seek(0)
    try:
        line_number = int(input())
    except ValueError:
        type_like_effect("Invalid input. Please try again.\n")
        sixth_option(file)
    if line_number < 1 or line_number > len(lines):
        type_like_effect("Invalid line number. Please try again.\n")
        sixth_option(file)
    type_like_effect('Would you like to insert or delete a line? (i/d): ', delay = 0.02)
    action = input()
    if action.lower() == 'i': 
        type_like_effect('Enter line to insert: ', delay = 0.02)
        line_to_insert = input()
        lines.insert(line_number - 1, line_to_insert + '\n')
        file.seek(0)
        file.writelines(lines)
        file.truncate()
        type_like_effect(f'Line inserted successfully.\n', delay = 0.02)
    elif action.lower() == 'd':
        lines.pop(line_number - 1)
        file.seek(0)
        file.writelines(lines)
        file.truncate()
        type_like_effect(f'Line deleted successfully.\n', delay = 0.02)
    else:
        type_like_effect("Invalid option. Please try again.\n")
        sixth_option(file)
def seventh_option(file):#Copy file
    try:
        file.seek(0)
        file_content = file.read()
        file_name = file.name.split('.')[0] + '_copy.' + file.name.split('.')[1]
        with open(file_name, 'w') as copy_file:
            copy_file.write(file_content)
        type_like_effect(f'File copied successfully.\n', delay = 0.02)

    except:
        type_like_effect("Error reading file. Please try again.\n")
        seventh_option(file)
def eighth_option(file):#Get metadata
    file.seek(0)
    type_like_effect(f'File name: {file.name}\n', delay = 0.02)
    type_like_effect(f'File size: {os.path.getsize(file.name)} bytes\n', delay = 0.02)
    type_like_effect(f'File creation time: {time.ctime(os.path.getctime(file.name))}\n', delay = 0.02)
    type_like_effect(f'File last modified time: {time.ctime(os.path.getmtime(file.name))}\n', delay = 0.02)
    type_like_effect(f'File type: {file.name.split('.')[-1]}\n', delay = 0.02)
    type_like_effect(f'File path: {file.name}\n', delay = 0.02)
    type_like_effect(f'File encoding: {file.encoding}\n', delay = 0.02)
    type_like_effect(f'File mode: {file.mode}\n', delay = 0.02)
def ninth_option(file):#
    type_like_effect(f'File type: {get_file_type(file)}\n', delay = 0.02)


def tenth_option(file):#Sort lines/words in file
    file.seek(0)
    type_like_effect('Would you like to sort lines or words? (l/w): ', delay = 0.02)
    option = input()
    if option.lower() == 'l':
        file.seek(0)
        lines = file.readlines()
        new = lines.sort()
        type_like_effect(new, delay=0.002)
    if option.lower() == 'w':
        file.seek(0)
        lines = file.read().split()
        lines.sort()
    else:
        type_like_effect("Invalid option. Please try again.\n")
        tenth_option(file)
def eleventh_option(file):#Split/merrge files
    file.seek(0)
    type_like_effect('Would you like to split or merge files? (s/m): ', delay = 0.02)
    option = input()
    if option.lower() == 's':
        file.seek(0)
        lines = file.readlines()
        type_like_effect(len(lines), delay=0.002)
        type_like_effect('Enter number of lines per file: ', delay = 0.02)
        try:
            num_lines = int(input())
        except ValueError:
            type_like_effect("Invalid input. Please try again.\n")
            eleventh_option(file)
        files = len(lines) // num_lines
        if len(lines) % num_lines != 0:
            files += 1
        type_like_effect(f'Creating {files} files with {num_lines} lines each.\n', delay = 0.02)
        for i in range(files):
            with open(f'file_{i+1}.txt', 'w') as new_file:
                for j in range(num_lines):
                    if i * num_lines + j < len(lines):
                        new_file.write(lines[i * num_lines + j])
                        type_like_effect(f'{files} files created successfully.\n', delay = 0.02)
    elif option.lower() == 'm':
            file.seek(0)
            lines = file.readlines()
            type_like_effect(len(lines), delay=0.002)
            type_like_effect('Enter name of second file to merge: ', delay = 0.02)
            second_file_name = input()
            try:
                with open(second_file_name, 'r') as second_file:
                    second_file_lines = second_file.readlines()
            except FileNotFoundError:
                type_like_effect("File not found. Please try again.\n")
                eleventh_option(file)
            merged_lines = lines + second_file_lines
            with open('merged_file.txt', 'w') as merged_file:
                merged_file.writelines(merged_lines)
            type_like_effect('Files merged successfully.\n', delay = 0.02)
def twelfth_option(file):#Deletes file
    file.seek(0)
    type_like_effect('Are you sure you want to delete the file? (y/n): ', delay = 0.02)
    option = input()
    if option.lower() == 'y':
        file.close()
        os.remove(file.name)
        type_like_effect('File deleted successfully.\n', delay = 0.02)
    elif option.lower() == 'n':
        type_like_effect('File not deleted.\n', delay = 0.02)
def menu():
    type_like_effect('''
-------------------Select an option------------------------------
1-->Read file<--
2-->Total number of characters/words<--
3-->Total number of lines<--
4-->Find character/word/pattern<--
5-->Replace character/word<--
6-->Insert/delete line<--
7-->Copy file<--
8-->Get file info<--
9-->Convert file<--
10-->Sort<--
1-->Split or merge files<--
12-->Delete file<--
13-->Open new file<--
14-->Options<--
15-->Exit<--
Type 'dir' to see all files in the current directory.
-----------------------------------------------------------\n''', delay = 0.002)
def file_parser(file):
    while True:
        type_like_effect("Enter action: ", delay=0.02)
        action = input()
        if action == '1':#Read file
            first_option(file)     
        elif action == '2':#Total number of characters/words
            second_option(file)    
        elif action == '3':#Total number of lines
            third_option(file)
        elif action == '4':#Find character/word/pattern
            fourth_option(file)
        elif action == '5':#Replace character/word
            fifth_option(file)
        elif action == '6':#Insert/delete line
            sixth_option(file)

        elif action == '7':#Copy file
            seventh_option(file)
        
        elif action == '8':#Get file info
            eighth_option(file)
        
        elif action == '9':#Convert file
            ninth_option(file)
        
        elif action == '10':#Sort
            tenth_option(file)

        elif action == '11':#Split/merrge files
            eleventh_option(file)

        elif action == '12':#Delete file
            twelfth_option(file)
        
        elif action == '13':#Open new file
            type_like_effect("Enter file name: ", delay=0.02)
            user_input = input()
            
            try:
                file = open(user_input, 'r+')
                file_parser(file)
            except FileNotFoundError:
                type_like_effect("File not found.")
                file_parser(file)
        
        elif action == '14':#Options
            menu()
            file_parser(file)
            break
        elif action == '15':#Exit
            type_like_effect("Thank you for using this programme. Goodbye!", delay=0.02)
            file.close()
            break
        elif action == 'dir':#Show current working directory
            list_dir = os.listdir()
            type_like_effect("Files in current directory:\n", delay=0.02)
            for i in list_dir:
                type_like_effect(f"{i}\n", delay=0.02)
        else:
            type_like_effect("Invalid option. Please try again.\n")
            file_parser(file)
        type_like_effect("\nWould you like to do anything else? (y/n): ", delay=0.02)
        user_input = input()
        if user_input.lower() == 'n':
            type_like_effect("Thank you for using this programme. Goodbye!", delay=0.02)
            file.close()
            break 
    
        elif user_input.lower() == 'y':
            continue
        else:
            type_like_effect("Invalid option. Please try again.\n")
            file_parser(file)
type_like_effect(f'''
Make sure file is in the same directory/folder as programme.
Current working directory: {os.getcwd()}
Type 'list' to see all files in current directory.
---------------------------------------------------------------
''', delay = 0.002)
while True:
    type_like_effect("Enter file name: ", delay=0.02)
    user_input = input()
    if user_input.lower() == 'list':
        type_like_effect('Files in this directory:\n', delay = 0.02)
        for file in os.listdir():
            type_like_effect(f'{file}\n', delay = 0.02)
        
    else:
        try:
            file = open(user_input, 'r+')
            menu()
            type_like_effect("Enter action: ", delay=0.02)
            action = input()
            if action == '1':#Read file
                first_option(file)     
            elif action == '2':#Total number of characters/words
                second_option(file)    
            elif action == '3':#Total number of lines
                third_option(file)
            elif action == '4':#Find character/word/pattern
                fourth_option(file)
            elif action == '5':#Replace character/word
                fifth_option(file)
            elif action == '6':#Insert/delete line
                sixth_option(file)

            elif action == '7':#Copy file
                seventh_option(file)
            
            elif action == '8':#Get file info
                eighth_option(file)
            
            elif action == '9':#Convert file
                ninth_option(file)
            
            elif action == '10':#Sort
                tenth_option(file)

            elif action == '11':#Split/merrge files
                eleventh_option(file)

            elif action == '12':#Delete file
                twelfth_option(file)
            
            elif action == '13':#Open new file
                type_like_effect("Enter file name: ", delay=0.02)
                user_input = input()
                
                try:
                    file = open(user_input, 'r+')
                    file_parser(file)
                except FileNotFoundError:
                    type_like_effect("File not found.")
                    file_parser(file)
            
            elif action == '14':#Options
                menu()
                file_parser(file)
                break
            elif action == '15':#Exit
                type_like_effect("Thank you for using this programme. Goodbye!", delay=0.02)
                file.close()
                break
            elif action == 'dir':#Show current working directory
                list_dir = os.listdir()
                type_like_effect("Files in current directory:\n", delay=0.02)
                for i in list_dir:
                    type_like_effect(f"{i}\n", delay=0.02)
            else:
                type_like_effect("Invalid option. Please try again.\n")
                file_parser(file)
            type_like_effect("\nWould you like to do anything else? (y/n): ", delay=0.02)
            user_input = input()
            if user_input.lower() == 'n':
                type_like_effect("Thank you for using this programme. Goodbye!", delay=0.02)
                file.close()
                break 
        
            elif user_input.lower() == 'y':
                file_parser(file)

            else:
                type_like_effect("Invalid option. Please try again.\n")
                file_parser(file)
            
        except FileNotFoundError:
            type_like_effect("\nFile not found.")
            



