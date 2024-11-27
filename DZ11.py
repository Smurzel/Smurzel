class WordLengthIterator:
    def __init__(self, words):
        self.words = words
        self.index = 0
    def __iter__(self):
        return self
    def __next__(self):
        if self.index < len(self.words):
            word_length = len(self.words[self.index])
            self.index += 1
            return word_length
        else:
            raise StopIteration

words = ["слово", "світ", "ого123456"]
iterator = WordLengthIterator(words)

for length in iterator:
    print(length)

def raise_to_the_degrees(number, max_degree):
    i=0
    for _ in range(max_degree):
        yield number ** i
        i+=1
res = raise_to_the_degrees(2, 10)
print(res)
for _ in res:
    print(_)