import pandas as pd
import numpy as np


## 1. Разобраться, как использовать мультииндексные ключи в конкретном примере
index=[
    ('city_1', 2010, 1),
    ('city_1', 2010, 2),

    ('city_1', 2020, 1),
    ('city_1', 2020, 2),

    ('city_2', 2010, 1),
    ('city_2', 2010, 2),

    ('city_2', 2020, 1),
    ('city_2', 2020, 2),

    ('city_3', 2010, 1),
    ('city_3', 2010, 2),

    ('city_3', 2020, 1),
    ('city_3', 2020, 2),]

population=[
    101,
    1010,
    201,
    2010,
    102,
    1020,
    202,
    2020,
    103,
    1030,
    203,
    2030
]
index = pd.MultiIndex.from_tuples(index)
pop = pd.Series(population, index=index)

pop_df = pd.DataFrame(
    {
        'total': pop,
        'something':
        [10,
        11,
        12,
        13,
        14,
        15,
        16,
        17,
        18,
        19,
        20,
        21]
    }
)

print(pop_df)
print(pop_df['something'])
print(pop_df.loc['city_2':'city_3'][['total']])
print(pop_df.loc['city_2', 2010][['total']])
print(pop_df.loc['city_2', 2010, 1][['total']])
print(pop_df.loc['city_1':'city_3', :, 1][['total']])
print(pop_df.loc[['city_1', 'city_3'], :, 1][['total', 'something']])
print(pop_df.loc[['city_1', 'city_3']][['total', 'something']])


## 2. Из получившихся данных выбрать данные по 
# - 2020 году (для всех столбцов)
# - job_1 (для всех строк)
# - для city_1 и job_2

index = pd.MultiIndex.from_product(
    [
        ['city_1', 'city_2'],
        [2010, 2020],
    ],
    names=['city', 'year']
)

columns = pd.MultiIndex.from_product(
    [
        ['person_1', 'person_2', 'person_3'],
        ['job_1', 'job_2']
    ],
    names=['worker', 'job']
)

rng = np.random.default_rng(1)
data = rng.random((4, 6))

data_df = pd.DataFrame(data, index=index, columns=columns)
print(data_df)
print(data_df.loc[:, 2020, :])

print(data_df[:]['job_1'])
print(data_df.xs('job_1', level='job', axis=1))
print(data_df.loc[:, pd.IndexSlice[:, 'job_1']])

print(data_df.loc['city_1'][:]['job_2'])
print(data_df.loc['city_1'].xs('job_2', level='job', axis=1))
print(data_df.loc['city_1', pd.IndexSlice[:, 'job_2']])


## 3. Взять за основу DataFrame со следующей структурой (как в номере 2)
# Выполнить запрос на получение следующих данных
# - все данные по person_1 и person_3
# - все данные по первому городу и первым двум person-ам (с использование срезов)
# Приведите пример (самостоятельно) с использованием pd.IndexSlice

print(data_df[['person_1', 'person_3']])
print(data_df.loc['city_1']['person_1':'person_2'])

print(data_df.loc[:, pd.IndexSlice[['person_1', 'person_3']]])
print(data_df.loc['city_1', pd.IndexSlice['person_1':'person_2']])


#4. Привести пример использования inner и outer джойнов для Series

ser1 = pd.Series(['a', 'b', 'c'], index=[1,2,3])
ser2 = pd.Series(['d', 'f', 'e'], index=[2,3,4])
print (pd.concat([ser1, ser2], axis=1)) # join='outer' по умолчанию
print (pd.concat([ser1, ser2], join='outer', axis=1)) # объединяет все индекся записывая NaN в пропуски
print (pd.concat([ser1, ser2], join='inner', axis=1)) # объединяет только совпадающие индексы