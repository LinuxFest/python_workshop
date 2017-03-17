import pandas as pd

serie = pd.Series([0, 1, 4, 9, 16, 25], name='squares')
print(serie)
print('---------------')
print(serie.index)
print('---------------')
print(serie.values)
print('---------------')
print(serie.keys())
print('---------------')

serie1 = pd.Series([98.2, 97.3, 96.6, 96.1], index=['Java', 'C++', 'Python', 'C'])

serie2 = pd.Series([100, 99, 98, 97], index=['Java', 'C++', 'Python', 'C'])
print(serie2)
print(serie2[0], serie2['Java'])
print(serie2['Java':'C'])
print(serie2[serie2 > 98])

two_series = pd.DataFrame({'serie1': serie1, 'serie2': serie2})
print(two_series)
two_series.sort_values('serie2', ascending=False)
print(two_series)
two_series['average'] = 0.5 * (two_series['serie1'] + two_series['serie2'])
print(two_series)