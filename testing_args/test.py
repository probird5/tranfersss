import argparse
from email import parser

parser = argparse.ArgumentParser()

parser.add_argument('-p', '--print_string', type = str, help='print a mothafucken file bruh')

options = parser.parse_args()

def printing_shit(string_toprint):
    print(string_toprint)

printing_shit(options.print_string)