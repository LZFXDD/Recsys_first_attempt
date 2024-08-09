import pandas as pd

dataset = {}

movies_path = r"D:\USTC\实验室\Reflexion_Recsys\pythonProject\ml-25m\movies.csv"
movies_dataset = pd.read_csv(movies_path, encoding='utf-8')

def extract_title_year(text):
    title = text.split('(')[0].strip()
    if title.endswith(', The'):
        title = "The " + title[:-6]

    year = text.split('(')[-1].replace(')', '').strip()

    return title.strip(), year.strip()

for row in movies_dataset.itertuples(index=False):
    movie_info = []
    # 信息以title为键，值按顺序依次为year, genres
    movie_info.append(extract_title_year(row[1])[1])
    movie_info.append(row[2]. split('|'))

    dataset[extract_title_year(row[1])[0]] = movie_info

