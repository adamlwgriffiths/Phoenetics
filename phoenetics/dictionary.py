import json

class dictionary( object ):
    
    def __init__( self ):
        super( dictionary, self ).__init__()

        self.dictionary = {}
    
    def load( self, filename = 'dictionary.json' ):
        """
        Load an existing dictionary file.
        """
        with open( filename, 'r') as f:
            self.dictionary = json.loads( f.read() )
    
    def save( self, filename = 'dictionary.json' ):
        """
        Write the currently loaded dictionary to a file.
        """
        with open( filename, 'w' ) as f:
            f.write(
                json.dumps(
                    self.dictionary,
                    sort_keys = True,
                    indent = 4
                )
             )
    
    def create(
        self,
        words_filename = 'words.json',
        values_filename = 'values.json'
        ):
        """
        Load the words and values files and calculate
        a new dictionary.
        """
        with open( words_filename, 'r' ) as f:
            words = json.loads( f.read() )
        with open( values_filename, 'r' ) as f:
            values = json.loads( f.read() )

        self.dictionary = {}

        # iterate through each word in our words file
        for word in words:
            try:
                # get the value for the word
                value = self.calculate_word_value(
                    word,
                    values
                    )

                # add the word and its value to our dictionary
                if value not in self.dictionary:
                    self.dictionary[ value ] = []
                self.dictionary[ value ].append( word )

                print 'Added word %(word)s' % \
                    {
                        'word'      : word
                    }

            except KeyError:
                # skip to the next word
                pass
            
    def calculate_word_value(
        self,
        word,
        values = None,
        values_filename = 'values.json'
        ):
        # ensure we have our values loaded
        if values == None:
            with open( values_filename, 'r' ) as f:
                values = json.loads( f.read() )

        value = 0
        try:
            # for each letter in the word
            for letter in word:
                # find the character in our values list
                value += values[ letter ]
        except KeyError as e:
            # thrown if the letter is not in our lookup file
            print "Letter '%(letter)s' not found in values file '%(values)s" % \
                {
                    'letter'    : letter,
                    'values'    : values_filename
                }
            raise
        return value
    

