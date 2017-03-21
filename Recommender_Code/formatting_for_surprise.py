# -*- coding: utf-8 -*-
#!/bin/python3.5

"""
Create a data file with compliance to the surprise library.
"""

import re, sys

def format_data():
  indices = []
  with open("/Users/apple/Desktop/capstone/data cleaning/test_restaurant.csv", 'r') as data_file:
    data = data_file.read().splitlines()[1:]
  indices = [ line.split(',') for line in data ]

  hundred_percent = len(indices)
  counter = 0
  with open('/Users/apple/Desktop/capstone/data cleaning/test_restaurant.data', 'w') as data_file:
    for business_id, user_id, stars_rev in indices:
      data_file.write('\t'.join([business_id, user_id, stars_rev]) + '\n')
      counter += 1
      sys.stdout.write("\rProgress: %d%%" % (int(counter/hundred_percent*100)))
      sys.stdout.flush()

if __name__ == '__main__':
  print("Formatting the file in .data for surprise to use")
  format_data()
  print("\nDone")