import printer
import reader
import sys, traceback

def READ(x):
    return reader.read_str(x)

def EVAL(x):
    return x

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

