"""my_list = [1, 2, 3]
iterator1 = iter(my_list)
print(next(iterator1))
print(next(iterator1))
print(next(iterator1))"""
"""my_list = [1, 2, 3]
iterator2 = iter(my_list)
for elem in iterator2:
    print(elem)"""
"""class Counter:
    class Counter:
        def __init__(self, max_number):
            self.i = 0
            self.max_number = max_number
        def __iter__(self):
            self.i = 0
            return self
        def __next__(self):
            self.i += 1
            if self.i > self.max_number:
                raise StopIteration
            return self.i

#for elem in count:
#    print(elem)
count = Counter(5)
print(count.__next__())
print(count.__iter__())
print(next(count))
print(iter(count))"""
"""def raise_to_the_degrees(number, max_degree):
    i=0
    while True:
        yield number ** i
        i+=1
res = raise_to_the_degrees(12345, 4500)
print(res)
for _ in res:
    print(_)"""
class EvenNumbers:
    def __init__(self, limit):
        self.limit = limit
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        while self.current <= self.limit:
            if self.current % 2 == 0:
                even_number = self.current
                self.current = self.current + 1
                return even_number
            self.current = self.current + 1
        raise StopIteration
even_numbers = EvenNumbers(10)
for num in even_numbers:
    print(num)
