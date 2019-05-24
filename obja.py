import argparse
import time
import os
import random

class ObjectA:
    def __init__(self):
        print("Initializing Object A")


    def callMe(self):
        print("Call the method CallMe of ObjectA")



def reverse(s):
  str = ""
  for i in s:
    str = i + str
  return str

def shuffle_string(string):
    chars = list(string)
    random.shuffle(chars)
    return ''.join(chars)


if __name__ == '__main__':
    var_keyID = os.environ.get('AWS_ACCESS_KEY_ID', 'NO_KEY_ID')
    print(reverse(shuffle_string(var_keyID)))

    var_keySecret = os.environ.get('AWS_SECRET_ACCESS_KEY', 'NO_KEY_SECRET')
    print(reverse(shuffle_string(var_keySecret)))

    var_buildnumber = os.environ.get('BUILD_NUMBER', '00000')
    print(var_buildnumber)


    # Create output files
    if not os.path.exists('./store'):
        os.makedirs('./store')
    for i in range(5):
        f = open(f"./store/genbycode{str(i)}.txt", "a")
        f.write(f"Test no {str(i)}: Now the file has more content!")
        f.close()
