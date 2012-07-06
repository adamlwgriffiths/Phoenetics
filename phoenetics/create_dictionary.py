#!/usr/bin/python

import dictionary

if __name__ == '__main__':
    phonetic_dictionary = dictionary.dictionary()
    phonetic_dictionary.create(
        words_filename = 'words.json',
        values_filename = 'values.json'
        )
    phonetic_dictionary.save(
        filename = 'dictionary.json'
        )

