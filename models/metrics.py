# построить на данных до 2015 года
# c 2016 по 2020 тестирование
# roc_auc, acc, confusion_matrix
import pandas as pd
from sklearn.metrics import roc_curve
from sklearn.metrics import f1_score, confusion_matrix

dataset = pd.read_csv('data/Coup_Data_v2.0.0.csv', encoding='utf-8', delimiter=',', error_bad_lines=False)
predicted_dataset = pd.read_csv('data/probas_for_coup_detait_with_un.csv', encoding='utf-8', delimiter=',', error_bad_lines=False)
y_true =
y_pred = list(predicted_dataset['p_year'])


roc_curve(y_true, y_test)

F_mera = f1_score(y_test, predicted)
confusion_matrix(y_test, predicted))
