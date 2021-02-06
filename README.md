# coup-prediction
Проект "Предсказание государственного переворота" на Зимней Школе CompTech 2021
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
`Задача:` предсказать, насколько вероятен госпереворот в той или иной стране и насколько он будет успешен, на основании исторических данных.

Запускать нужно файл CoupPrediction/manage.py

## Папки

`.github/workflows` - код для github actions. который срабатывает при каждом push в репозиторий и отправляет весь код, лежащий в репе, на сайт

`CoupPrediction` - CoupPrediction, который содержит в себе настройки Django и настройки сервера и CoupPredictionApp, который отвечает за всё, что связано с отображением и работой сайта

`Plotly Map + data` - отрисованная географическая карта по странам и данные по населению

`coup_detat` - вычисление частот и сглаженных частот по странам, обработанные данные по странам 

`data` - собранный датасет по странам, регионам и населению

`models`- baseline-модель на основе статистики

`reign` - данные(режим, лидеры государств)


## Ресурсы

https://databank.illinois.edu/datasets/IDB-0433268 - датасет переворотов с документацией

https://www.oefresearch.org/activities/coup-cast - сайт с предсказанием государственных переворотов


