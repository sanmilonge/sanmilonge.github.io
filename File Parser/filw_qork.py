import re
import time
import os
import string
def type_like_effect(text, delay=0.1):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)

cwd = f"Current working directory: {os.getcwd()}"
type_like_effect(cwd, delay = 0.02)
type_like_effect("\n---------------------------------------------------------------\n", delay = 0.02)
type_like_effect("Enter file name: ", delay=0.02)
user_input = input()
try:
    file = open(user_input, 'r')
except FileNotFoundError:
    print("File not found.")
    exit()


menu =('''------------Select an option-------------
      1-->Read file<--
      2-->Number of characters<--
      3-->Number of words<--
      4-->Number of lines<--
      5-->Find character(s)<--
      6-->Convert file<--''')

type_like_effect(menu, delay = 0.02)
action_text = "\nEnter option number: "
type_like_effect(action_text, delay = 0.02)
action = input()
if action == '1':
    type_like_effect(file.read(), delay=0.002)
elif action == '2':
    num_char = f'Number of characters: {len(file.read())}'
    type_like_effect(num_char, delay = 0.02)
elif action == '3':
   num_words = f'Number of words: {len(file.read().split())}'
   type_like_effect(num_words, delay = 0.02)
elif action == '4':
    num_lines = f'Number of lines: {len(file.readlines())}'
    type_like_effect(num_lines, delay = 0.02)
