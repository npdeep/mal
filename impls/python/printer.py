from mal_types import *

def pr_str(x, print_readably=True):
    """
    Takes as input a Mal data structure and prints it
    """
    if x is None:
        return "nil"
    if isinstance(x, bool):
        if x:
            return "true"
        else:
            return "false"
    if isinstance(x, Number):
        return str(x)
    elif isinstance(x, Symbol):
        return x
    elif isinstance(x, List):
        return "(" + " ".join([pr_str(i) for i in x]) + ")"
    