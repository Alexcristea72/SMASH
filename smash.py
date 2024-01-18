from lexer import MyLexer

if __name__ == "__main__":
    smash_lex = MyLexer()
    smash_lex.build()
    try:
        while True:
            user_input = input("$: ")
            for i in smash_lex.generate(user_input):
                print(i)

    except KeyboardInterrupt:
        print("\nUnsmashing....")