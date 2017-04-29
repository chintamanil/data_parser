#!/usr/bin/env python
#-*- coding: utf-8 -*-

u"""
JSON Parser: Parse the json data from input file to get correct entries for user
with first name last name phone number and color.
"""
import argparse, json
import re, time
from string import whitespace
import sys
import glob, os
os.chdir('./')
# 'segment*' are files after using 'split -l [N] file segment' command
'TODO: Idea is to run the main function in threads for each segent file.'
for file_name in glob.glob('segment*'):
    print(file_name)

def timing_decorator(decorated_func):
    """Decorator with times the function run time"""
    def wrapper(*args):
        """Wrapper for time executions """
        start = time.time()
        res = decorated_func(*args)  # Call the real function
        elapsed = time.time() - start
        print "Execution of '{0}{1}' took {2} seconds".format(decorated_func.__name__, args, elapsed)
        return res
    return wrapper

def file_check(fn):
    """Check if file is valid"""
    try:
        fd = open(fn, 'r')
    except IOError:
        print "Error: File does not appear to exist."
        sys.exit()
    else:
        return fd

def read_stripped_file_lines(f):
    """Generator which reads lines from a file and strips them"""
    for file_line in f:
        yield file_line.strip(whitespace)

def split_lines_in_words(lines_to_split):
    """Generator which splits incoming iterable's lines into words """
    for line in lines_to_split:
        yield line.split(',')

def name_parser(first_name, last_name, isCombined=False):
    """parses the name and returns first and last name """
    if isCombined:
        first_name, last_name = first_name.rsplit(' ' , 1)
    return first_name.strip(whitespace), last_name.strip(whitespace)

def parse_phone_number(phone_number):
    """parses the phone number for correct format
    and returns parsed phone number """
    phone_number = re.sub('[ ()-]', '', phone_number)
    if len(phone_number) == 10 and not bool(re.search(r'[^\d]', phone_number)):
        formatted_number = []
        for index, number in enumerate(phone_number):
            if index == 3 or index == 6:
                formatted_number.append('-')
            formatted_number.append(number)
        return ''.join(formatted_number)
    else:
        return False

def parse_zipcode(zipcode):
    """Checks zipcode for validity and returns parsed zipcode or False """
    zipcode = zipcode.strip(' ')
    return zipcode if len(zipcode) == 5 and  bool(re.search(r'^\d', zipcode)) else False

def parse_color(color):
    """Checks if color is valid (length and dosent contain numbers)
    and returns parsed color """
    'TODO: Check color with predefined list of colors from python library'
    color = color.strip(whitespace)
    return color if len(color) >= 3 and not bool(re.search(r'\d', color)) else False

def parse_words_array(words_array):
    """words array is the content of line
    this function runs the check on the array elemets for validity
    of color, name, zipcode """
    len_words_array = len(words_array)
    if len_words_array == 4:
        first_name, last_name = name_parser(words_array[0], words_array[1], True)
        zipcode = parse_zipcode(words_array[2])
        phone_number = parse_phone_number(words_array[3])
        color = parse_color(words_array[1])
    elif len_words_array == 5:
        color = parse_color(words_array[3])
        if color:
            first_name, last_name = name_parser(words_array[1] , words_array[0], False)
            zipcode = parse_zipcode(words_array[4])
            phone_number = parse_phone_number(words_array[2])
        else:
            first_name, last_name = name_parser(words_array[0] , words_array[1], False)
            color = parse_color(words_array[4])
            zipcode = parse_zipcode(words_array[2])
            phone_number = parse_phone_number(words_array[3])
    else:
        return False
    parsed_object = {}
    for each in ['color', 'first_name', 'last_name', 'zipcode', 'phone_number']:
        parsed_object[each] = eval(each)
    check = True
    for each in parsed_object:
        check = False if parsed_object[each] == False else check
    return parsed_object if check == True else False

@timing_decorator
def main():
    """Main function that parses the file and checks validity """
    parser = argparse.ArgumentParser(description='File to Open')
    parser.add_argument('file', help='open this file')
    args = parser.parse_args()
    f = file_check(args.file)
    line_number = 0
    stripped_lines = read_stripped_file_lines(f)
    words_in_line = split_lines_in_words(stripped_lines)
    errors, entries = ([] for i in range(2))
    for word_array in words_in_line:
        parsed = parse_words_array(word_array)
        entries.append(parsed) if parsed else errors.append(line_number)
        line_number += 1
    entries = sorted(entries, key = lambda x: (x['last_name'], x['first_name']))
    json_data = {}
    json_data.update({'entries': entries, 'errors': errors})
    with open('result.out', 'w') as outfile:
        json.dump(json_data, outfile,  sort_keys=True, indent=2, separators=(',', ': '))

if __name__ == "__main__":
    main()
