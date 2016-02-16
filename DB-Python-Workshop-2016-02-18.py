
# coding: utf-8

# # Intermediate Python Workshop
# 
# ## Agenda
# 
# - Introductions
# - Motivation
# - Warm-ups
#     - sorted
#     - string slicing
#     - set
# - Fancy Python Shortcuts and Concepts and stuff
#     - List comprehensions
#     - Ternary operator
#     - Iterables
#     - Generators
# - Functional Programming
#     - Map
#     - Zip
# - Standard Library
#     - itertools
#     - random.choice
#     - pdb
#     - defaultdict
# - External 
#     - Django, Flask (web frameworks)
#     - BeautifulSoup (scraping websites)
#     - numpy, matplotlib, jupyter (numerical/scientific computing)
#     - nltk (natural language processing)
#     - sklearn (machine learning and data science)
# - Community / Drama / Resources
#     - 2v3
#     - Conferences
#     - Udacity

# # Introduction
# 
# ## What you should already know
# 
# - basic python syntax (for loops, variable declarations, strings)
# - basic python data structures (lists, dictionaries)
# - how to write functions in python
# 
# ## What is this workshop
# 
# - The only real unifying theme of this talk is that it's going to be features of python that I (Simon) like or think are cool that go beyond the very basics of python. 
# - [Not a beginner, not an expert](http://afabbro.github.io/jsconf2013/), [video](https://www.youtube.com/watch?v=v0TFmdO4ZP0) - good talk on being an intermediate programmer
# - Code / presentation is at https://github.com/simzou/python-workshop
# - This is a jupyter notebook, if you have it installed you can run the code in this talk by double clicking a code cell and hitting shift+enter. If you don't, don't worry about it, will talk about it later.
# 
# 
# # Motivation
# 
# - Question for the audience: Why are you here?
# - Why I like python
#     - "batteries included"
#     - lots of features, but the syntax stays out of your way
#     - It's fun (name origin, code feels clean)

# In[ ]:

import antigravity


# # Warm-ups
# ## sorting
# - Tricking you into learning functional programming
# - Python docs [here](https://docs.python.org/2/howto/sorting.html)

# In[1]:

sentence = "Thanks for coming to this python workshop! I think python is a neat language."
# by default, split() uses whitespace as delimiters
words = sentence.split()
print "words:", words


# In[2]:

sorted_words = sorted(words)
print "sorted words:", sorted_words


# In[3]:

sorted_words_by_length = sorted(words, key=len)
print "sorted words by length:", sorted_words_by_length


# In[4]:

sorted_words_by_length_rev = sorted(words, key=len, reverse=True)
print "reversed:", sorted_words_by_length_rev


# ## string slicing (and the step parameter)
# - useful for manipulating strings quickly
# - Interview question: Does this create new memory?

# In[5]:

introduction = "Hi my name is Simon"
# get the whole string
print introduction[:]
# get whole thing starting from index 4
print introduction[4:]
# get up to index 8
print introduction[:8]


# In[6]:

# get every other letter
introduction[::2]


# In[7]:

# reverse the string
introduction[::-1]


# In[8]:

# Also works in range()
print range(0,20,2)


# ## sets
# - same as the mathematical set, doesn't allow duplicates
# - so it's useful anytime you want to find unique elements, filter out duplicates, etc.
# - Python docs [here](https://docs.python.org/2/library/stdtypes.html#set-types-set-frozenset)

# In[9]:

repeats = "Hi Hi My My Name Name is is Simon Simon"
bag_of_words = set(repeats.split())
print "Bag of words:", bag_of_words


# In[10]:

word = "bookkeeper"
print set(word)


# # Fancy Python Shortcuts 
# 
# also known as syntatic sugar
# 
# ## List Comprehensions
# - for making lists in one line

# In[11]:

# Making a list of perfect squares
squares = []
for i in range(10):
    square = i * i
    squares.append(square)
print squares


# In[12]:

squares_lc = [i * i for i in range(10)]
print squares_lc


# ## Ternary Operator
# - for those too lazy to write an if else

# In[13]:

simon_is_hungry = False

if simon_is_hungry:
    words = '"Give me food!"'
else:
    words = '"I am full"'
    
print "Simon says,", words


# In[14]:

words = '"Give me food!"' if simon_is_hungry else '"I am full"'
print "Simon says,", words


# ## Combined, sort of
# - okay not really

# In[15]:

squares = [x*x for x in range(10) if x % 2 == 0]
print squares


# ## Functional Programming
# 
# 

# # The Standard Library
# ## itertools library
# - As the name implies useful for iterating over stuff

# In[16]:

import itertools

perms = itertools.permutations("ABCD", 2)
for p in perms:
    print p


# In[17]:

combos = itertools.combinations("ABCD", 2)
for c in combos:
    print c


# In[18]:

# what is this?
print combos


# # A detour - Some python concepts
# ## Iterables and iterators
# - Iterable definition: "An iterable is an object that has an __iter__ method which returns an iterator"
# - Iterator definition: "An iterator is an object with a next method"
# - References: [Stack Overflow](http://stackoverflow.com/questions/9884132/what-exactly-are-pythons-iterator-iterable-and-iteration-protocols) and [Some dude's blog](http://nvie.com/posts/iterators-vs-generators/)
# 
# 
# - My definition: Iterable is anything you can do a for loop on. In python this is all the basic data structures like lists and dictionaries, but also strings (loop through characters) and files (loop through lines).
# - Iterator: Object that you can call next on
# 
# 
# - So `combos` is clearly an iterable, but the type is not that of a collection (data structure that holds stuff); it is a **generator**
# 
# ## Generators and the `yield` keyword

# In[19]:

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


# In[20]:

r = count_using_return()
print "r:", r
y = count_using_yield()
print "y:", count_using_yield()


# In[21]:

for c in count_using_yield():
    print c


# ### So why is this helpful? 
# 
# - Generators take up less space, and defer computation and access until when you need it. 
# - `range(10)` creates the list of 10 integers
# - `xrange(10)` creates a generator
# - Since xrange is more efficient, in Python 3, implementation of `range` is replaced with `xrange`
# 
# 
# - This was a long way of saying `itertools.combinations` object is a generator

# In[22]:

print type(range(10))
print type(xrange(10))


# In[ ]:




# In[ ]:



