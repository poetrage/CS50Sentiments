import nltk
# import helpers


class Analyzer():
    """Implements sentiment analysis."""

    def __init__(self, positives, negatives):

        self.positives = set()
        with open('positive-words.txt') as lines:
            for line in lines:
                if line.startswith(';') is False:
                    self.positives.add(line.rstrip('\n'))
            # file.close()# close is not needed if use with open

        self.negatives = set()
        with open('negative-words.txt') as lines:
            for line in lines:
                if line.startswith(';') is False:
                    self.negatives.add(line.rstrip('\n'))
        #    file.close()
        """Initialize Analyzer."""

        # TODO

    def analyze(self, text):
        """Analyze text for sentiment, returning its score."""

        # TODO
        # tokens = tokenizer.tokenize(tweet)
        tokenizer = nltk.tokenize.TweetTokenizer()
        tokens = tokenizer.tokenize(text)
        score = 0

        for word in tokens:
                # iterate over tokens#str.lower

            if word.lower() in self.positives:
                score = score+1

            elif word.lower() in self.negatives:
                score = score-1

            else:
                continue
        return score
