# Book Data Analysis Project

## Aprašymas
Šis projektas atlieka knygų populiarumo analizę, naudojant duomenis iš `books.csv` ir `ratings.csv` failų. 
Analizės tikslas - nustatyti populiariausias knygas, pagal vartotojų skaičių ir jų vidutinius įvertinimus.

## Funkcionalumas
- Įkelia ir sujungia duomenis iš dviejų CSV failų (`books.csv` ir `ratings.csv`).
- Nustato TOP 10 populiariausių knygų pagal vartotojų skaičių.
- Apskaičiuoja šių knygų vidutinius įvertinimus.
- Sugeneruoja diagramas:
- Populiariausių knygų pagal vartotojų skaičių.
- Vidutinių populiariausių knygų įvertinimų.

## Reikalavimai
Projektas reikalauja šių bibliotekų:
- Python
- pandas
- matplotlib

Pilną priklausomybių sąrašą rasite `requirements.txt` faile.

## Naudojimo instrukcija
1. Įsitikinkite, kad turite `books.csv` ir `ratings.csv` failus toje pačioje direktorijoje kaip šis projektas.
2. Įdiekite priklausomybes:
   ```bash
   pip install -r requirements.txt
