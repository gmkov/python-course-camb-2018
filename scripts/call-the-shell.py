import  subprocess

result = subprocess.run(['date'], 
	stdout=subprocess.PIPE,
	universal_newlines=True)

result = subprocess.run(['date | wc'], 
	# you need to call the shell because you have used the |, medicare shell symbol
	shell=True, # I want to execute a subcommand, fire up shell, let the shell do it
	stdout=subprocess.PIPE,
	universal_newlines=True)

print(result.stdout[:-1]) # to remove blank line at the end