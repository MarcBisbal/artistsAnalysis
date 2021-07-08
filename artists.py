import pandas as pd
import seaborn as sns

df = pd.read_csv("https://drive.google.com/uc?export=download&id=1pFg9a1Ce_q-Am3SlLOSpXPmR8c5nGHWX")

df.boxplot(column="paintings", fontsize=19)

df.sort_values(by=['paintings'], ascending=False).head(3)

nationality = df.nationality
nationality_freq = nationality.value_counts()
nationality_freq.plot.pie(figsize=(10, 10))
df_nation = df.nationality.str.split(",", expand=True)
df_nation.head()

all_nations = pd.concat([df_nation[0], df_nation[1], df_nation[2]], axis = 0)
all_nations = all_nations.dropna()
all_nations = all_nations.value_counts()
all_nations.plot.pie(figsize=(10, 10))
genre = df.genre
genre_freq = genre.value_counts()
genre_freq.plot.pie(figsize=(10, 10))
df_genre = df.genre.str.split(",", expand=True)
df_genre.head()
all_genre = pd.concat([df_genre[0], df_genre[1], df_genre[2]], axis = 0)
all_genre = all_genre.dropna()
all_genre = all_genre.value_counts()
all_genre.plot.pie(figsize=(10, 10))
