#problem 1
with open("data2.txt") as file:
	for line in file:
		if "lol" in line.lower():
			print(line.strip())

#problem 2
dict_to_str=lambda d:"\n".join(", ".join(map(str,i))for i in d.items())

#problem 3
def dict_to_str_sorted(d):
	return dict_to_str(sorted(d.items(), key=lambda item: item[0]))

#problem 4
class Phones:
	#4a
	def read_words(self, file_name="cmudict-0.7b"):
		with open(file_name) as file:
			lines = list(file)

		lines = [line.strip().split("  ", 1) for line in lines if line[:3] != ";;;"]
		self.words = {''.join(filter(lmabda x: str.isalpha or x=="-", line[0])):line[1].split() for line in lines}

	#4b
	def read_categories(self, file_name="cmudict-0.7b.phones"):
		with open(file_name) as file:
			lines = list(file)

		lines = [line.strip().split("\t", 1) for line in lines]
		self.categories = {line[0]:line[1] for line in lines}
		self.vowels = [syllable for syllable in self.categories if self.categories[syllable]=="vowel"]

	def get_syllables(self, word):
		return [''.join(filter(str.isalpha, syllable)) for syllable in self.words[word]]

	#4c
	def vowel_count(self, word):
		word = self.get_syllables(word)
		return sum(word.count(vowel) for vowel in self.vowels)

	#4d
	def syllable_count(self, word):
		syllables = self.get_syllables(word)
		count = 0
		is_prev = False
		for n in range(len(syllables)):
			if syllables[n] in self.vowels and not is_prev:
				pass


		return len(syllables)

	#problem 5
	def reading_level(self, file_name):
		with open(file_name) as file:
			lines = list(file)

		text = ".".join(lines)
		words = [''.join(filter(str.isalpha, word)).upper() for word in text.split(" ")]

		syllables = sum(self.syllable_count(word) for word in words)
		words = len(words)
		sentences = text.count(".")

		return 0.39*words/sentences+11.8*syllables/words-15.59

x = {1:6, "sds":67, "Josh":"Bad"}
print(dict_to_str(x))