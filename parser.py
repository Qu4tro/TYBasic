import re
from pyPEG import parse
import pyPEG
import sys
import fileinput


# pyPEG:
#                    0: following element is optional
#                   -1: following element can be omitted or repeated endless
#                   -2: following element is required and can be repeated endless

def program():
    return -2, line

def line():
    return ":", 0, [statement, expression]

def statement():
    return [assignment]

def number():
    return re.compile(r'-?(\d*\.\d*|\d+|".+?")')

def variable():
    return re.compile(r'[A-Z]')

def expression():
    return [number, variable, operation, ("(", expression, ")")]

def expr():
    return [number, variable, ("(", expression, ")")]

def assignment():
    return expression, '->', variable

def operator():
    return re.compile(r"\+|-|\*|/|\^")

def operation():
    return expr, operator, expr

pyPEG.print_trace = True

files = fileinput.input()
result = parse(program(), files)
print result

