"""Regex, yay."""
import re


def find_words(text: str) -> list:
    """Given string text, return all the words in that string."""
    new_list = []
    pattern = r"[A-ZÕÄÖÜ][a-zõäöü]+"
    for match in re.finditer(pattern, text):
        found_words = match.group()
        new_list.append(found_words)
    return new_list


print(find_words("Tomat,Apelsin,mandarin,Klaviatuur,arvuti,Äike,Päike"))


def find_words_with_vowels(text: str) -> list:
    """Given string text, return all the words in that string that start with a vowel."""
    new_list = []
    pattern = r"[AEIOUÕÄÖÜ][a-zõäöü]+"
    for match in re.finditer(pattern, text):
        found_words = match.group()
        new_list.append(found_words)
    return new_list


print(find_words_with_vowels("Tomat,Apelsin,mandarin,Klaviatuur,arvuti,Äike,Päike"))


def find_sentences(text: str) -> list:
    """Given string text, return all sentences in that string."""
    new_list = []
    pattern = r"([A-ZÕÄÖÜ][^\.!?]*[\.!?]+)"
    for match in re.finditer(pattern, text):
        found_words = match.group()
        new_list.append(found_words)
    return new_list


print(find_sentences("See on:esimene lause! See lause on 2. Aga see läuse on - kolmas! Äga see neljas. aga see viies."))


def find_words_from_sentence(sentence: str) -> list:
    """Given a sentence, return all words in that sentence."""
    new_list = []
    pattern = r"\w+"
    for match in re.finditer(pattern, sentence):
        found_words = match.group()
        new_list.append(found_words)
    return new_list


print(find_words_from_sentence("Minu nimi on - uljana."))


def find_words_from_sentences_only(text: str) -> list:
    """Given string text, return all words in that string that are a part of a sentence in that string."""
    new_list = []
    sentences_only = find_sentences(text)
    print(sentences_only)
    for sentences in sentences_only:
        words_only = find_words_from_sentence(sentences)
        for word in words_only:
            new_list.append(word)
    return new_list


print(find_words_from_sentences_only("Minu nimi on uljana. Python is my fav language!!! I love Python!  ffff44 I love coding. HHhh. ldhrö 3300blabla bla abdscjdll"))


def find_years(text: str) -> list:
    """Given string text, return a list of all 4-digit numbers (years) in that string."""
    new_list = []
    pattern = r"(?<!\d)\d{4}(?!\d)"
    for match in re.finditer(pattern, text):
        found_words = match.group()
        new_list.append(int(found_words))
    return new_list


print(find_years("1998, 1998, 7777, 1234"))


def find_phone_numbers(text: str) -> dict:
    new_dict = dict
    pattern = "(\+\d{3} *)?(\d{7,8})"
    for match in re.finditer(pattern, text):
        number = match.group(2)
        index = match.group(1)
        print(index, number)




print(find_phone_numbers("+372 56887364  +37256887363  +33359835647  56887365 +11 1234567 +327 1 11111111"))
