"""
File: client.py
Initial developers: COMP 801 instructors
Developer: Nalin
Collaborator(s):Nalin
Date:9/13/2024
"""
from sentence import Sentence


def main():
    """
    Check the functionality of `Sentence` class.
    """
    s_obj = Sentence('happy new 7e@r 2024')
    print(s_obj.sentence)
    s_obj.only_integers()
    print(s_obj.sentence)

    d_obj = Sentence('hello im nalin here')
    print(d_obj.sentence)
    word_lst = ['im', 'here']
    d_obj.filter_words(word_lst)
    print(d_obj.sentence)

    f_obj = Sentence('hello im nalin here')
    print(f_obj.sentence)
    word_lst = ['ill', 'her', 'tap']
    f_obj.filter_words(word_lst)
    print(f_obj.sentence)


main()
