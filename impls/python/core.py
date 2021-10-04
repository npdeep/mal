# namespace definition
from mal_types import List
import printer

def prn(x):
    print(printer.pr_str(x[0], print_readably=True))
    return None

ns = {
    'prn' : prn,
    'list' : List,
    'list?' : lambda args:  isinstance(args[0], List),
    'empty?' : lambda args: len(args[0])==0 if (args[0] is not None) else True,
    'count' : lambda args: len(args[0]) if (args[0] is not None) else 0,
    '=' : lambda args: args[0]==args[1],
    '>' : lambda args: args[0] > args[1],
    '<' : lambda args: args[0] < args[1],
    '>=' : lambda args: args[0] >= args[1],
    '<=' : lambda args: args[0] <= args[1],
    '+': lambda args: args[0]+args[1],
    '-': lambda args: args[0]-args[1],
    '*': lambda args: args[0]*args[1],
    '/': lambda args: int(args[0]/args[1]),}



def list(*args):
    return list(*args)