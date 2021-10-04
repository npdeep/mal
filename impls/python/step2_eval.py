from mal_types import Symbol, List
import printer
import reader
import sys, traceback


repl_env = {'+': lambda a,b: a+b,
            '-': lambda a,b: a-b,
            '*': lambda a,b: a*b,
            '/': lambda a,b: int(a/b)}


def READ(x):
    return reader.read_str(x)

def eval_ast(ast, env=repl_env):
    # ast has type: MalDataType
    if isinstance(ast, Symbol):
        if ast in env:
            return env[ast]
        else:
            raise KeyError("Symbol Not Found")
    elif isinstance(ast, List):
        return List([EVAL(x) for x in ast])
    else:
        return ast


def EVAL(ast, env=repl_env):
    if isinstance(ast, List):
        if len(ast)==0:
            return ast
        proc, *args = eval_ast(ast)
        return proc(*args)
    else:
        return eval_ast(ast)

def PRINT(x):
    return printer.pr_str(x)

def rep(x: str):
    return PRINT(EVAL(READ(x)))

prompt = "user> "

while True:
    try:
        input_text = input(prompt)
        if input_text == None:
            break
        print(rep(input_text))
    except Exception as e:
        print("".join(traceback.format_exception(*sys.exc_info())))

