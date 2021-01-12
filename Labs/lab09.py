import urllib.request

def read(file_name):
	with open(file_name, encoding="latin-1") as file:
		text = file.read()
	return text.split()

def count_words(text):
	return {word:text.count(word) for word in set(text)}

def topn(L, n=10):
	return sorted(set(L), reverse=True)[:n]

def top_words(word_counts, n=10):
	inv = {v: k for k, v in word_counts.items()}
	return [inv[i] for i in topn(inv.keys(), n)]

def choose_variant(variants):
	count = {}
	for term in variants:
		with urllib.request.urlopen("https://search.yahoo.com/search?p="+"+".join(term.split())) as html:
			page = html.read().decode("utf-8")
		print(page)
		count[page.count("li")] = term
	return count[max(count.keys())]

file_name = "text.txt"
text = read(file_name)
word_counts = count_words(text)
best = choose_variant(["top ranked school uoft", "top ranked school waterloo"][:1])

print(word_counts, best, top_words(word_counts, 2))