animals = {"elephant", "dog", "cat", "mouse", "dog", "elephant", "rabbit", "rabbit", "mouse"}

for animal in animals:
    print(animal)  # unique elements

# rabbit
# elephant
# mouse
# cat
# dog

print(len(animals))  # 5

more_animals = {"crocodile", "snake", "lizard", "dinosaur"}

animals.update(more_animals)

for update_set in animals:
    print(update_set)
# snake
# mouse
# dinosaur
# dog
# rabbit
# crocodile
# elephant
# cat
# lizard

print(len(animals))  # 9 animals in set after update

add_two_sets = animals.union(more_animals)
print(add_two_sets)  # {'elephant', 'mouse', 'snake', 'lizard', 'crocodile', 'dinosaur', 'cat', 'dog', 'rabbit'}

animals.remove("snake")
print(animals)  # {'cat', 'dog', 'dinosaur', 'rabbit', 'crocodile', 'lizard', 'mouse', 'elephant'}

animals.add("hello")
print(animals)  # {'elephant', 'dinosaur', 'crocodile', 'cat', 'dog', 'hello', 'lizard', 'mouse', 'rabbit'}

animals.copy()
print(animals)  # {'mouse', 'elephant', 'lizard', 'cat', 'hello', 'rabbit', 'crocodile', 'dog', 'dinosaur'}

animals.pop()
print(animals)  # remove random last element

animals.clear()
print(animals)  # set()

set_1 = {"one", "two", "three", "four", "five", "six"}
set_2 = {"one hundred", "two", "ten", "four", "fifteen", "six"}
print(set_1.difference(set_2))  # {'one', 'five', 'three'}
print(set_2.difference(set_1))  # {'ten', 'one hundred', 'fifteen'}

set_3 = {"one", "two", "three", "four", "five", "six"}
set_4 = {"1", "2", "3", "four", "5", "6"}
print(set_3.intersection(set_4))  # {'four'}


