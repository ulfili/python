"""Regex, yay."""
import re


def find_words(text: str) -> list:
    """
    Given string text, return all the words in that string.

    A word here is considered to be any combination letters that starts with
    a capital letter and contains of at least one more lowercase letter.
    Note that Estonian õ, ä, ö and ü should also be accepted here.

    Words must be found using regex.

    :param text: given string
     find words from
    :return: list of words found in given string
    """
    new_list = []
    pattern = r"[A-ZÕÄÖÜ][a-zõäöü]*"
    for match in re.finditer(pattern, text):
        found_words = match.group()
        new_list.append(found_words)
    return new_list


print(find_words("Tomat,Apelsin,mandarin,Klaviatuur,arvuti,Äike,Päike"))


def find_words_with_vowels(text: str) -> list:
    """
    Given string text, return all the words in that string that start with a vowel.

    A word here is considered to be any combination letters that starts with
    a capital letter and contains of at least one more lowercase letter.
    Note that Estonian õ, ä, ö and ü should also be accepted here.

    Words must be found using regex.

    :param text: given string to find words from
    :return: list of words that start with a vowel found in given string
    """
    new_list = []
    pattern = r"[AEIOUÕÄÖÜ][a-zõäöü]*"
    for match in re.finditer(pattern, text):
        found_words = match.group()
        new_list.append(found_words)
    return new_list


print(find_words_with_vowels("Tomat,Apelsin,mandarin,Klaviatuur,arvuti,Äike,Päike"))


def find_sentences(text: str) -> list:
    """
    Given string text, return all sentences in that string.

    A sentence always starts with a capital letter and ends with punctuation (.!?).
    Note that a sentence may also contain all the typical symbols (like commas, colons, numbers, etc.).
    A sentence may also end in multiple punctuation (example: "Wait...").

    Sentences must be found using regex.

    :param text: given string to find sentences from
    :return: list of sentences found in given string
    """
    new_list = []
    pattern = r"([A-ZÕÄÖÜ][^\.!?]*[\.!?])"
    for match in re.finditer(pattern, text):
        found_words = match.group()
        new_list.append(found_words)
    return new_list


print(find_sentences("See on:esimene lause! See lause on 2. Aga see läuse on - kolmas! Äga see neljas. aga see viies."))


def find_words_from_sentence(sentence: str) -> list:
    """
    Given a sentence, return all words in that sentence.

    Here, a word is considered to be a normal word in a sentence,
    that is separated from other words by a whitespace (or commas, etc.).
    Note that numbers are also considered as words here, but commas, etc. are not
    a part of a word.

    Words must be found using regex.

    :param sentence: given sentence to find words from
    :return: list of words found in given sentence
    """
    new_list = []
    pattern = r"\w+"
    for match in re.finditer(pattern, sentence):
        found_words = match.group()
        new_list.append(found_words)
    return new_list


print(find_words_from_sentence("Minu nimi on - uljana."))
