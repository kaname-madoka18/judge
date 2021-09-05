import os
from os import path
import sys
from getopt import getopt

def manual_judge(resolution):
    with open(resolution, "r") as fin:
        print(fin.read())
    return float(input("input the score: "))

def test_problem(resolution ,test_files):
    with open(path.join(test_files, "__cnt.txt"), "r") as fin:
        cnt = int(fin.readline())
    for i in range(1, cnt+1):
        test_file = path.join(test_files, f"{i}.in")


def test_submit(submit, tests, points = None):
    problems = os.listdir(tests)
    total_score = 0
    if points is None:
        points = [10/len(problems)]*len(problems)
    for i, problem in enumerate(problems):
        if test_problem(path.join(submit, problem), path.join(tests, problem)):
            total_score += points[i]
        else:
            total_score += manual_judge(path.join(submit, problem))



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