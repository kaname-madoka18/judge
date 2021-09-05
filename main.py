import os
import sys
from getopt import getopt

def test_problem():
    pass

def test_submit(submit, tests, points = None):
    problems = os.listdir(tests)
    total_score = 0
    if points is None:
        points = [10/len(problems)]*len(problems)
    for problem in problems:
        if



def main():
    opts = getopt(sys.argv[1:], "hd:s", ["help", "assignments", "cases", "single"])
    cases = None
    single_test = False
    for arg, value in opts[0]:
        if arg == '-h' or arg == "--help":
            print("""usage:
    python main.py [-opts] submits
parameters:
    -h --help: display help message
    -c --cases: test cases directory
    -s --single: test one submit""")
            exit(0)
        elif arg == '-c' or arg == "--cases":
            cases = value
        elif arg == '-s' or arg == "--single":
            single_test = True
    if len(opts[1]) != 1:
        raise Exception("too few/many arguments")
    if cases is None:
        raise Exception("need argument -c[--cases]")
    submit_dir = opts[1][0]


if __name__ == "__main__":
    main()