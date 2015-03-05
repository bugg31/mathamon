#Areas
main = 1
levels = 0
asking = 0
level1 = 0

def main():
	print("Hello and welcome to mathamon")
	print("Always answer decimals with decimals and fractions with fractions")
	players_answer = raw_input("type 'Play' to move on")
	players_answer = players_answer.lower()
	if players_answer == "play":
		print("Moving To Levels...")
		main = 0
		levels = 1

# running
if __name__ == '__main__':
	print("Always have a decimal at the end so if the answer is 60, type 60.0 otherwise it bugs out")
	print("answer decimals with decimals and fractions with fractions.")
	main()