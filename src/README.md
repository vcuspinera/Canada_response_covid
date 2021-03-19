# File description in this directory

Brief overview of each script and jupyter notebook in this directory in the order of their usage:

|Step |Script | Type | Expected time | Comment |
|:---:|:------|:----:|:-----|:------|
|1A|[twitter-search_v1_TwitterAPI.ipynb](https://github.com/vcuspinera/Canada_response_covid/blob/master/src/twitter-search_v1_TwitterAPI.ipynb) |  notebook | not registered | Search for tweets using `Twitter API`. <br>🚫 _This notebook was not useful to retrieve historic tweets._|
|1B|[twitter-search_v2_GetOldTweets3.ipynb](https://github.com/vcuspinera/Canada_response_covid/blob/master/src/twitter-search_v2_GetOldTweets3.ipynb) | notebook | not registered | Search for tweets using `GetOldTweets3` library. <br>🚫 _The `GetOldTweets3` library is no longer functioning._|
|1C|[twitter-search_v3_snscrape.ipynb](https://github.com/vcuspinera/Canada_response_covid/blob/master/src/twitter-search_v3_snscrape.ipynb) | notebook | 230-240 min. |Search for tweets using `snscrape` package. <br>✅ _Final and successful approach to download tweets._|
|2|[preprocess.py](https://github.com/vcuspinera/Canada_response_covid/blob/master/src/preprocess.py) | script | 100-110 min. | Identify sensible information from tweets and performs the customed preprocess. |
|3|[eda.ipynb](https://github.com/vcuspinera/Canada_response_covid/blob/master/src/eda.ipynb) | notebook | 1-2 min. | Uses the preprocessed tweets to perform basic analysis and EDA. |
|4|[twitter_trend.ipynb](https://github.com/vcuspinera/Canada_response_covid/blob/master/src/twitter_trend.ipynb)| notebook | 1 sec. | Explores Twitter Trends in Canada from March 10 to March 19, 2020, from the `GetDayTrends` webpage. |
|5|[cleaning_adds.ipynb](https://github.com/vcuspinera/Canada_response_covid/blob/master/src/cleaning_adds.ipynb)| notebook | 15 sec. | Look for Twitter's usernames published adds or repeats the same tweet several times. |
|6|[tweets_sentiment.py](https://github.com/vcuspinera/Canada_response_covid/blob/master/src/tweets_sentiment.py)| script | 200-210 min. | Script that use SpaCy sentiment analysis to get _polarity_ and _subjectivity_ of tweets. |
|7|[sentiment_analysis.ipynb](https://github.com/vcuspinera/Canada_response_covid/blob/master/src/sentiment_analysis.ipynb) | notebook | 1-2 min. | Performs sentiment analysis on tweets using descriptive statistics based in counts of words, word clouds, polarity and subjectivity scores. |

__Note__: If you are having problems opening any Jupyter Notebook, try to open it using [`nbviewer`](https://nbviewer.jupyter.org) online:
1. Open the [`nbviewer`](https://nbviewer.jupyter.org/) webpage: "https://nbviewer.jupyter.org/"
2. Paste the link of the Jypyter Notebook (e.g. "https://github.com/vcuspinera/Canada_response_covid/blob/master/src/sentiment_analysis.ipynb")
3. This will render the notebook! 🎉
