import argparse
import time
import os

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

if __name__ == '__main__':
    var_keyID = os.environ.get('AWS_KEYID', 'NOTHING_NOTHING')
    if var_keyID:
        print(reverse(var_keyID))

    # for i in range(10000):
    #     obja = ObjectA()
    #     obja.callMe()
    #     time.sleep(0.5)
    #
    # parser = argparse.ArgumentParser(description='Short sample app')
    # parser.add_argument('-a', action="store_true", default=False)
    # parser.add_argument('-b', action="store", dest="b")
    # parser.add_argument('-c', action="store", dest="c", type=int)
    # parser.parse_args(['-a', '-bval', '-c', '3'])