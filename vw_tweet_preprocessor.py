# -*- coding: utf-8 -*-
import language_detector as lang_detector
import tweet_preprocessor as preprocessor

import pandas as pd
import sys

vw_original = pd.read_csv('input/vw_clean_en.csv')
vw = pd.DataFrame(data=vw_original)

vw_out = pd.DataFrame()

for index, row in vw.iterrows():
  try:
    if len(str(row['text']).split()) > 1:
      if lang_detector.detect_language(str(row['text'])) == 'english':
        if not (str(row['text'])).lower().startswith('rt'): # we avoid RT
          text = preprocessor.process_tweet(str(row['text'])).replace('volkswagen', ' ').replace('vw', ' ')
          # vw_out = vw_out.append(row)
          vw_out = vw_out.append({'id':row['id'], 'created_at':row['created_at'],
				'name':row['name'], 'screen_name':row['screen_name'],
				'verified':row['followers_count'], 'friends_count':row['friends_count'],
				'text':text, 'description':row['description'],
				'lang':row['lang'], 'time_zone':row['time_zone'],
				'location':row['location']}, ignore_index = True)


  except KeyboardInterrupt:
    print 'Generating file'
    vw_out.to_csv('output/vw_clean_en_rechecked.csv')
    sys.exit()

print 'Generating file'
vw_out.to_csv('output/vw_clean_en_rechecked.csv')

