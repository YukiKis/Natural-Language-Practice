# -*- coding: utf-8 -*-
"""
Created on Mon Dec 14 16:06:24 2020

@author: s1430
"""

import re
import numpy as np
import pandas as pd

# 00
word = "stressed"
print(word[::-1])

# 01
word = "パタトクカシーー"
print(word[::2])

# 02
word1 = "パトカー"
word2 = "タクシー"
word = ""
# ans = "".join([i + j for i, j in zip(word1, word2)])
for x in range(len(word1)):
    word += word1[x] + word2[x]
print(word)

# 03
word = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
word = re.sub(r"[,.]", "", word)
word_list = word.split()
word_count = []
for w in word_list:
    word_count.append(len(w))
print(word_count)

# 04
word = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
word_list = word.split()
count_list = np.arange(len(word_list))
first_list = np.array([1, 5, 6, 7, 8, 9, 15, 16, 19]) - 1
first_second_list = np.delete(count_list, first_list)
# df = pd.DataFrame([first_list, [word_list[w][0] for w in first_list], first_second_list, [word_list[w][0:2] for w in first_second_list]])
# df = df.T
word_dict = {}
for x in count_list:
    if x in first_list:
        word_dict[x] = word_list[x][0]
    else:
        word_dict[x] = word_list[x][0:2]
print(word_dict)

# 05 何故かはじめn個の空タプルが出来る
def n_gram_word(word, n):
    n_gram_list = []
    for x in np.arange(len(word) - n + 1):
        n_gram_list.append(tuple(word[x:x+n]))
    return n_gram_list

def n_gram_alphabet(word, n):
    word_list = re.sub(r"\W", "", word).split()
    alphabet_list = []
    for word in word_list:
        for alpha in word:
            alphabet_list.append(alpha)
    n_gram_list = [alphabet_list[x: x+n] for x in np.arange(len(alphabet_list) -n + 1)]
    return n_gram_list

print(n_gram_word("Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can.", 2))
print(n_gram_word("Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can.", 3))

print(n_gram_alphabet("Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can.", 2))
print(n_gram_alphabet("Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can.", 3))

# 06
word1 = "paraparaparadise"
word2 = "paragraph"

def n_gram_al(word, n):
    alset = set()
    for index in range(len(word) - n + 1):
        alset.add(word[index:index+n])
    return alset
X = n_gram_al(word1, 2)
Y = n_gram_al(word2, 2)
print(X & Y)
print(X | Y)
print(X - Y)
print("True" if "se" in X else "False")

# 07
def template(x, y, z):
    return ("{}時の{}は{}".format(x, y, z))
print(template("12時", "気温", "22.4"))

# 08
def cipher(str):
    rep = [char(219 - ord(x)) if x.islower() else x for x in str]
    return "".join(rep)


# 09
#def Typoglycemia(sentence):
#    for word in sentence:
#        if len(word) > 4:
#            word[1:len(word) - 1] = word.delete(0, -1).shuffle()
import random
def shuffle(words):
    result = []
    for word in words.split():
        if len(word) > 4:
            word = word[:1] + "".join(random.sample(word[1:-1], len(word) - 2)) + word[-1:]
        result.append(word)
    return result
words = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
print(shuffle(words))
            
