#!/usr/bin/python3


"""
This is the module level doctstring

This module provide the function text_indentation(...)
to print text

"""
def text_indentation(text):
    """""prints a text after each of these characters: ., ? and :"""
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    else:
        i = 0
        size = len(text)
        while i < size:
            if text[i] == "." or text[i] == "?" or text[i] == ":":
                print("{}".format(text[i]), end="")
                print(1 * "\n")
                if text[i + 1] == " ":
                    i += 2
                    continue
                i += 1
            print("{}".format(text[i]), end="")
            i += 1
