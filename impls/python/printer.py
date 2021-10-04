def pr_str(x):
    """
    Takes as input a Mal data structure and prints it
    """
    if isinstance(x, int) or isinstance(x, float):
        return str(x)
    elif isinstance(x, str):
        return x
    elif isinstance(x, list):
         return "(" + " ".join([pr_str(i) for i in x]) + ")"