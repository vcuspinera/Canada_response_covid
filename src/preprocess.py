# authors: Leo Cuspinera and Victor Cuspinera
# date: 2021-02-16

'''This script load tweets dataset, performs preprocessing on the comments,
and saves the dababase in a new file.  

Usage: preprocess.py --input_dir=<input_dir_path> --output_dir=<destination_dir_path>

Example:
    python src/preprocess.py --input_dir=tweets/ --output_dir=tweets/

Options:
--input_dir=<input_dir_path> Directory with the consolidated data (tweets_db.json)
--output_dir=<destination_dir_path> Directory for saving the preprocessed tweets (tweets_db_clean.json)
'''

# Libraries
import pandas as pd
import numpy as np
import os
import re
import spacy
import string
import time
import en_core_web_sm
nlp = en_core_web_sm.load()
from docopt import docopt

opt = docopt(__doc__)


def main(input_dir, output_dir):
    print("\n--- START: preprocess.py ---")
    start = time.time()

    # Directories check    
    assert os.path.exists(input_dir), "The path entered for input_dir does not exist. Make sure to enter correct path \n"
    assert os.path.exists(output_dir), "The path entered for output_dir does not exist. Make sure to enter correct path \n"

    # Open tweets
    print("Loading: open the Json file with all tweets")
    df_tot = pd.read_json(input_dir + 'tweets_db.json')

    # Run preprocess
    print('Preprocess: this step could take time, please be patient')
    df_tot['tweet'] = preprocess(df_tot['content'])

    # Save new file
    print('Saving: saves the preprocessed tweets')
    df_tot.drop('content', axis=1).to_json(output_dir + 'tweets_db_clean.json')

    print("Total time: time used to run preprocess.py:", np.round((time.time() - start)/60, 2), "minutes.")
    print("--- END: preprocess.py ---\n")
    return


def preprocess(text, irrelevant_pos = ['SPACE'],
              avoid_entities = ['ORG']):
    """
    Function that identify sensible information and delete some of 
    these data as emails and urls.
    Parameters
    -------------
    text : (list)
        the list of text to be preprocessed
    irrelevant_pos : (list)
        a list of irrelevant 'pos' tags
    avoid_entities : (list)
        a list of entity labels to be avoided

    Returns
    -------------
    (list) list of preprocessed text

    Example
    -------------
    example = ["Contact me at george23@gmail.com",
           "@vcuspinera my webpage is https://vcuspinera.github.io"]
    preprocess(example)
    (output:) ['contact me at',
               'my webpage is']
    """
    result = []

    for sent in text:
        sent = str(sent).lower()

        result_sent = []
        doc = nlp(sent)
        entities = [str(ent) for ent in doc.ents if ent.label_ in avoid_entities]
        # This helps to detect names organization

        for token in doc:            
            if (token.like_email or
                token.like_url or
                token.pos_ in irrelevant_pos or
                str(token) in entities
               ):
                continue
            else:
                if str(token) in string.punctuation:
                    try:
                        result_sent[-1] = str(result_sent[-1]) + str(token)
                    except:
                        result_sent.append(str(token))
                else:
                    result_sent.append(str(token))
        result.append(" ".join(result_sent))
    return result

if __name__ == "__main__":
    main(opt["--input_dir"], opt["--output_dir"])
