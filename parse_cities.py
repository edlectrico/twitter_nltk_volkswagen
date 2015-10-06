import pandas as pd
import sys

cities1000 = pd.read_csv('../data/cities1000.txt', sep='\t')
cities_df = pd.DataFrame(data=cities1000)

cities_geo = pd.DataFrame(columns=['city', 'lat', 'lon', 'country_code'])

for index, row in cities_df.iterrows():
  try:
    cities_geo = cities_geo.append({'city':row['city'], 
				'lat':row['latitude'], 
				'lon':row['longitude'],
				'country_code':row['country_code']}, 
				ignore_index=True)
  except KeyboardInterrupt:
    print('Printing to file...')
    cities_geo.to_csv('output/cities_geo.csv')
    sys.exit()

print('Printing to file...')
cities_geo.to_csv('output/cities_geo.csv')

