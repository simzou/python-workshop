
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
#     - Filter
# - Standard Library
#     - itertools
#     - random
#     - defaultdict
#     - pdb
# - External 
#     - Django, Flask (web frameworks)
#     - BeautifulSoup (scraping websites)
#     - numpy, matplotlib, jupyter (numerical/scientific computing)
#     - nltk (natural language processing)
#     - sklearn (machine learning and data science)
# - The python toolkit
#     - pip
#     - virtualenv
#     - anaconda
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
# - `len`, `range`, basic built in functions
# 
# ## What is this workshop
# 
# - The only real unifying theme of this talk is that it's going to be features of python that I (Simon) like or think are cool / interesting / useful about python that go beyond the basics.
# - [Not a beginner, not an expert](http://afabbro.github.io/jsconf2013/), [video](https://www.youtube.com/watch?v=v0TFmdO4ZP0) - good talk on being an intermediate programmer
# - Code / presentation is at https://github.com/simzou/python-workshop, [web page](simzou.github.io/python-workshop), [alternative](https://github.com/simzou/python-workshop/blob/master/workshop.md)
# - This is a jupyter notebook, if you have it installed you can run the code in this talk by double clicking a code cell and hitting shift+enter. If you don't, don't worry about it, will talk about it later.
# 
# 
# # Motivation
# 
# - Question for the audience: Why are you here?
# - Why I like python
#     - "batteries included"
#     - lots of features, but the syntax stays out of your way
#     - lots of mature libraries for doing anything from web apps to natural language processing
#     - code feels clean
#     - usable in job interviews
#     - It's fun 

# In[1]:

# try this
import antigravity


# # Warm-ups
# ## sorting
# - Tricking you into learning functional programming
# - Python docs [here](https://docs.python.org/2/howto/sorting.html)

# In[2]:

sentence = "Thanks for coming to this python workshop! I think python is a neat language."
# by default, split() uses whitespace as delimiters
words = sentence.split()
print "words:", words


# In[3]:

sorted_words = sorted(words)
print "sorted words:", sorted_words


# In[4]:

sorted_words_by_length = sorted(words, key=len)
print "sorted words by length:", sorted_words_by_length


# In[5]:

sorted_words_by_length_rev = sorted(words, key=len, reverse=True)
print "reversed:", sorted_words_by_length_rev


# ## string slicing (and the step parameter)
# - useful for manipulating strings quickly
# - Interview question: Does this create new memory?

# In[6]:

introduction = "Hi my name is Simon"
# get the whole string
print introduction[:]
# get whole thing starting from index 4
print introduction[4:]
# get up to index 8
print introduction[:8]


# In[7]:

# get every other letter
introduction[::2]


# In[8]:

# reverse the string
introduction[::-1]


# In[9]:

# Also works in range()
print range(0,20,2)


# ## sets
# - same as the mathematical set, doesn't allow duplicates
# - so it's useful anytime you want to find unique elements, filter out duplicates, etc.
# - Python docs [here](https://docs.python.org/2/library/stdtypes.html#set-types-set-frozenset)

# In[10]:

repeats = "Hi Hi My My Name Name is is Simon Simon"
bag_of_words = set(repeats.split())
print "Bag of words:", bag_of_words


# In[11]:

word = "bookkeeper"
print set(word)


# # Fancy Python Shortcuts 
# 
# also known as syntatic sugar
# 
# ## List Comprehensions
# - for making lists in one line

# In[12]:

# Making a list of perfect squares
squares = []
for i in range(10):
    square = i * i
    squares.append(square)
print squares


# In[13]:

squares_lc = [i * i for i in range(10)]
print squares_lc


# ## Ternary Operator
# - for those too lazy to write an if else

# In[14]:

simon_is_hungry = False

if simon_is_hungry:
    words = '"Give me food!"'
else:
    words = '"I am full"'
    
print "Simon says,", words


# In[15]:

words = '"Give me food!"' if simon_is_hungry else '"I am full"'
print "Simon says,", words


# ## Combined, sort of
# - okay not really

# In[16]:

squares = [x*x for x in range(10) if x % 2 == 0]
print squares


# On the agenda it says we're going to cover iterables and generators next, but I think it's easier to explain if I start with something else:
# 
# # A detour to the Standard Library
# ## itertools library
# - As the name implies useful for iterating over stuff

# In[17]:

import itertools

perms = itertools.permutations("ABCD", 2)
for p in perms:
    print p


# In[18]:

combos = itertools.combinations("ABCD", 2)
for c in combos:
    print c


# In[19]:

# what is this?
print combos


# # Some python concepts
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

# In[20]:

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


# In[21]:

r = count_using_return()
print "r:", r
y = count_using_yield()
print "y:", count_using_yield()


# In[22]:

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

# In[23]:

print type(range(10))
print type(xrange(10))


# # Functional Programming
# 
# Wikipedia definition: "programming paradigm—a style of building the structure and elements of computer programs—that treats computation as the evaluation of mathematical functions and avoids changing-state and mutable data."
# 
# My definition: When you pass functions as parameters to other functions 
# 
# ## built in python methods - map, filter
# 
# ### map - apply a function to every element

