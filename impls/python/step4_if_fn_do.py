from mal_types import Symbol, List
from core import ns
from env import Env
import printer
import reader
import sys, traceback

repl_env = Env(outer=None)

for k, v in ns.items():
    repl_env.set(k, v)


def READ(x):
    return reader.read_str(x)

def eval_ast(ast, env:Env):
    # ast has type: MalDataType
    if isinstance(ast, Symbol):
        return env.get(ast)
    elif isinstance(ast, List):
        return List([EVAL(x, env=env) for x in ast])
    else:
        return ast


def EVAL(ast, env:Env):
    if isinstance(ast, List):
        if len(ast)==0:
            return ast
        proc, *args = ast 
        if proc=="def!":
            second_arg = EVAL(args[1], env=env)
            env.set(args[0], second_arg)
            return second_arg
        elif proc=="let*":
            newEnv = Env(outer=env)
            # first element is a list
            for i in range(0, len(args[0]), 2):
                newEnv.set(args[0][i], EVAL(args[0][i+1], newEnv))
            return EVAL(args[1], env=newEnv)
        elif proc=="do":
            return [EVAL(x, env=env) for x in args][-1]
        elif proc=="if":
            conditional = EVAL(args[0], env=env)
            if conditional is not None and conditional is not False:
                return EVAL(args[1], env=env)
            elif len(args)==2:
                return None
            elif len(args)==3:
                return EVAL(args[2], env=env)
        elif proc=="fn*":
            # returns a function closure
            return lambda x: (EVAL(args[1], env=Env(outer=env, binds=args[0], exprs=x)))
        else:
            proc, *args = eval_ast(ast, env=env)
            return proc(args)
    else:
        return eval_ast(ast, env=env)

def PRINT(x):
    return printer.pr_str(x)

def rep(x: str):
    return PRINT(EVAL(READ(x), env=repl_env))

prompt = "user> "

while True:
    try:
        input_text = input(prompt)
        if input_text == None:
            break
        print(rep(input_text))
    except Exception as e:
        print("".join(traceback.format_exception(*sys.exc_info())))

