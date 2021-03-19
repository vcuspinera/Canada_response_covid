# authors: Leo Cuspinera and Victor Cuspinera
# date: 2021-03-01

'''Script that use SpaCy sentiment analysis for polarity and subjectivity of tweets.  

Usage: tweets_sentiment.py --input_file=<input_file> --output_dir=<destination_dir_path>

Example:
    python src/tweets_sentiment.py --input_file=tweets/tweets_db_clean.json --output_dir=tweets/

Options:
--input_file=<input_file> File with the preprocessed tweets (tweets_db_clean.json)
--output_dir=<destination_dir_path> Directory to save tweets' sentiment (tweets_sentiment.json)
'''

# Libraries
import pandas as pd
import numpy as np
import os
import spacy
from spacytextblob.spacytextblob import SpacyTextBlob
import time
from docopt import docopt

opt = docopt(__doc__)

def main(input_file, output_dir):
    print("\n--- START: tweets_sentiment.py ---")
    start = time.time()

    # Directories check    
    #assert os.path.exists(input_dir), "The path entered for input_file does not exist. Make sure to enter correct path \n"
    assert os.path.exists(output_dir), "The path entered for output_dir does not exist. Make sure to enter correct path \n"

    # Open tweets
    print("Loading: open the Json file with preprocessed tweets.")
    df = pd.read_json(input_file)

    # Add variables
    print("Variables: add date, announcement, and select only english tweets.") 
    df['day'] = [df['date'][i].strftime("%Y-%m-%d") for i in range(len(df))] # add day
    df['announcement'] = ["before" if i<"2020-03-11" else "after" for i in df['day']] # boolean variable of the Accouncement
    df = df[df['lang']=='en'].reset_index(drop=True) # select only tweets in English
    # Note: We keep 85.5% of the tweets, and we could use different packages for sentiment 
    # analysis and tokens in English.
    my_size = len(df)

    # Run sentiment of tweets
    print('Sentiment: gets the polarity and subjectivity of tweets. ⚠️  this step could take time, please be patient.')
    i = 0
    n = 200_000

    for i in range(int(my_size / n) + 1):
        start_sub = time.time()
        df_sub = df[n*i : n*(i+1)].reset_index(drop=True)
        aux = sentimenter(df_sub.tweet)
        result = pd.concat([df_sub, aux], axis=1)

    # Save new file
        #print('Saving: saves the tweets\' sentiment.')
        result.to_json(output_dir + 'tweets_sentiment_' + str(i) + '.json')
        print("  - Batch time: time used for batch", i, ":", np.round((time.time() - start_sub)/60, 2), "minutes.")

    print("Total time: time used to run tweets_sentiment.py:", np.round((time.time() - start)/60, 2), "minutes.")
    print("--- END: tweets_sentiment.py ---\n")
    return

def sentimenter(text):
    """
    Function that given a list with sentences or tweets returns a 
    list with two numbers for each sentences representing the
    polarity (score as a float within the range [-1.0, 1.0]) and 
    subjectivity (that is a float within the range [0.0, 1.0] 
    where 0.0 is very objective and 1.0 is very subjective).

    Parameters
    -------------
    text : (list)
        list where each element is a sentence or tweet.

    Returns
    -------------
    (DataFrame) two-column data frame with polarity and subjectivity.

    Example
    -------------
    example = ["Contact me at george23@gmail.com",
           "@vcuspinera my webpage is https://vcuspinera.github.io"]
    preprocess(example)
    (output:) ['contact me at',
               'my webpage is']
    """
    nlp = spacy.load('en_core_web_sm')
    spacy_text_blob = SpacyTextBlob()
    nlp.add_pipe(spacy_text_blob)

    result = [[nlp(tw)._.sentiment.polarity, nlp(tw)._.sentiment.subjectivity] for tw in text]
    result = pd.DataFrame(result).rename(columns={0:'polarity', 1:'subjectivity'})
    return result

if __name__ == "__main__":
    main(opt["--input_file"], opt["--output_dir"])
