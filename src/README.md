# File description in this directory

Brief overview of each script and jupyter notebook in this directory in the order of their usage:

|Step |Script | Type | Usage |
|:---:|:------|:----:|:------|
|1A|[twitter-search_v1_TwitterAPI.ipynb](https://github.com/vcuspinera/Canada_response_covid/blob/master/src/twitter-search_v1_TwitterAPI.ipynb) | notebook |Search for tweets using Twitter API. 🚫 This notebook was not useful to retrieve historic tweets.|
|1B|[twitter-search_v2_GetOldTweets3.ipynb](https://github.com/vcuspinera/Canada_response_covid/blob/master/src/twitter-search_v2_GetOldTweets3.ipynb) | notebook |Search for tweets using GetOldTweets3. 🚫 However, this tool is not longer functioning.|
|1C|[twitter-search_v3_snscrape.ipynb](https://github.com/vcuspinera/Canada_response_covid/blob/master/src/twitter-search_v3_snscrape.ipynb) | notebook |Search for tweets using snscrape. ✅ This notebook works well.|
|2|[preprocess.py](https://github.com/vcuspinera/Canada_response_covid/blob/master/src/preprocess.py) | script |Identify sensible information from tweets and performs the customed preprocess. |
|3|[eda.ipynb](https://github.com/vcuspinera/Canada_response_covid/blob/master/src/eda.ipynb) | notebook |Uses the preprocessed tweets to perform basic analysis and EDA. |
|4|[tweets_sentiment.py](https://github.com/vcuspinera/Canada_response_covid/blob/master/src/tweets_sentiment.py)| script |Script that use SpaCy sentiment analysis for polarity and subjectivity of tweets. |
|5|[sentiment_analysis.ipynb](https://github.com/vcuspinera/Canada_response_covid/blob/master/src/sentiment_analysis.ipynb) | notebook |Performs sentimen analysis on tweets. |
