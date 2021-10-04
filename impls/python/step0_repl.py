

def READ(x: str):
    return x

def EVAL(x: str):
    return x

def PRINT(x: str):
    return x

def rep(x: str):
    return PRINT(EVAL(READ(x)))

prompt = "user> "

while True:
    input_text = input(prompt)
    if input_text == None:
        break
    print(rep(input_text))
