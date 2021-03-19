# Historic tweets
This folder will storage the historic tweets from February 1st to April 30th of 2020, from the Government of Canada's official accounts:

- [@Canada](https://twitter.com/canada?lang=en). Showcasing Canada to the world. Twitter.
- [@JustinTrudeau](https://twitter.com/JustinTrudeau?s=20). Official account of Justin Trudeau as public person, and 23rd Prime Minister of Canada. Twitter.
- [@CanadianPM](https://twitter.com/CanadianPM). Official account of the Prime Minister of Canada. Twitter.
- [@GovCanHealth](https://twitter.com/govcanhealth?lang=en). Health Canada and Public Health Agency of Canada. Twitter.

Additionally to this _README.md_ and _twitter_supported_languages.csv_ files, after running all notebooks and scripts from the [`src` folder of this repository](https://github.com/vcuspinera/Canada_response_covid/tree/master/src), this folder will populate with:
- 360 JSON files with the raw tweets from the the four official Canadian Government accounts mentioned above.
- `tweets_db.json` file that gather the 360 previous files in one total document, selecting some of the variables useful for the analysis.
- `tweets_db_clean.json` file with the preprocessed tweets from `tweets_db.json`.
- 10 JSON files named as `tweets_sentiment_X.json` with the preprocessed tweets in english, that cointain the scores for sentiment analysis of tweets.
- `tweets_db_sentiment.json` merges the ten previous files that contain twees' sentiment in one file.
