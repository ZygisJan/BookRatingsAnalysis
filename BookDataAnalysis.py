import pandas as pd
import matplotlib.pyplot as plt

def clean_and_load_csv(file_path, separator=',', encoding='utf-8'):
    try:
        data = pd.read_csv(file_path, sep=separator, encoding=encoding, on_bad_lines='skip')
        print(f"Failas {file_path} sėkmingai įkeltas. Eilučių skaičius: {len(data)}")
        return data
    except Exception as e:
        print(f"Klaida įkeliant failą {file_path}: {e}")
        return None

books = clean_and_load_csv('books.csv', separator=';')
ratings = clean_and_load_csv('ratings.csv', separator=';')

books.rename(columns=lambda x: x.strip(), inplace=True)
ratings.rename(columns=lambda x: x.strip(), inplace=True)

if 'isbn' in ratings.columns:
    ratings.rename(columns={'isbn': 'ISBN'}, inplace=True)

if 'isbn' in books.columns:
    books.rename(columns={'isbn': 'ISBN'}, inplace=True)

ratings.dropna(subset=['ISBN'], inplace=True)
books.dropna(subset=['ISBN'], inplace=True)

merged_data = pd.merge(ratings, books, on='ISBN', how='inner')
print(f"Sujungtų duomenų eilučių skaičius: {len(merged_data)}")

merged_data = merged_data[(merged_data['Year'] > 1800) & (merged_data['Year'] <= 2025)]
meaningful_ratings = merged_data[merged_data['Rating'] > 0]

book_analysis = meaningful_ratings.groupby('Title').agg(
    total_users=('User-ID', 'count'),
    average_rating=('Rating', 'mean')
).sort_values(by='total_users', ascending=False)

# Lietuviškas rezultato tekstas
print("\nTOP 10 populiariausių knygų pagal vartotojų skaičių:")
for title, row in book_analysis.head(10).iterrows():
    print(f"Knyga: '{title}', Vartotojų skaičius: {row['total_users']}, Vidutinis įvertinimas: {row['average_rating']:.2f}")

plt.figure(figsize=(10, 6))
book_analysis['total_users'].head(10).plot(kind='bar', color='teal', title='TOP 10 populiariausių knygų pagal vartotojų skaičių')
plt.xlabel('Knygos')
plt.ylabel('Vartotojų skaičius')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()

plt.figure(figsize=(10, 6))
book_analysis['average_rating'].head(10).plot(kind='bar', color='orange', title='TOP 10 populiariausių knygų vidutinis įvertinimas')
plt.xlabel('Knygos')
plt.ylabel('Vidutinis įvertinimas')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()



