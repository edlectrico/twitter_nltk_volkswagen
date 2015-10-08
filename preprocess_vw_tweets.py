import language_detector as lang_detector
import tweet_preprocessor as preprocessor

import pandas as pd
import sys

# This method generates the vw_clean_en_rechecked.csv output file
# cleaning the input from input/vw_clean_en.csv
def generate_output(language):
  input_lang = language[0].lower()
  vw_in = pd.read_csv('input/vw_clean_' + input_lang + '.csv')
  df = pd.DataFrame(data=vw_in)

  vw_out = pd.DataFrame()
  lang = ''

  if str(input_lang).lower() == 'en':
    lang = 'english'
  else: 
    lang = 'spanish'

  print('Processing dataset in', lang)

  for index, row in df.iterrows():
    try:
      if len(str(row['text']).split()) > 1:
        if lang_detector.detect_language(str(row['text'])) == lang:
          if not (str(row['text'])).lower().startswith('rt'): # we avoid RT
            text = preprocessor.process_tweet(str(row['text'])).replace('volkswagen', ' ').replace('vw', ' ')
            vw_out = vw_out.append({'id':row['id'], 'created_at':row['created_at'],
				'name':row['name'], 'screen_name':row['screen_name'],
				'verified':row['followers_count'], 'friends_count':row['friends_count'],
				'text':text, 'description':row['description'],
				'lang':row['lang'], 'time_zone':row['time_zone'],
				'location':row['location']}, ignore_index = True)
    except KeyboardInterrupt:
      print('Generating file in', lang)
      vw_out.to_csv('output/vw_clean_' + input_lang + '_rechecked.csv')
      sys.exit()

  print('Generating file in', lang)
  vw_out.to_csv('output/vw_clean_' + input_lang + '_rechecked.csv')

if __name__ == '__main__':
  generate_output(sys.argv[1:])
