import argparse
import time

class ObjectA:
    def __init__(self):
        print("Initializing Object A")


    def callMe(self):
        print("Call the method CallMe of ObjectA")


if __name__ == '__main__':
    for i in range(10000):
        obja = ObjectA()
        obja.callMe()
        time.sleep(0.5)

    parser = argparse.ArgumentParser(description='Short sample app')
    parser.add_argument('-a', action="store_true", default=False)
    parser.add_argument('-b', action="store", dest="b")
    parser.add_argument('-c', action="store", dest="c", type=int)
    parser.parse_args(['-a', '-bval', '-c', '3'])