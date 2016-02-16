
# Intermediate Python Workshop

## Agenda

- Introductions
- Motivation
- Warm-ups
    - sorted
    - string slicing
    - set
- Fancy Python Shortcuts and Concepts and stuff
    - List comprehensions
    - Ternary operator
    - Iterables
    - Generators
- Functional Programming
    - Map
    - Zip
- Standard Library
    - itertools
    - random.choice
    - pdb
    - defaultdict
- External 
    - Django, Flask (web frameworks)
    - BeautifulSoup (scraping websites)
    - numpy, matplotlib, jupyter (numerical/scientific computing)
    - nltk (natural language processing)
    - sklearn (machine learning and data science)
- Community / Drama / Resources
    - 2v3
    - Conferences
    - Udacity

# Introduction

## What you should already know

- basic python syntax (for loops, variable declarations, strings)
- basic python data structures (lists, dictionaries)
- how to write functions in python

## What is this workshop

- The only real unifying theme of this talk is that it's going to be features of python that I (Simon) like or think are cool that go beyond the very basics of python. 
- [Not a beginner, not an expert](http://afabbro.github.io/jsconf2013/), [video](https://www.youtube.com/watch?v=v0TFmdO4ZP0) - good talk on being an intermediate programmer
- Code / presentation is at https://github.com/simzou/python-workshop
- This is a jupyter notebook, if you have it installed you can run the code in this talk by double clicking a code cell and hitting shift+enter. If you don't, don't worry about it, will talk about it later.


# Motivation

- Question for the audience: Why are you here?
- Why I like python
    - "batteries included"
    - lots of features, but the syntax stays out of your way
    - It's fun (name origin, code feels clean)


```python
import antigravity
```

# Warm-ups
## sorting
- Tricking you into learning functional programming
- Python docs [here](https://docs.python.org/2/howto/sorting.html)


```python
sentence = "Thanks for coming to this python workshop! I think python is a neat language."
# by default, split() uses whitespace as delimiters
words = sentence.split()
print "words:", words
```

    words: ['Thanks', 'for', 'coming', 'to', 'this', 'python', 'workshop!', 'I', 'think', 'python', 'is', 'a', 'neat', 'language.']



```python
sorted_words = sorted(words)
print "sorted words:", sorted_words
```

    sorted words: ['I', 'Thanks', 'a', 'coming', 'for', 'is', 'language.', 'neat', 'python', 'python', 'think', 'this', 'to', 'workshop!']



```python
sorted_words_by_length = sorted(words, key=len)
print "sorted words by length:", sorted_words_by_length
```

    sorted words by length: ['I', 'a', 'to', 'is', 'for', 'this', 'neat', 'think', 'Thanks', 'coming', 'python', 'python', 'workshop!', 'language.']



```python
sorted_words_by_length_rev = sorted(words, key=len, reverse=True)
print "reversed:", sorted_words_by_length_rev
```

    reversed: ['workshop!', 'language.', 'Thanks', 'coming', 'python', 'python', 'think', 'this', 'neat', 'for', 'to', 'is', 'I', 'a']


## string slicing (and the step parameter)
- useful for manipulating strings quickly
- Interview question: Does this create new memory?


```python
introduction = "Hi my name is Simon"
# get the whole string
print introduction[:]
# get whole thing starting from index 4
print introduction[4:]
# get up to index 8
print introduction[:8]
```

    Hi my name is Simon
    y name is Simon
    Hi my na



```python
# get every other letter
introduction[::2]
```




    'H ynm sSmn'




```python
# reverse the string
introduction[::-1]
```




    'nomiS si eman ym iH'




```python
# Also works in range()
print range(0,20,2)
```

    [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]


## sets
- same as the mathematical set, doesn't allow duplicates
- so it's useful anytime you want to find unique elements, filter out duplicates, etc.
- Python docs [here](https://docs.python.org/2/library/stdtypes.html#set-types-set-frozenset)


```python
repeats = "Hi Hi My My Name Name is is Simon Simon"
bag_of_words = set(repeats.split())
print "Bag of words:", bag_of_words
```

    Bag of words: set(['Simon', 'is', 'Hi', 'My', 'Name'])



```python
word = "bookkeeper"
print set(word)
```

    set(['b', 'e', 'k', 'o', 'p', 'r'])


# Fancy Python Shortcuts 

also known as syntatic sugar

## List Comprehensions
- for making lists in one line


```python
# Making a list of perfect squares
squares = []
for i in range(10):
    square = i * i
    squares.append(square)
print squares
```

    [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]



```python
squares_lc = [i * i for i in range(10)]
print squares_lc
```

    [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]


## Ternary Operator
- for those too lazy to write an if else


```python
simon_is_hungry = False

if simon_is_hungry:
    words = '"Give me food!"'
else:
    words = '"I am full"'
    
print "Simon says,", words
```

    Simon says, "I am full"



```python
words = '"Give me food!"' if simon_is_hungry else '"I am full"'
print "Simon says,", words
```

    Simon says, "I am full"


## Combined, sort of
- okay not really


```python
squares = [x*x for x in range(10) if x % 2 == 0]
print squares
```

    [0, 4, 16, 36, 64]


## Functional Programming



# The Standard Library
## itertools library
- As the name implies useful for iterating over stuff


```python
import itertools

perms = itertools.permutations("ABCD", 2)
for p in perms:
    print p
```

    ('A', 'B')
    ('A', 'C')
    ('A', 'D')
    ('B', 'A')
    ('B', 'C')
    ('B', 'D')
    ('C', 'A')
    ('C', 'B')
    ('C', 'D')
    ('D', 'A')
    ('D', 'B')
    ('D', 'C')



```python
combos = itertools.combinations("ABCD", 2)
for c in combos:
    print c
```

    ('A', 'B')
    ('A', 'C')
    ('A', 'D')
    ('B', 'C')
    ('B', 'D')
    ('C', 'D')



```python
# what is this?
print combos
```

    <itertools.combinations object at 0x104663578>


# A detour - Some python concepts
## Iterables and iterators
- Iterable definition: "An iterable is an object that has an __iter__ method which returns an iterator"
- Iterator definition: "An iterator is an object with a next method"
- References: [Stack Overflow](http://stackoverflow.com/questions/9884132/what-exactly-are-pythons-iterator-iterable-and-iteration-protocols) and [Some dude's blog](http://nvie.com/posts/iterators-vs-generators/)


- My definition: Iterable is anything you can do a for loop on. In python this is all the basic data structures like lists and dictionaries, but also strings (loop through characters) and files (loop through lines).
- Iterator: Object that you can call next on


- So `combos` is clearly an iterable, but the type is not that of a collection (data structure that holds stuff); it is a **generator**

## Generators and the `yield` keyword


```python
# This code doesn't really make sense but bear with me
def count_using_return():
    count = 0
    while(count < 10):
        count += 1
        return count
    
def count_using_yield():
    count = 0
    while (count < 10):
        count += 1
        yield count
```


```python
r = count_using_return()
print "r:", r
y = count_using_yield()
print "y:", count_using_yield()

```

    r: 1
    y: <generator object count_using_yield at 0x104644cd0>



```python
for c in count_using_yield():
    print c
```

    1
    2
    3
    4
    5
    6
    7
    8
    9
    10


### So why is this helpful? 

- Generators take up less space, and defer computation and access until when you need it. 
- `range(10)` creates the list of 10 integers
- `xrange(10)` creates a generator
- Since xrange is more efficient, in Python 3, implementation of `range` is replaced with `xrange`


- This was a long way of saying `itertools.combinations` object is a generator


```python
print type(range(10))
print type(xrange(10))
```

    <type 'list'>
    <type 'xrange'>



```python

```


```python

```
