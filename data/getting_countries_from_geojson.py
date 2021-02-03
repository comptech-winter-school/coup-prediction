import json
import pandas as pd


def getting_coutries(map_path, csv_path):
    with open(map_path, encoding='utf-8') as file:
        geo_data = json.load(file)

    countries = list()
    for country in geo_data['features']:
        countries.append(country['properties']['geounit'])

    data = pd.DataFrame({'country': sorted(countries)}, columns=['country'])
    data.to_csv(csv_path, encoding='utf-8')


if __name__ == '__main__':
    getting_coutries('/Plotly Map + data/Custom.geo(middle).json', 'etalon_country_list.csv')
