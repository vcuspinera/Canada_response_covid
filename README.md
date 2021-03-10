<img src="img/logo_canada_word_cloud.png" width="180" align = "right">

# Canada response to Covid-19
*Sentiment analysis of people's tweets referring to Canadian Government's accounts after Government announcement of policies as response of Covid-19.*

[![License:
MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## Authors
|Name |Github| Webpage |
|:----|:-----|:-------:|
|Victor Cuspinera | [vcuspinera](https://github.com/vcuspinera) | [<img src="/img/logo_vcuspinera.png" width=15%/>](https://vcuspinera.github.io) |
|Leopoldo Cuspinera | [cuspime](https://github.com/cuspime) | [<img src="/img/logo_cuspime.png" width=15%>](https://cuspime.github.io) |

## Overview
The idea of this project was born after March 27th, 2020, when the Prime Minister of Canada, Justin Trudeau, [announced a series of policies facing impacts of Covid-19](https://youtu.be/1o-tV0A87l8) to support small businesses and their employees.  

The objective of this project is to analyse the Canadian Government response to Covid-19 through the perception of the people by making sentiment analysis on people's tweets mentioning Canadian Government's accounts as [@JustinTrudeau](https://twitter.com/JustinTrudeau?s=20), [@CanadianPM](https://twitter.com/CanadianPM), [@Canada](https://twitter.com/canada?lang=en) and [@GovCanHealth](https://twitter.com/govcanhealth?lang=en).

## Retrieving tweets
To compare the tweets before and after Trudeau announcement, the first step was getting the tweets from March 1st to April 30th, from the four official-accounts selected from the Government of Canada.

### Getting the tweets
#### What didn't work: `Twitter API` and `GetOldTweets3` library
Our first attempt was using the [Twitter API](https://github.com/vcuspinera/Canada_response_covid/blob/master/src/twitter-search_v1_TwitterAPI.ipynb). For this reason, we get a twitter developer's account<sup><a name="myfootnote1">1</a></sup>. However, the standard twitter developer's account only gives access to search historic databases with a 7-day limit, which means we were not able to reach tweets that were older than a week and so this approach was discarded.

As a second approach we used the [GetOldTweets3 library](https://github.com/vcuspinera/Canada_response_covid/blob/master/src/twitter-search_v2_GetOldTweets3.ipynb), which initially gave us satisfactory results.
However due the changes in Twitter's API in late 2020, GetOldTweets3 is no longer functioning.

#### What worked for the current version of the project: `snscrape` library

Our final and successful approach to get the wanted tweets was using the [snscrape](https://github.com/vcuspinera/Canada_response_covid/blob/master/src/twitter-search_v3_snscrape.ipynb). 
<s>
This package allowed us to find old tweets as opposed to the free version of the API from twitter, and the GetOldTweets3 library that is non-currently working.
</s>

In this case, we use the development version of snscrape to access information directly from tweets instead of tweet URLs:
```
!pip3 install git+https://github.com/JustAnotherArchivist/snscrape.git
```

An important point is that this package works directly from the terminal with Command Line Interface (CLI) so, in this case, we didn't need to call it as a library but we use the OS library for Python to execute snscrape with CLI commands in Python. In the next code chunk, you could find how to use it in jupyter:

```python
# Libraries
import os
import pandas as pd

# Use OS library to call snscrape with CLI in Python and save tweets
os.system("snscrape --jsonl --max-results 1_000 --since 2020-05-01 twitter-search 'JustinTrudeau until:2020-05-02' > ../tweets/JustinTrudeau_2020-05-01.json")

# Call tweet's json files as Data Frame
df = pd.read_json('../tweets/JustinTrudeau_2020-05-01.json', lines=True)
```

With the snscrape package we download as many as 100,000 tweets per day for each Twitter account of the Government of Canada. This means that we got 244 `JSON` files, and stored them in [the _tweets_ folder](https://github.com/vcuspinera/Canada_response_covid/tree/master/tweets) of this repository.

Subsequently, we merged some selected columns of these files in one file named *tweets_db.json*

[⭐️ click here](https://github.com/vcuspinera/Canada_response_covid/blob/master/src/twitter-search_v3_snscrape.ipynb) to see more details about how we download tweets with `snscrape`.

### Preprocessing tweets
Our final step of this section was [preprocessing the tweets](https://github.com/vcuspinera/Canada_response_covid/blob/master/src/preprocess.py) to delete some of the sensible information as emails and urls.<sup><a name="myfootnote2">2</a></sup> You can run the preprocess.py script by writing in the Terminal at the main folder of this repository:

```
python src/preprocess.py --input_dir=tweets/ --output_dir=tweets/
```

## EDA
When comparing the tweets per day by Canadian Government Twitter accounts, we find that between March and April 2020, the [@Canada](https://twitter.com/Canada) account had between 29.1 and 62.4 thousand tweets per day, followed by [@JustinTrudeau](https://twitter.com/JustinTrudeau) in a range of 3.5 to 29.7 thousand tweets per day. With much fewer tweets, [@CanadianPM](https://twitter.com/CanadianPM) had between 131 and 1,207 tweets, and [@GovCanHealth](https://twitter.com/GovCanHealth) between 105 and 1,188 tweets per day.

<img src="img/EDA_1_tweets_per_day.png" width="600">

Most tweets were written in English -around 85% -, followed by Spanish and French. Notice that there's a large number of tweets have with an undefined language. For the main analysis we used tweets wrote in English. This enhanced the reach of powerful tools like [spacy](https://spacy.io), [textblob](https://textblob.readthedocs.io/en/dev/) and [wordcloud](https://amueller.github.io/word_cloud/index.html), mainly developed for this language.

<img src="img/EDA_2_proportion_by_language.png" width="550">

When normalizing the number of tweets by account, we can identify the days with more tweets. 
<span style="color:orange"> maybe some moving average here would be better? a 3 day window should suffice although a 7 days window would help remove weekly seasonality.
</span>
In the following plot we can identify a higher number of tweets in all Canadian Government's Twitter account between March 12 and March 29, 2020.

<img src="img/EDA_3_heatmap_weights.png" width="780">

⭐️ More details of the basic analysis and EDA of this report are available [in this link](https://github.com/vcuspinera/Canada_response_covid/blob/master/src/eda.ipynb).

## Sentiment Analysis
For sentiment analysis we select only tweets written in English, and use descriptive statistics based in counts of words, word clouds and scores get by [spaCy](https://spacy.io).

When comparing word clouds of tweets published before and after the announcement, we observe that the most used words and their repetitions are very similar among both groups.

<img src="img/sentiment_wordcloud.png" width="650">

Additionally, we explore sentiment analysis with [spaCy](https://spacy.io)'s `polarity` and `subjectivity`.<sup><a name="myfootnote3">3</a></sup>  

In this case, we observe that the information from tweets before and after the announcement have very similar Polarity and Subjectivity curves. Talking about polarity, in both groups we see mainly neutral tweets skewed to be positive. In the other hand, these tweets were much more objective than subjective. We also perform hypothesis testing polarity and subjectivity on tweets before and after the announcement on sub-samples of tweets, but we couldn't reject that both means of these measures were different.

sdf
<p style="color:blue">
I think a log scale for this very plot would be better, cause they're just too close to each other and the range of values is very big. There are some subjectivity outliers around 0. Is this normal???
More importantly,
here I would do something slightly different. I would not take the tweets before and after and divide them in 2 likt this. I think I would rather see a time series. So, I would prefer to see medians with bands that move through time (with a window average if it helps). This would help me better to "see" what happened. Maybe the difference was huge within 3 days and then it went back to normal?
</p> 

<img src="img/sentiment_polar_subject.png" width="750">

Finally, while the announcement didn't impact in the sentiment of tweets, it impacted in the volume of actions and reactions of users increasing the number of likes, replies, retweets and quotes, as we can find in the next plot.

<img src="img/sentiment_reactions.png" width="700">

[⭐️ click here](https://github.com/vcuspinera/Canada_response_covid/blob/master/src/sentiment_analysis.ipynb) to see more details about the sentiment analysis.

## Final comments
While the aim of this project was to compare the sentiment analysis of people before and after Trudeau's announcement on March 27th, 2020, where the Canadian Government was willing to support small businesses and employees after Covid-19 financial impact. We found out that the sentiment analysis didn't show any difference on tweets sent before and after the announcement; however, this event impact in the volume of tweets, actions and reactions of users.

## Dependencies
|Python packages|Python packages|
|:------|:---|
|altair |re  |
|collections|scipy |
|datetime|seaborn |
|docopt |spacy|
|en_core_web_sm|spacytextblob |
|GetOldTweets3 |string|
|json   |textblob |
|matplotlib |textblob |
|numpy  |time|
|os     |twitter|
|pandas |warnings|
|PIL    |wordcloud |
|pytz   | |

## Usage
### Running recipe (recommended)
To replicate the analysis, clone this GitHub repository and follow the next steps:

1. Install the [dependencies](#dependencies) listed above.  

2. Open [`twitter-search_v2_GetOldTweets3.ipynb`](https://github.com/vcuspinera/Canada_response_covid/blob/master/src/twitter-search_v3_snscrape.ipynb) notebook located in the _src_ folder, and run all cells.

3. Run the Python script [`preprocess.py`](https://github.com/vcuspinera/Canada_response_covid/blob/master/src/preprocess.py) in the terminal from the root directory of this project to identify and delete sensible information.
_⚠️ Caution: this process take around one hour._
```
python src/preprocess.py --input_dir=tweets/ --output_dir=tweets/
```

4. Open and run [`eda.ipynb`](https://github.com/vcuspinera/Canada_response_covid/blob/master/src/eda.ipynb) notebook located in the _src_ folder.

5. Run the Python script [`tweets_sentiment.py`](https://github.com/vcuspinera/Canada_response_covid/blob/master/src/tweets_sentiment.py) in the terminal to select only tweets written in English and add Polarity and Subjectivity scores from spaCy.  
_⚠️ Caution: [this process take a long time to run it, in my case it took 13 hr.](https://github.com/vcuspinera/Canada_response_covid/blob/master/img/tweets_sentiment_times.png)_
```
python src/tweets_sentiment.py --input_file=tweets/tweets_db_clean.json --output_dir=tweets/
```

6. Open and run [`sentiment_analysis.ipynb`](https://github.com/vcuspinera/Canada_response_covid/blob/master/src/sentiment_analysis.ipynb) notebook.

## Main references
- [Justin Trudeau – Prime Minister of Canada. (March 27, 2020). *Announcing support for small businesses facing impacts of COVID-19*. Retrieved: 2019-05-18](https://youtu.be/1o-tV0A87l8)
- [@JustinTrudeau](https://twitter.com/JustinTrudeau?s=20). Official account of Justin Trudeau as public person, and 23rd Prime Minister of Canada. Twitter.
- [@CanadianPM](https://twitter.com/CanadianPM). Official account of the Prime Minister of Canada. Twitter.
- [@Canada](https://twitter.com/canada?lang=en). Showcasing Canada to the world. Twitter.
- [@GovCanHealth](https://twitter.com/govcanhealth?lang=en). Health Canada and Public Health Agency of Canada. Twitter.

[⭐️ Click here](https://github.com/vcuspinera/Canada_response_covid/blob/master/References.md) to access the complete list of references for this project.

<br>

---
<sup>[[1]](#myfootnote1) If you are interested to get the twitter developer's account, [click here](https://github.com/vcuspinera/Canada_response_covid/tree/master/keys) to see details and recommendation to get one.</sup>

<sup>[[2]](#myfootnote2) We didn't delete all the sensible information nor anonymize the tweets because we loosed important tokens as _Trudeau_ or the tags to official Twitter accounts of Canadian Government.</sup>

<sup>[[3]](#myfootnote3) `polarity` score is a float within the range [-1.0, 1.0] where -1.0 is a very negative tweet and 1.0 is positive one. In the other hand, `subjectivity` is a float within the range [0.0, 1.0] where 0.0 is very objective and 1.0 is very subjective.</sup>
