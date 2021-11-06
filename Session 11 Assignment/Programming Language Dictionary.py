"""
Create a dictionary consisting of 5 programming languages. These programming languages will be the key 
in the dictionary, with each having a value consisting of a one sentence string that gives a brief 
description of the language.
Print the name of the programming language along with its brief description in the following order:
3rd
2nd
4th
1st
5th
Sample output:
html,go,java,css,python
"""

def language(*index):
    prolang = {
    "CSS": "The language we use to style an HTML document. CSS describes how HTML elements should be displayed.",
    "Go": "A statically typed, compiled programming language designed at Google.",
    "HTML": "The standard markup language for Web pages.",
    "Java": "A high-level, class-based, object-oriented programming language that is designed to have as few implementation dependencies as possible.",
    "Python": "Can be used on a server to create web applications."
    }
    prolang_key = list(prolang)
    prolang_value = list(prolang.values())
    for i in index:
        print(prolang_key[i], prolang_value[i], sep='\n')

language(2,1,3,0,4)