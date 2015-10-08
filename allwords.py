import pandas as pd
import os
import sys
from nltk.corpus import wordnet

def generate_all_words(language):
  input_lang = language[0].lower()

  input_csv = pd.read_csv('output/vw_clean_' + input_lang + '_rechecked.csv')
  input_df = pd.DataFrame(data=input_csv)

  input_classified_csv = pd.read_csv('output/vw_classified_'+ input_lang + '.csv')
  input_classified_df = pd.DataFrame(data=input_classified_csv)

  output_df = pd.DataFrame(columns=['id', 'word', 'classification'])

  for index, row in input_df.iterrows():
    try:
      row_words = str(row['text'])
      words = row_words.split(' ')
      for word in words:
        if wordnet.synsets(word):
          classification_row = input_classified_df.loc[input_classified_df['id'] == row['id']]
          classification = classification_row['classification']
          final_classification = 'pos'
          if 'neg' in str(classification):
            final_classification = 'neg'
          output_df = output_df.append({'id':row['id'], 'word':word, 'classification':final_classification}, ignore_index=True)
    except KeyboardInterrupt:
      print('Writing to...output/allwords_classified_by_tweet_' + input_lang + '.csv')
      output_df.to_csv('output/allwords_classified_by_tweet_' + input_lang + '.csv')
      sys.exit()

  print('Writing to...output/allwords_classified_by_tweet_' + input_lang + '.csv')
  output_df.to_csv('output/allwords_classified_by_tweet_' + input_lang + '.csv')

if __name__ == '__main__':
  generate_all_words(sys.argv[1:])