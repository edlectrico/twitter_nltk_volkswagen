import pandas as pd
import sys
import re

def geolocate_tweets(language):
  input_lang = language[0].lower()

  vw_in = pd.read_csv('input/vw_clean_' + input_lang + '.csv')
  locations = pd.read_csv('output/cities_geo.csv')
  vw_df = pd.DataFrame(data=vw_in)
  cities_df = pd.DataFrame(data=locations)

  vw_geo = pd.DataFrame(columns=['id', 'location', 'country_code', 'latitude', 'longitude'])

  cities_found = 0
  print('Processing dataset in', input_lang)

  for c_index, c_row in cities_df.iterrows():
    try:
      city = str(c_row['city']).lower().replace(" ", "") # cities_df may be written in a different way in each dataset
      clean_city = re.sub('\W+','', city)
      for vw_index, vw_row in vw_df.iterrows():
        vw_city = str(vw_row['location']).lower().replace(" ", "")
        clean_vw_city = re.sub('\W+','', vw_city)
        if clean_city in clean_vw_city:
          cities_found += 1
          print('Cities found:', cities_found)
	  # Now we append a new line to the output DataFrame containing
	  # the tweet id for future JOINS and the coordinates of the tweet
          vw_geo = vw_geo.append({'id':str(vw_row['id']), 
			'location':c_row['city'],
			'country_code':c_row['country_code'],
			'latitude':c_row['lat'], 
			'longitude':c_row['lon']}, 
			ignore_index=True)
    except KeyboardInterrupt:
      print('KeyboradInterrupt exception raised: Generating output/vw_clean_' + input_lang + '_geo.csv')
      vw_geo.to_csv('output/vw_clean_' + input_lang + '_geo.csv')
      sys.exit()

  print('Writing to output/vw_clean_' + input_lang + '_geo.csv')
  vw_geo.to_csv('output/vw_clean_' + input_lang + '_geo.csv')


if __name__ == '__main__':
  geolocate_tweets(sys.argv[1:])

