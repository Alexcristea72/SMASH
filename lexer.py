import ply.lex as lex

class MyLexer:
    tokens = (
        'NUMBER',
        'PLUS',
        'MINUS',
        'TIMES',
        'DIVIDE',
        'LPAREN',
        'RPAREN',
        'LOGICAL_AND',
        'LOGICAL_OR',
        'LOGICAL_NOT',
        'ASSIGNMENT',
        'DOUBLE_QUOTE_STRING',
        'ARRAY',
        'VARIABLE',
        'UNARY_MESSAGE',
        'KEYWORD_ARGUMENT',
        'KEYWORD_SELECTOR',
        'EQUALS',
        'NOT_EQUAL',
        'GREATER',
        'LESS',
        'GREATER_EQUAL',
        'LESS_EQUAL',
    )

    t_PLUS = r'\+'
    t_MINUS = r'-'
    t_TIMES = r'\*'
    t_DIVIDE = r'/'
    t_LPAREN = r'\('
    t_RPAREN = r'\)'
    t_ARRAY = r'\#'
    t_EQUALS = r'=='
    t_NOT_EQUAL = r'!='
    t_GREATER = r'>'
    t_LESS = r'<'
    t_GREATER_EQUAL = r'>='
    t_LESS_EQUAL = r'<='

    t_LOGICAL_AND = r'\&\&'
    t_LOGICAL_OR = r'\|\|'
    t_LOGICAL_NOT = r'\!'
    t_ASSIGNMENT = r':='

    def t_UNARY_MESSAGE(self, t):
        r'\b(?:history|\w+)\b(?:\s*:\s*\$?\w+\$?(?:\s*:\s*\w+\$?)*)?'
        if t.value.isalpha():
            t.type = 'VARIABLE'
        else:
            t.type = 'UNARY_MESSAGE'
        return t

    def t_KEYWORD_ARGUMENT(self, t):
        r'\b\w+\b'
        return t

    def t_KEYWORD_SELECTOR(self, t):
        r'\b\w+\b:\b\w+\b'
        return t

    def t_NUMBER(self, t):
        r'(\d*\.)?\d+'
        t.value = float(t.value)
        return t

    def t_DOUBLE_QUOTE_STRING(self, t):
        r'["\'][^"\']*["\']'
        t.value = t.value[1:-1]
        return t

    def t_VARIABLE(self, t):
        r'[a-zA-Z_][a-zA-Z0-9_]*'
        return t

    def t_newline(self, t):
        r'\n+'
        t.lexer.lineno += len(t.value)

    t_ignore = ' \t'

    def t_error(self, t):
        print("Illegal character '%s'" % t.value[0])
        t.lexer.skip(1)

    def build(self, **kwargs):
        self.lexer = lex.lex(module=self, **kwargs)

    def test(self, data):
        self.lexer.input(data)
        while True:
            tok = self.lexer.token()
            if not tok:
                break
            print(tok)

    def generate(self,data):
        self.lexer.input(data)
        while True:
            tok = self.lexer.token()
            if not tok:
                break
            yield tok

if __name__ == "__main__":
    test_string = '''
    a := #(1 2 3)
    b := 5
    c := 10
    d := a == b
    e := a != c
    f := b > c
    g := b < c
    h := b >= c
    i := b <= c
    '''

    smash_lex = MyLexer()
    smash_lex.build()
    smash_lex.test(test_string)
