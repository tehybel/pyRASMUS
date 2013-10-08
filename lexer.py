TK_ERR = 255
TK_EOF = 254
TK_TUP = 1
TK_REL = 2
TK_FUNC = 3
TK_END = 4
TK_AT = 5
TK_SHARP = 6
TK_NOT = 7
TK_MINUS = 8
TK_AND = 9
TK_OR = 10  
TK_TRUE = 11
TK_FALSE = 12
TK_LPAREN = 13
TK_RPAREN = 14
TK_BLOCKSTART = 15
TK_BLOCKEND = 16
TK_VAL = 17
TK_IN = 18
TK_NAME = 19
TK_COLON = 20
TK_INT = 21
TK_TEXT = 22
TK_ZERO = 23
TK_ONE = 24
TK_STDBOOL = 25
TK_STDINT = 26
TK_STDTEXT = 27
TK_COMMA = 28
TK_FUNC = 29
TK_END = 30
TK_RIGHTARROW = 31
TK_TYPE_BOOL = 32
TK_TYPE_INT = 33
TK_TYPE_TEXT = 34
TK_TYPE_ATOM = 35
TK_TYPE_TUP = 36
TK_TYPE_REL = 37
TK_TYPE_FUNC = 38
TK_TYPE_ANY = 39
TK_EQUAL = 40
TK_ASSIGN = 41
TK_PLUS = 42
TK_MUL = 43
TK_DIV = 44
TK_MOD = 45
TK_SEMICOLON = 46
TK_CONCAT = 47
TK_PIPE = 48
TK_OPEXTEND = 49
TK_LESS = 50
TK_GREATER = 51
TK_DIFFERENT = 52
TK_LESSEQUAL = 53
TK_GREATEREQUAL = 54
TK_TWO_DOTS = 55
TK_ONE_DOT = 56
TK_QUESTION = 57
TK_SET_MINUS = 58
TK_PROJECT_PLUS = 59
TK_PROJECT_MINUS = 60
TK_LEFT_ARROW = 61
TK_LBRACKET = 62
TK_RBRACKET = 63
TK_MAX = 64
TK_MIN = 65
TK_COUNT = 66
TK_ADD = 67
TK_MULT = 68
TK_DAYS = 69
TK_BEFORE = 70
TK_AFTER = 71
TK_TODAY = 72
TK_DATE = 73
TK_OPEN = 74
TK_CLOSE = 75
TK_WRITE = 76
TK_SYSTEM = 77
TK_IF = 78
TK_FI = 79
TK_CHOICE = 81
TK_ISBOOL = 82
TK_ISINT = 83
TK_ISTEXT = 84
TK_ISATOM = 85
TK_ISTUP = 86
TK_ISREL = 87
TK_ISFUNC = 88
TK_ISANY = 89
TK_BANG = 90
TK_BANGLT = 80
TK_BANGGT = 91
TK_HAS = 92
TK_TILDE = 93

operators = [
    (TK_AT, "@"),
    (TK_SHARP, "#"),
    (TK_LPAREN, "("), 
    (TK_RPAREN, ")"), 
    (TK_MINUS, "-"),
    (TK_BLOCKSTART, "(+"),
    (TK_BLOCKEND, "+)"), 
    (TK_COLON, ":"),
    (TK_STDBOOL, "?-Bool"),
    (TK_STDINT, "?-Int"),
    (TK_STDTEXT, "?-Text"),
    (TK_COMMA, ","),
    (TK_RIGHTARROW, "->"),
    (TK_EQUAL, "="),
    (TK_ASSIGN, ":="),
    (TK_PLUS, "+"),
    (TK_MUL, "*"),
    (TK_DIV, "/"),
    (TK_SEMICOLON, ";"),
    (TK_CONCAT, "++"),
    (TK_PIPE, "|"),
    (TK_OPEXTEND, "<<"),
    (TK_LESS, "<"),
    (TK_GREATER, ">"),
    (TK_DIFFERENT, "<>"),
    (TK_LESSEQUAL, "<="),
    (TK_GREATEREQUAL, ">="),
    (TK_TWO_DOTS, ".."),
    (TK_ONE_DOT, "."),
    (TK_QUESTION, "?"),
    (TK_SET_MINUS, "\\"),
    (TK_PROJECT_PLUS, "|+"),
    (TK_PROJECT_MINUS, "|-"),
    (TK_LEFT_ARROW, "<-"),
    (TK_LBRACKET, "["),
    (TK_RBRACKET, "]"),
    (TK_CHOICE, "&"),
    (TK_ISBOOL, "is-Bool"),
    (TK_ISINT, "is-Int"),
    (TK_ISTEXT, "is-Text"),
    (TK_ISATOM, "is-Atom"),
    (TK_ISTUP, "is-Tup"),
    (TK_ISREL, "is-Rel"),
    (TK_ISFUNC, "is-Func"),
    (TK_ISANY, "is-Any"),
    (TK_BANG, "!"),
    (TK_BANGLT, "!<"),
    (TK_BANGGT, "!>"),
    (TK_TILDE, "~"),
    ]

