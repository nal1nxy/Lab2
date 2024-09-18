"""
Test Sentence methods.
Initial developers: COMP 801 Instructors
Created: February 2024
Developer(s): Nalin
Conllaborator(s): Nalin
Date: 9/13/2024
"""
import pytest

from sentence import Sentence


def test_only_integers_4_1():
    """
    Test sentence that has 4 words, one of which is an integer.
    """
    #test_sentence = 'happy new 2024 year'
    s_obj = Sentence('happy new 2024 year')
    expected = '2024'
    s_obj.only_integers()
    actual = s_obj.sentence
    assert actual == expected


def test_only_integers_4_1_1():
    """
    Test sentence that has 4 words, one of which is an integer, and another
    one has digits and other characters.
    """
    test_sentence = 'happy new 7e@r 2024'
    s_obj = Sentence(test_sentence)
    expected = '2024'
    s_obj.only_integers()
    actual = s_obj.sentence
    assert actual == expected


def test_filter_words_4_2_2():
    """
    Test sentence that has 4 words, including 2 words in the word_lst of
    of length 2
    """
    test_sentence = 'hello im nalin here'
    s_obj = Sentence(test_sentence)
    word_lst = ['im', 'here']
    expected = 'hello nalin'
    s_obj.filter_words(word_lst)
    actual = s_obj.sentence
    assert actual == expected


def test_filter_words_4_0_3():
    """
    Test sentence that has 4 words, none of which is in the word_lst of length
    3
    """
    test_sentence = 'hello im nalin here'
    s_obj = Sentence(test_sentence)
    word_lst = ['ill', 'her', 'tap']
    expected = 'hello im nalin here'
    s_obj.filter_words(word_lst)
    actual = s_obj.sentence
    assert actual == expected


