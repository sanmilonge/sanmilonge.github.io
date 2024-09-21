import pandas as pd
import time
import os
import fp_func_file as fp

def display(file_name):
    try:
        df = pd.read_csv(file_name)
        fp.type_like_effect(df, delay=0.02)
    except FileNotFoundError:
        fp.type_like_effect(f"File '{file_name}' not found.", delay = 0.02)
    except Exception as e:
        fp.type_like_effect(f"An error occurred: {e}", delay=0.02)

def analyze_csv(file_name, option="characters"):
    try:
        df = pd.read_csv(file_name)
        data_string = df.to_string()

        if option == "characters":
            total_characters = len(data_string)
            print(f"Total characters in the CSV: {total_characters}")
            return total_characters

        elif option == "words":
            total_words = len(data_string.split())
            print(f"Total words in the CSV: {total_words}")
            return total_words

        elif option == "cells":
            total_cells = df.size
            print(f"Total cells in the CSV: {total_cells}")
            return total_cells

        else:
            print("Invalid option. Choose 'characters', 'words', or 'cells'.")
            return None

    except FileNotFoundError:
        print(f"File '{file_name}' not found.")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def csv_menu():
    fp.type_like_effect('''
----------------------------Menu----------------------------
1-->Read file<--
2-->Total number of characters/words<--
3-->Replace<--
4-->Copy file<--
5-->Get file info<--
6-->Sort<--
7-->Delete file<--
8-->Open new file<--
9-->Options<--
10-->Exit<--
Type 'dir' to see all files in the current directory.
---------------------------------------------------------------\n''', delay = 0.02)
def option_2(file_name):
    options = ["characters", "words", "cells"]
    fp.type_like_effect("Enter 'characters', 'words' or 'cells': ", delay=0.02)
    option = input()
    if option in options:
        analyze_csv(file_name, option)
    else:
        fp.type_like_effect("Invalid option. Choose 'characters', 'words', or 'cells'.", delay=0.02)
        option_2(file_name)



def replace_in_csv(input_file, output_file, old_text, new_text):    
    df = pd.read_csv(input_file)
    df.replace(old_text, new_text, inplace=True)
    df.to_csv(output_file, index=False)
    
    fp.type_like_effect(f"Replacements completed. The updated CSV has been saved to {output_file}.", delay = 0.02)

def option_3(file_name):
    fp.type_like_effect("Enter the text you would like to replace: ", delay=0.02)
    old_text = input()
    fp.type_like_effect("Enter the text you would like to replace it with: ", delay=0.02)
    new_text = input()
    new_csv_file = f'{old_text}_replacedcsv'
    try:
        replace_in_csv(file_name, new_csv_file, old_text, new_text)
    except Exception as e:
        fp.type_like_effect(f"An error occurred: {e}", delay=0.02)
        option_3(file_name)


def display_csv_info(file_name, fp):
    df = pd.read_csv(file_name)
    fp.type_like_effect(f"File name: {file_name}\n", delay=0.02)
    fp.type_like_effect(f"Number of Rows: {len(df)}\n", delay=0.02)
    fp.type_like_effect(f"Number of Columns: {len(df.columns)}\n", delay=0.02)
    fp.type_like_effect("Columns:\n", delay=0.02)
    for column in df.columns:
        fp.type_like_effect(f" - {column}\n", delay=0.02)
    fp.type_like_effect("\nColumn Data Types:\n", delay=0.02)
    for column, dtype in df.dtypes.items():
        fp.type_like_effect(f" - {column}: {dtype}\n", delay=0.02)
    fp.type_like_effect("\nFirst 5 Rows of Data:\n", delay=0.02)
    fp.type_like_effect(df.head().to_string(index=False) + "\n", delay=0.02)
