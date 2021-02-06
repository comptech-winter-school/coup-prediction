import pandas as pd

def data_preprocess(filename, start_year, end_year, periorised=False):
    dataset = pd.read_csv(filename, encoding='utf-8', delimiter=',', error_bad_lines=False)
    # убираем уже не существующие страны
    old_countries = ['Czechoslovakia', 'Yemen PDR', 'USSR']
    clean_data = dataset.copy()
    for c in old_countries:
        clean_data = clean_data[clean_data.country != c]
    # учёт разных названий одной и той же страны
    clean_data = clean_data.replace(
        to_replace={'Yemen': 'Yemen Arab Republic', 'Swaziland': 'Eswatini', 'Ecudaor': 'Ecuador',
                    'Kyrgyz Republic': 'Kyrgyzstan', "Cote d'Ivoire": 'Ivory Coast',
                    'Congo': 'Democratic Republic of the Congo'})
    # запись фрейма в файл
    # госперевороты для заданного периода
    if periorised:
        data_filtered = clean_data[clean_data['year'] > int(start_year)]
        data_filtered = data_filtered[data_filtered['year'] > int(end_year)]
        data = data_filtered
    else:
        data = clean_data
    # сортировка стран по алфавиту
    data_country_filtered = data.sort_values('country', ascending=True)
    return data_country_filtered


class StasticsModel:

    def __init__(self, etalon_file: str, dataset_file_path: str, start_year: str, end_year: str):
        self.start_year = start_year
        self.end_year = end_year
        self.result_path = 'data/probas_for_coup_detait_with_un' + str(end_year) + '.csv'
        self.etalon_dataset = data_preprocess(etalon_file, self.start_year, self.end_year)
        self.dataset_file = dataset_file_path
        self.a = 0.1
        self.p_month = list()
        self.p_year = list()
        self.p_year_smooth = list()
        self.p_month_smooth = list()

    def get_file_with_predicted_probas(self):
        result_data = self._get_result_frame()
        result_data.to_csv(self.result_path, encoding='utf-8')

    def predict(self, country_name: str) -> str:
        result_frame = self._get_result_frame()
        result_frame_filtered = result_frame[result_frame.country == country_name]
        result_proba = result_frame_filtered['p_year_smooth']
        return str(result_proba)

    def _compute_probas(self):
        # частотность переворотов за последние 30 лет
        # количество переворотов == количество строчек с этой страной
        data_filtered = data_preprocess(self.dataset_file, self.start_year, self.end_year, periorised=True)
        data_country_numbered = data_filtered.groupby('country').count()
        coup_numbers = list(data_country_numbered['coup_id'])
        # таблица для записи итоговых данных
        self.result_coup_data = pd.DataFrame({'country': data_filtered['country'].unique(), 'coup_num': coup_numbers},
                                             columns=['country', 'coup_num'])

        for num in self.result_coup_data['coup_num']:
            self.p_month.append(num / 600 * 100)
        # частоты по годам
        for num in self.result_coup_data['coup_num']:
            self.p_year.append(num / 50 * 100)

        self._write_values_to_column('p_month', self.p_month)
        self._write_values_to_column('p_year', self.p_year)
        # сглаженные частоты по месяцам
        m = self.result_coup_data['p_month'].mean()
        for p in self.result_coup_data['p_month']:
            self.p_month_smooth.append((1 - self.a) * p + self.a * m)
        # сглаженные частоты по годам
        m = self.result_coup_data['p_year'].mean()
        for p in self.result_coup_data['p_year']:
            self.p_year_smooth.append((1 - self.a) * p + self.a * m)
        # запись значение в фрейм
        self._write_values_to_column('p_month_smooth', self.p_month_smooth)
        self._write_values_to_column('p_year_smooth', self.p_year_smooth)

        return self.result_coup_data

    def _write_values_to_column(self, column_name: str, values_list: list):
        self.result_coup_data[column_name] = values_list

    def _get_result_frame(self):
        result_data_with_un = self._compute_probas().copy()
        # добавляем в список стран, которых не было в Coup d'etait
        list_for_adding = list(set(self.etalon_dataset['country']) - set(self.result_coup_data['country']))
        # частоты для них проставляем средние
        p_month_smooth_average = self.result_coup_data['p_month_smooth'].mean()
        p_month_average = self.result_coup_data['p_month'].mean()
        p_year_smooth_average = self.result_coup_data['p_year_smooth'].mean()
        p_year_average = self.result_coup_data['p_year'].mean()
        coup_average = self.result_coup_data['coup_num'].mean()
        data_un = pd.DataFrame(
            {'country': list_for_adding, 'coup_num': coup_average, 'p_month': p_month_average, 'p_year': p_year_average,
             'p_year_smooth': p_year_smooth_average, 'p_month_smooth': p_month_smooth_average},
            columns=['country', 'coup_num', 'p_month', 'p_year', 'p_year_smooth', 'p_month_smooth'])
        result_data_with_un = result_data_with_un.append(data_un, ignore_index=True)
        return result_data_with_un


if __name__ == '__main__':
    model = StasticsModel('../data/etalon_country_list.csv', 'data/Coup_Data_v2.0.0.csv', '1989', '2015')
    model.get_file_with_predicted_probas()
