from lexer import MyLexer
from smash_sys import Sys

if __name__ == "__main__":
    smash_lex = MyLexer()
    smash_lex.build()
    try:
        while True:
            user_input = input("$: ")

            Sys.add_to_history(user_input)

            for i in smash_lex.generate(user_input):
                print(i)

    except KeyboardInterrupt:
        print("\nUnsmashing....")

    Sys.save_history_to_file()

    Sys.print_history()
