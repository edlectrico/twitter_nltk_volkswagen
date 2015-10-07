# Volkswagen emissions scandal worldwide reactions in Twitter

This project analyzes the opinions collected from Twitter regarding the volkswagen emissions scandal.

In this case, the data has been collected using a [Flume agent](http://blog.cloudera.com/blog/2012/10/analyzing-twitter-data-with-hadoop-part-2-gathering-data-with-flume/) (within its [Cloudera Big Data](http://www.cloudera.com/content/cloudera/en/home.html) infrastructure).

![Alt text](http://blog.cloudera.com/wp-content/uploads/2012/10/fig.png "Flume agent collecting tweets from Twitter")

## Input data
We have used only two files as inputs for this scenario:
* [cities1000.txt](input/cities1000.txt): A file downloaded from geonames (as open data) which includes information about each world city with more than 1,000 inhabitants. It includes the city name, its coordinates, and country code name.
* [vw_clean_en.csv](input/vw_clean_en.csv): A file which contains all the collected tweets. The file has been processed with [Hive](https://hive.apache.org/) to delete NULLs and to use only tweets in English. However, we'll see that this first "cleaning" process is not enough.

## Scripts description and execution order
### Intermediate scripts:
* [tweet_preprocessor.py](tweet_preprocessor.py): This script is not directly executable from command line. It is used by the vw_tweet_preprocessor.py script.
* [language_detector.py](language_detector.py): As the previous one, this script is just used by the vw_tweet_preprocessor.py script.

### Executable scripts:
* [vw_tweet_preprocessor.py](vw_tweet_preprocessor.py): This script takes the [vw_clean_en.csv](input/vw_clean_en.csv) input file and re-checks that the text of the tweet is not a RT, is not NULL, and it is writen in English. The output file is stored in [vw_clean_en_rechecked.csv](output/vw_clean_en_rechecked.csv).
* [parse_cities.py](parse_cities.py): It takes the [cities1000.txt](input/cities1000.txt) file and generates a new [cities_geo.csv](output/cities_geo.csv) with the city name, its coordinates, and its two-digit country code.
* [vw_geolocate_tweets.py](vw_geolocate_tweets.py): It generates an [vw_clean_en_geo.csv](output/vw_clean_en_geo.csv) file with the tweet and its location.

### Analysis scripts:
* [sentiment_train.py](sentiment_train.py): It trains several classification algorithms to choose the best option for the current case.
* [sentiment_mod.py](sentiment_mod.py): It uses the trained algorithms to classify the corresponding input data.
* [vw_sentiment_classification.py](vw_sentiment_classification.py): FInally, this script takes the [vw_clean_en_rechecked.csv](output/vw_clean_en_rechecked.csv) and uses sentiment_mod to classify the content of the tweet in a positive or negative way.
* [allwords.py](allwords.py): This script generates an output file with all the words analyzed and the corresponding tweet classification.

### Usage
* python3 vw_tweet_preprocessor.py en|es
* python3 parse_cities.py
* python3 vw_geolocate_tweets.py (this script takes even hours depending on the amount of collected tweets)
* python3 sentiment_train.py
* python3 sentiment_mod.py
* python3 allwords.py

## Necessary packages
* python3 (obvioysly)
* pip3 to install the following packages
* pandas
* nltk
* scikit-learn
 
PS: I highly recomend to use Python3 instead of Python2.x. Notice that if you use Python3 you'll need to install each package again with pip3, no matter if you have them already installed with Python2.x.
