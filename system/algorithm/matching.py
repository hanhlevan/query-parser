
class Consine:
	def __init__(self):
		pass

	def exec(self, vector_1, vector_2):
		size_1 = 0
		for (word, weight) in vector_1.items():
			size_1 += weight ** 2
		if size_1 == 0: return 0
		size_2 = 0
		for (word, weight) in vector_2.items():
			size_2 += weight ** 2
		if size_2 == 0: return 0
		sim = 0
		for (word, weight) in vector_1.items():
			if word in vector_2:
				sim += weight * vector_2[word]
		sim /= (size_1 * size_2)
		return sim

class NGram:
	
	def __init__(self, list_ngrams=[1, 2, 3]):
		self.list_ngrams = list_ngrams

	def exec(self, list_words_1, list_words_2):
		ngram_matching = dict()
		for n in self.list_ngrams:
			s1 = set(tuple(tuple(list_words_1[i : i + n]) for i in range(len(list_words_1) - n + 1)))
			s2 = set(tuple(tuple(list_words_2[i : i + n]) for i in range(len(list_words_2) - n + 1)))
			ngram_matching[n] = len(s1.intersection(s2)) / max(1, len(s1.union(s2)))
		sim = 0
		for n in self.list_ngrams:
			sim += ngram_matching[n] * n
		return sim / sum(self.list_ngrams)

class EditDistance:

	def __init__(self):
		pass

	def exec(self, list_words_1, list_words_2):
		m = max(len(list_words_1), len(list_words_2))
		distances = range(m + 1)
		for i2, w2 in enumerate(list_words_2):
			distances_ = [i2+1]
			for i1, w1 in enumerate(list_words_1):
				if w1 == w2:
					distances_.append(distances[i1])
				else:
					distances_.append(1 + min((distances[i1], distances[i1 + 1], distances_[-1])))
			distances = distances_
		u = distances[-1] / max(1, m)
		return 1 - u