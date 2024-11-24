import pandas as pd

df = pd.read_csv('Introduction to Numpy and Pandas.csv')

print("Первые 5 строк данных:")
print(df.head())
print("\n")

print("Информация о данных:")
print(df.info())
print("\n")

print("Статистическое описание:")
print(df.describe())
print("\n")

avg_salary_by_city = df.groupby('City')['Salary'].mean()
print("Средняя зарплата по городам:")
print(avg_salary_by_city)

