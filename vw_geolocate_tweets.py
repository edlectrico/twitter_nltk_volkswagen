# -*- coding: utf-8 -*-
import pandas as pd
import sys
import re

# Input DataFrames
vw_original = pd.read_csv('output/vw_clean_en_rechecked.csv')
locations = pd.read_csv('output/cities_geo.csv')

vw = pd.DataFrame(data=vw_original)
cities = pd.DataFrame(data=locations)
# Output DataFrame
vw_geo = pd.DataFrame(columns=['id', 'location', 'country_code', 'latitude', 'longitude'])

cities_found = 0

for c_index, c_row in cities.iterrows():
  try:
    city = str(c_row['city']).lower().replace(" ", "") # cities may be written in a different way in each dataset
    clean_city = re.sub('\W+','', city)
    for vw_index, vw_row in vw.iterrows():
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
    print('KeyboradInterrupt exception raised: Generating output/vw_clean_en_geo.csv')
    vw_geo.to_csv('output/vw_clean_en_geo.csv')
    sys.exit()

print('Writing to output/vw_clean_en_geo.csv')
vw_geo.to_csv('output/vw_clean_en_geo.csv')
