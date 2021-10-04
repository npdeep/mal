import re

class Reader:
    def __init__(self, tokens, position=0):
        self.tokens = tokens
        self.position = position

    def next(self):
        self.position += 1
        return self.tokens[self.position-1]

    def peek(self):
        if len(self.tokens)>self.position:
            return self.tokens[self.position]
        else:
            return None


def read_str(x):
    tokens = tokenize(x)
    return read_form(Reader(tokens))

def tokenize(str):
    tre = re.compile(r"""[\s,]*(~@|[\[\]{}()'`~^@]|"(?:[\\].|[^\\"])*"?|;.*|[^\s\[\]{}()'"`@,;]+)""");
    return [t for t in re.findall(tre, str) if t[0] != ';']

def _unescape(s):
    return s.replace('\\\\', ('\u029e')).replace('\\"', '"').replace('\\n', '\n').replace(('\u029e'), '\\')

def read_form(reader: Reader):
    token = reader.peek()
    if token == "(":
        return read_list(reader)
    elif token == ")":
        return Exception("unexpeced ')'")
    if token == "[":
        return read_list(reader, start="[", end = "]")
    elif token == "]":
        return Exception("unexpeced ']'")
    else:
        return read_atom(reader)

def read_list(reader: Reader, start="(", end=")"):
    token_list = []
    token = reader.next()
    
    if token != start:
        raise Exception("Unexpected Beginning")
    
    token = reader.peek()
    while token != end:
        if not token: raise Exception("expected ')', got EOF")
        token_list.append(read_form(reader))
        token = reader.peek()
    reader.next()
    return token_list
            

def read_atom(reader: Reader):
    token = reader.next() # Read and jump to next
    try:
        return int(token)
    except:
        return token