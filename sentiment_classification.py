import sentiment_mod as s
import tweet_preprocessor as prep

import pandas as pd
import sys

def classify_tweets(language):
  input_lang = language[0].lower()

  vw_original = pd.read_csv('output/vw_clean_' + input_lang + '_rechecked.csv')
  vw = pd.DataFrame(data=vw_original)

  vw_out = pd.DataFrame(columns=['id', 'classification'])

  for index, row in vw.iterrows():
    try:
      if len(str(row['text']).split()) > 1:
        print (s.sentiment(str(row['text'])))
        vw_out = vw_out.append({'id':str(row['id']),
  			'classification':str(s.sentiment(str(row['text']))[0])},
  			ignore_index = True)
    except KeyboardInterrupt:
      print('Writing to file...output/vw_classified_' + input_lang + '.csv')
      vw_out.to_csv('output/vw_classified_' + input_lang + '.csv')
      sys.exit()

  print('Writing to file...output/vw_classified_' + input_lang + '.csv')
  vw_out.to_csv('output/vw_classified_' + input_lang + '.csv')

if __name__ == '__main__':
  classify_tweets(sys.argv[1:])