#!/usr/bin/python

import sys

import dictionary

def print_usage():
    print """Usage:
    %(script)s [word]
    """ % \
        {
            "script"    : sys.argv[ 0 ]
        }

if __name__ == '__main__':
    if len( sys.argv ) < 2:
        print_usage()
        sys.exit( 1 )

    # load the currently saved dictionary
    phonetic_dictionary = dictionary.dictionary()
    phonetic_dictionary.load(
        filename = 'dictionary.json'
        )

    # calculate the value of the word
    value = phonetic_dictionary.calculate_word_value(
        sys.argv[ 1 ],
        values_filename = 'values.json'
        )
    print "Word has value '%(value)d'" % \
        {
            'value' : value
        }

    # find similar words
    if str( value ) in phonetic_dictionary.dictionary:
        # print them out
        words = phonetic_dictionary.dictionary[ str( value ) ]
        print 'The following matches were found:'
        for word in words:
            print '\t' + word
    else:
        # no similar words
        print 'No similar words found in dictionary'

