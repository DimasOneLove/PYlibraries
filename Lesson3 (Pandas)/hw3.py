import numpy as np
import pandas as pd

## 1. Привести различные способы создания объектов типа Series
# Для создания Series можно использовать
# - списки Python или массивы NumPy
# - скалярные значения
# - словари
list1 = [1, 2, 3, 4, 5]
list1_series = pd.Series(list1)
print(list1_series)
np_arr = np.array(list1)
np_arr_series = pd.Series(np_arr, index=['a', 1, 'f', 5, 'pd'])
print(np_arr_series)

x1 = 10
x2 = 23
x3 = 12
x_series = pd.Series([x1,x2,x3])
print(x_series)

user_dict = {
    'name': 'Petr',
    'age': 28,
    'status': 'student',
    'balance': 1000
}
user_dict_series = pd.Series(user_dict)
print(user_dict_series)


## 2. Привести различные способы создания объектов типа DataFrame
## DataFrame. Способы создания:
# - через объекты Series
# - списки словарей
# - словари объектов Series
# - двумерный массив NumPy
# - структурированный массив NumPy

#1
s1 = pd.Series([1,2,3,4])
s2 = pd.Series(['a', 'b', 'c', 'd'])
s12 = pd.DataFrame([s1,s2])
print(s12)

#2
dict1 = {
    'player1': 'L.Messi',
    'player2': 'C.Ronaldo',
    'player3': 'Neymar JR'
}
dict2 = {
    'player1': 878,
    'player2': 924,
    'player3': 453
}
footballers = pd.DataFrame({
    'name': dict1,
    'goals': dict2
})
print(footballers)

#3
s1 = pd.Series([1,2,3,4])
s2 = pd.Series(['a', 'b', 'c', 'd'])
s12 = pd.DataFrame({
    's1': s1,
    's2': s2
})
print(s12)

#4
arr1 = np.array([[10,20,30,40],
                 [50,60,70,80],
                 [25,35,65,95]])
df = pd.DataFrame(arr1)
print(df)

#5
data = np.zeros(4, dtype = {
    'names':(
        'name', 'age'
    ),
    'formats':(
        'U10', 'i4'
    )
})
name = ['name1', 'name2', 'name3', 'name4']
age = [10, 20, 30, 40]
data['name'] = name
data['age'] = age
print(data)
df = pd.DataFrame(data)
print(df)


## 3. Объедините два объекта Series с неодинаковыми множествами ключей (индекс), так чтобы вметсто NaN было установлено значение 1
s1 = pd.Series({
    'person1': 'Ivan',
    'person2': 'Boris',
    'person3': 'Toby',
    'person4': 'Bob',
})
s2 = pd.Series({
    'person1': 19,
    'person2': 31,
    'person3': 12,
    'person5': 10,
})
df = pd.DataFrame({'name':s1, 'age': s2})
print(df)
print(df.fillna(1))


## 4. Переписать пример с транслированием для DataFrame так, чтобы вычитание происходило по столбцам
rng = np.random.default_rng(1)
A = rng.integers(0, 10, (3,4))
df = pd.DataFrame(A, columns=['a', 'b', 'c', 'd'])
print(df)
print(df - df.iloc[0, ::2])
print(df.sub(df['a'], axis=0))

## 5. На примере объектов DataFrame продемонстрируйте использование методов ffill() и bfill()
df = pd.DataFrame(
    [
        [1,2,3,np.nan,None,pd.NA],
        [1,2,3,None,5,6],
        [1,np.nan,3,None,np.nan,6],
    ]
)
print(df.ffill(axis=0)) # вместо Nan ставится предыдущее допустимое значение в столбце сверху вниз (если нет, то остается NaN)
print(df.ffill(axis=1)) # вместо Nan ставится предыдущее допустимое значение в строке слева направо
print(df.ffill(axis=1, limit=1)) # limit - кол-во пропусков подряд
print(df.ffill(axis=1, limit_area='inside')) # Заполнение происходит только между существующими (не пропущенными) значениями.Пропуски в начале или конце данных не заполняются.
print(df.ffill(axis=1, limit_area='outside')) # Заполнение происходит только в начале или конце данных. Пропуски между существующими значениями не заполняются.

print(df.bfill()) # заполняет пропущенные значения, используя следующее доступное значение после пропуска -> по умолчанию axis=0, т.е. заполнение снизу вверх в столбцах
print(df.bfill(axis=1)) # заполнение справа налево
# есть также параметры limit, limit_area