keywords = [(TK_TUP, "tup"), 
            (TK_REL, "rel"),
            (TK_TRUE, "true"),
            (TK_FALSE, "false"), 
            (TK_NOT, "not"),
            (TK_OR, "or"),
            (TK_AND, "and"),
            (TK_VAL, "val"),
            (TK_IN, "in"),
            (TK_ZERO, "zero"),
            (TK_ONE, "one"),
            (TK_FUNC, "func"),
            (TK_END, "end"),
            (TK_TYPE_BOOL, "Bool"),
            (TK_TYPE_INT, "Int"),
            (TK_TYPE_TEXT, "Text"),
            (TK_TYPE_ATOM, "Atom"),
            (TK_TYPE_TUP, "Tup"),
            (TK_TYPE_REL, "Rel"),
            (TK_TYPE_FUNC, "Func"),
            (TK_TYPE_ANY, "Any"),
            (TK_MOD, "mod"),
            (TK_MAX, "max"),
            (TK_MIN, "min"),
            (TK_COUNT, "count"),
            (TK_ADD, "add"),
            (TK_MULT, "mult"),
            (TK_DAYS, "days"),
            (TK_BEFORE, "before"),
            (TK_AFTER, "after"),
            (TK_TODAY, "today"),
            (TK_DATE, "date"),
            (TK_OPEN, "open"),
            (TK_CLOSE, "close"),
            (TK_WRITE, "write"),
            (TK_SYSTEM, "system"),
            (TK_IF, "if"),
            (TK_FI, "fi"),
            (TK_HAS, "has"),
            ]

tokenNames = {}
for k,v in operators:
    tokenNames[k] = "\"%s\""%v
for k,v in keywords:
    tokenNames[k] = "\"%s\""%v
tokenNames[TK_EOF] = "End of file"
tokenNames[TK_ERR] = "Bad token"
tokenNames[TK_NAME] = "Name"
tokenNames[TK_INT] = "Int"
tokenNames[TK_TEXT] = "Text"

maxLength = max([len(value) for _,value in operators])

operators_map = [{} for _ in range(maxLength+1)]

for key, value in operators:
    operators_map[len(value)][value] = key

keywords_map = {}
for key, value in keywords:
    keywords_map[value] = key

class Lexer:
    def __init__(self, code):
        self.code = code
        self.index = 0

    def getNext(self):
        c, i = self.code, self.index
        whitespace = " \t\r\n"
        while i < len(c) and c[i] in whitespace:
            i+=1

        self.index = i

        if i == len(c):
            return (TK_EOF, i, 0)

        # check if is operator
        for l in reversed(range(len(operators_map))):
            if c[i:i+l] in operators_map[l]:
                self.index += l
                return (operators_map[l][c[i:i+l]], i, l)

        # check if is Name or keyword
        if c[i].isalpha():
            j = 0
            while i+j < len(c) and c[i+j].isalnum():
                j+=1
            self.index += j
            # check if is keyword
            if c[i:i+j] in keywords_map: 
                return (keywords_map[c[i:i+j]], i, j)
            return (TK_NAME, i, j)
        
        # check if it is an int
        if c[i].isdigit():
            j = 0
            while i+j < len(c) and c[i+j].isdigit():
                j+=1
            self.index += j
            return (TK_INT, i, j)    

        # check if it is a text
        if c[i] == '"':
            j = 1
            while i + j < len(c) and c[i+j] != '"':
                j+=1
            if i+j == len(c):
                self.index += j
                return (TK_ERR, i, j)
            self.index += j+1
            return (TK_TEXT, i, j+1)
        
        # skip invalid token
        j = 0
        while i+j < len(c) and c[i+j] not in " \t\r\n":
            j = j + 1
        self.index += j
        return (TK_ERR, i, j)
