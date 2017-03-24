# -*- coding: utf-8 -*-

"""This is the entry point of the program."""
from collections import Counter

def detect_language(text, languages):
    words_appearing = 0
    selected_language = None
    """Returns the detected language of given text."""
    for language in languages:
        words = len([word for word in language['common_words'] if word in text])
        if words > words_appearing:
            words_appearing = words
            selected_language = language['name']
        
    return selected_language
   

def most_common_word(text):
    words = text.split()
    counted_words = Counter(words)
    most_common = counted_words.most_common(1)[0][0]
    return most_common


def percentage_of_language(text, languages):
    words = text.split()
    percent_dict = {}
    percentages = ""

    #return percentage of each language
    for language in languages:
        lang_words = [word for word in language['common_words'] if word in text]
        percentage = 100 * len(lang_words)/len(words)
        percent_dict[language['name']] = "%.2f" % percentage
    
    for key, val in percent_dict.items():
        percentages += key + ": "+val+"\n"
        
    return percentages