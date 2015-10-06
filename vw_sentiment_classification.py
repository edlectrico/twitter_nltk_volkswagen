import sentiment_mod as s
import tweet_preprocessor as prep

import pandas as pd
import sys

vw_original = pd.read_csv('output/vw_clean_en_rechecked.csv')
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
    print('Writing to file...')
    vw_out.to_csv('output/vw_classified.csv')
    sys.exit()

print('Writing to file...')
vw_out.to_csv('output/vw_classified.csv')
