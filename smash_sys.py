import subprocess

class Sys:
    command_history = []

    def __init__(self):
        pass

    def call(self, command: str):
        try:
            result = subprocess.run(command, shell=True, check=True, text=True, capture_output=True)
            return result.stdout
        except subprocess.CalledProcessError as e:
            return e

    @staticmethod
    def add_to_history(command):
        Sys.command_history.append(command)

    @classmethod
    def get_history(cls):
        return cls.command_history

    @classmethod
    def save_history_to_file(cls, filename='command_history.txt'):
        with open(filename, 'a') as file:
            for command in cls.command_history:
                file.write(command + '\n')

    @classmethod
    def print_history(cls):
        print("Command History:")
        for idx, command in enumerate(cls.command_history, start=1):
            print(f"{idx}. {command}")
