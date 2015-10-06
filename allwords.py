import pandas as pd
import os
import sys
from nltk.corpus import wordnet

input_csv = pd.read_csv('output/vw_clean_en_rechecked.csv')
input_df = pd.DataFrame(data=input_csv)

input_classified_csv = pd.read_csv('output/vw_classified.csv')
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
        # print(str(classification))
        # break
        final_classification = 'pos'
        if 'neg' in str(classification):
          final_classification = 'neg'
        output_df = output_df.append({'id':row['id'], 'word':word, 'classification':final_classification}, ignore_index=True)
  except KeyboardInterrupt:
    print('Exiting...')
    output_df.to_csv('output/allwords_classified_by_tweet.csv')
    sys.exit()

output_df.to_csv('output/allwords_classified_by_tweet.csv')
