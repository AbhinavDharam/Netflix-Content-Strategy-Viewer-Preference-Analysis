import pandas as pd

df = pd.read_csv("Netflix_Data.csv")

print(df.head())

print(df.info())

print("shape:", df.shape)

print("\nMissing Values:")
print(df.isnull().sum())

print("\nDuplicates:")
print(df.duplicated().sum())

df.drop_duplicates(inplace=True)

df['director'] = df['director'].fillna('Unknown')

df['cast'] = df['cast'].fillna('Not Available')

df['country'] = df['country'].fillna('Unknown')

df['rating'] = df['rating'].fillna(df['rating'].mode()[0])

df['date_added'] = pd.to_datetime(
    df['date_added'].astype(str).str.strip(),
    format='%B %d, %Y',
    errors='coerce'
)

df = df.dropna(subset=['date_added'])

df['year_added'] = df['date_added'].dt.year
df['month_added'] = df['date_added'].dt.month
invalid_dates = df[df['date_added'].isna()]

print(invalid_dates[['title', 'date_added']].head(20))

print("\nMissing Values After Cleaning:")
print(df.isnull().sum())

df.to_csv("cleaned_netflix_data.csv", index=False)

print("Dataset cleaned successfully!")