# In[24]:

words = "Hi my name is Simon".split()
# ['Hi', 'my', 'name', 'is', 'Simon']
# get the length of each word
map(len, words)


# ### lambda functions - functions without a name
# 

# In[25]:

def add(x,y):
    return x + y

# is equivalent to 

add = lambda x,y:  x + y


# In[26]:

map(lambda x: x.upper(), words)


# ### filter - filters things

# In[27]:

# even numbers
filter(lambda x: x % 2 == 0, range(20))


# In[28]:

# get all words from sentence with 3 or fewer letters
filter(lambda x: len(x) <= 3, "Hi My Name is Simon".split())


# # Back to the Standard Library
# 
# ## random
# 
# - lots of stuff in here, the things I find most useful is `random.choice` and `random.sample`
# - [Python docs](https://docs.python.org/2/library/random.html)

# In[29]:

import random

numbers = range(10)

for _ in range(5):
    print random.choice(numbers)


# In[30]:

random.sample(numbers, 5)


# ## collections - fancy containers
# 
# ### defaultdict - dictionaries with default values for keys

# In[32]:

from collections import defaultdict

dd = defaultdict(list)
print dd['keyIhaventseenbefore']


# ## pdb - because you miss gdb
# - Use `pdb.set_trace()` to set a breakpoint

# In[31]:

import pdb

x = 4
y = 5
pdb.set_trace()
z = 6


# # The Python Ecosystem - External Libraries
# 
# Beautiful thing about python is that other people like it and build libraries to do useful stuff for it.
# 
# - Django, Flask (web frameworks)
#     - Pinterest, Bitbucket built on Django
# - BeautifulSoup (scraping websites)
# - numpy, matplotlib (numerical/scientific computing)
# - nltk (natural language processing)
# - sklearn (machine learning and data science)
# - jupyter notebooks
#     - tool primarily used for data science, scientific computing, but I find it useful pedagogy and presentations as well
# 
# ## Libaries for managing these libraries
# 
# - pip (python package manager)
#     - e.g. `pip install django`
# - virtualenv (create a contained python environment)
#     - for managing different versions of libraries
# - anaconda (for jupyter notebooks, data science stuff)
#     - not sure how well this plays with the above though...

# # Community
# 
# - Big python conferences are called PyCon, they happen around the world
# - There's also separate conferences for SciPy, Django, ... 
# - [SoCal Python Meetup Group](http://www.meetup.com/socalpython/)
# - [Pyladies](www.pyladies.com)
# - I've never been to any python conferences, but here's a description from Paul Ford's beautiful article / novella [What is Code](http://www.bloomberg.com/graphics/2015-paul-ford-what-is-code/): 
# 
# > Tech conferences look like you’d expect. Tons of people at a Sheraton, keynote in Ballroom D. Or enormous streams of people wandering through South by Southwest in Austin. People come together in the dozens or thousands and attend panels, ostensibly to learn; they attend presentations and brush up their skills, but there’s a secondary conference function, one of acculturation. You go to a technology conference to affirm your tribal identity, to transfer out of the throng of dilettantes and into the zone of the professional. You pick up swag and talk to vendors, if that’s your thing.
# 
# # Python 2 vs Python 3 drama and notes
# 
# - In 2008 python 3 was released. It is a technically "better" language (more consistent, efficient, better Unicode support) but it was not backwards compatible with python 2. This made people unhappy.
#     - division is by default integer division in python 2 but is floating point in python 3
#         - you can get python 3 division (and others similarly) in python 2 by including `from __future__ import division` in your python file
#     - instead of `print "Hello World"` you now have to do `print("Hello World")` in python 3. In some ways this is a small change, in other ways it's a huge change that got people most upset
# - Python 2 "just worked" so adoption has been slow. As of 2015, more people were still using python 2 [[citation]](http://stackoverflow.com/questions/30751668/python-2-vs-python-3-2015-usage)
# - Part of the problem is that every major library had to be rewritten in python 3, so many did not support python 3 for a while
# - I still use python 2

# # Resources (i.e. where I learned Python)
# 
# - [Udacity](udacity.com)
#     - [CS 212 - Design of Computer Programs](https://www.udacity.com/course/design-of-computer-programs--cs212) - Taught by Peter Norvig, director of Research of Google and author of the standard book in AI (used in UCLA's CS 161). Probably my favorite class I've ever taken. Most of things in this workshop come from there.
#     - [CS 373 - Programming a Robotic Car](https://www.udacity.com/course/artificial-intelligence-for-robotics--cs373) - Taught by Sebastian Thrun, who started the autonomous car project at Google. Not python per se, but you get practice doing something cool in python and some numerical computing stuff
#     - [CS 253 - Web App Development](https://www.udacity.com/course/web-development--cs253) - Taught by Steve Huffman, co-founder of reddit. Teaches you how to build a blog and wiki from scratch using python and Google App Engine
# - Books
#     - There was a one python book at my local library, just checked that out and read it
