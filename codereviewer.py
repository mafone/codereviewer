#!/usr/bin/env python
"""Multiplatform program to help programmers in fast code reviews with quality.
    Usage:
        codereviewer
            [--version| -v          ] The current version (Version 0.1.0).
            [--help   | -h          ] This help. Each option also has its own help.
            [--dir    | -d <path>   ] A path to a directory to be analyzed by codereviewer.
            [--file   | -f <path>   ] A path to a file to be analyzed by codereviewer.
            [--option | -op <option>] <fix|review|fix-review> whether you want to review-only, fix-only or both.
            [--require| -rq <file>  ] A json file containing rules for not allowed sentences and/or regular expressions.
            [--refuse | -rf <file>  ] A json file containing rules for allowed sentences and/or regular expressions.
            [--out    | -o <file>   ] A file containing the lines of code to be changed with the violations highlighted.
    
    Examples:
        Check examples/codereviewer_require.json and examples/codereviewer_refuse.json 
"""
import sys

PROGRAM_NAME = "codereviewer"
PROGRAM_VERSION = "0.1.0"
PYTHON_VERSION =  "Python " + sys.version.split(' ')[0]

if sys.platform == "linux" or sys.platform == "linux2":
    print("***Running {} {}, {} - Linux***".format(PROGRAM_NAME, PROGRAM_VERSION, PYTHON_VERSION))
elif sys.platform == "darwin":
    print("***Running  {} {} {} in OS X***".format(PROGRAM_NAME, PROGRAM_VERSION, PYTHON_VERSION))
elif sys.platform == "win32":
   print("***Running  {} {} {}  in Windows***".format(PROGRAM_NAME, PROGRAM_VERSION, PYTHON_VERSION))
else:
    print("***sys.platform {} not supported ({})***".format(sys.platform))


def parse_params():
    dir = ""
    file = ""
    option = ""
    require = ""
    refuse = ""
    output = ""
    for i in range(len(sys.argv)):
        print("###################################### " + sys.argv[i])
        if sys.argv[i] == "--dir" or sys.argv[i] == "-d":
            print("got dir")
        elif sys.argv[i] == "--file" or sys.argv[i] == "-f":
            print("got file")
        elif sys.argv[i] == "--option" or "-op":
            print("got option")
        elif sys.argv[i] == "--require" or sys.argv[i] == "-rq":
            print("got require")
        elif sys.argv[i] == "--refuse" or sys.argv[i] == "-rf":
            print("got refuse")
        elif sys.argv[i] == "--out" or sys.argv[i] == "-o":
            print("got output")
    print("done")

def main_function():
    """Function with the main logic of the application.
    """
    # No options
    if len(sys.argv) < 2:
        print("Error: No valid options, check --help")
        return False

    # Helper options
    elif len(sys.argv) == 2:
        if "-h" in sys.argv or "--help" in sys.argv:
            print("Usage: \n\
                    codereviewer \n\
                        [--version| -v          ] The current version (Version 0.1.0).\n\
                        [--help   | -h          ] This help. Each option also has its own help.\n\
                        [--dir    | -d <path>   ] A path to a directory to be analyzed by codereviewer.\n\
                        [--file   | -f <path>   ] A path to a file to be analyzed by codereviewer.\n\
                        [--option | -op <option>] <fix|review|fix-review> whether you want to review-only, fix-only or both.\n\
                        [--require| -rq <file>  ] A json file containing rules for not allowed sentences and/or regular expressions.\n\
                        [--refuse | -rf <file>  ] A json file containing rules for allowed sentences and/or regular expressions.\n\
                        [--out    | -o <file>   ] A file containing the lines of code to be changed with the violations highlighted.\n")
        elif "-v" in sys.argv or "--version" in sys.argv:
            print("VERSION: " + PROGRAM_NAME + ' ' + PROGRAM_VERSION)
        else:
            print("Error: Invalid options, check --help")
            return False
    # Review options help. From this point on, all invalid options will be ignored.
    elif len(sys.argv) == 3:
        if sys.argv[-1] in ["--help" or "-h]"]:
            print("Check help for {} option".format(sys.argv[-2])) # TODO: Add a dictionaty ot handle that
        parse_params()


    # Several options together to start the review
    else:
        parse_params()

    return True


if __name__ == '__main__':
    main_function()
