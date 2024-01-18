import subprocess
class Sys:

	def __init__(self):
		pass

	def call(self, command: str):
		try:
			result = subprocess.run(command, shell=True, check=True, text=True, capture_output=True)
			return result.stdout
		except subprocess.CalledProcessError as e:
			return e
