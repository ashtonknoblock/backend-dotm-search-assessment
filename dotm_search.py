#!/usr/bin/env python
"""
Given a directory path, this searches all files in the path for a given text string 
within the 'word/document.xml' section of a MSWord .dotm file.
"""
import zipfile
import glob
import os 
import sys
import argparse
cwd = os.getcwd()

def decode_files(text, path = cwd):
    matched = 0
    total = 0
    for filename in glob.iglob('./dotm_files/*.dotm'):
        total += 1
        zf = zipfile.ZipFile(filename, 'r')
        data = zf.read('word/document.xml')
        if text in data:
            matched += 1
            keyword_index = data.index(text)
            first_40 = data[keyword_index-40:keyword_index+1]
            last_40_backwards = data[keyword_index+40:keyword_index:-1]
            last_40 = last_40_backwards[::-1]
            print
            print " In the file {}, I found a match at ...{}... ".format(filename, first_40+last_40)
            print

    print "total files SEARCHED: {}".format(total)
    print "number of files MATCHED: {}".format(matched)
    print
            
        



if __name__ == "__main__":
    text = sys.argv[1]
    if len(sys.argv) == 2:
        decode_files(text)
    elif len(sys.argv) == 3:
        new_path = sys.argv[2]
        decode_files(text, new_path)  
    else:
        print 'ERROR: please type a valid command'
        sys.exit(1)