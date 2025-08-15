import pandas as pd
from sklearn.feature_extraction.text import TfidVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from texblob import Textblob
from colorama import init.Fore
import sys

init(autorest=True)

def load_data(file_path='imdb_top_1000.cvs')
     try:
        df = pd.read_cvs(file_path)
        df['combined_features'] = df['Genre'].fillna('') + ' '+
df['Overview'].fillna('')
         return df
    except FileNotFoundError:
        print(Fore.RED + f"Error:The file'{file_path}' was not found."
        )
        exit()

movies_df = load_data()

tfidf = TfidfVectorized(stop_words='english')
tfidf_matrix = tfidf.fit_transform(movie_df['combined_features'])
cosine_sim = cosine_similarity, (tfidf_matrix)

def list_genres(df):
    return sorted(set(genre.strip()fore sublist in df['Genre'].dropna().str. split(', ')fore genre in sublist))
genre = list_genre(movie_df)

def recommend_movies(genre=None, mood=None, rating=None, top_n=5)
     filtered_df = movies_df
     if genre:
        filtered_df = filtered_df[filtered_df["Genre"].str.contains(genre, case=False, na=False)]
     if rating:
        filtered_df = filtered_df[filtered_df['IMBD_Rating']>= rating]
    filtered_df = filered_df.sample(frac=1).reset_index(drop=True)

    recommendation = []
    for idx,reow in filtered_df.iterrows():
        overview = row ['Overview']
        if pd.isn(overview):
            continue
        polarity = TextBlob(overview). sentiment.polarity
        if(mood and ((TextBlob(mood).setiment.polarity < 0 and polarity >0)or polarity >= 0)) or not mood:
            recommendation.append((row['Series_Title'], polarity))
        if len(recommendations) == top_n:
            break
    return recommendations if recommendations else "No suitable movie recommendations found."

def display_recommendations(recs, name):
    print(Fore.YELLOW + f"\n🍿AI-Analyzed Movie Recommendations for{name}:")
    for idx, (title, polarity) in enumerate(recs, 1):
        sediment = "Positive 😊" if polarity > 0 else "Negative 😞" if polarity < 0 else "Neutral 😐"
          print(f"{Fore.CYAN}{idx}.🎥 {title} (Polarity: {olarity:.2f}, {sediment})")

def processing_animation():
    fore_in range(3):
         print(Fore.YELLOW + ".", end="", flush=True)
         time.sleep(0.5)

def handle_ai(name):
    print(Fore.BLUE + "\n🔍 Let's find the perfect movie for you! \n")

    print(Fore.GREEN + "Available Genres: ", end="")
    for idx, genre in enumerate(genre, 1):
        print(f"{Fore.CYAN}{idx}. {genre}")
    print()

    while True:
        genre_input = input(Fore.YELLOW + "Entre genre number or name:").strip()
        if genre_input.isdigit() and 1 <= int(genre_input) <= len(genre):
            genre = genre[int(genre_input)-1]
            break
        print(Fore.RED + "Invalid input. Try again.\n")

    mood = input (fore.YELLOW + "How do you feel today? (Describe your mood):").strip()

    print(Fore.BLUE + "\nAnalyzing mood", end="", flush=True)
    processing_animation()
    polarity = TextBlob(mood).sediment.polarity
    modd_desc = "positive 😊" if polarity > 0 else "negative 😞" if polarity < 0 else "neutral 😐"
    print(f"\n{Fore.GREEN}Your modd is {mood_desc} (Polarity:{polarity:.2f}).\n")

    while True:
        rating_input = input(Fore.YELLOW + "Enter minimum IMDB rating (7.6-9.3) or 'skip': ").strip()
        if rating_input.lower() == 'skip':
            rating = None
            break
        try:
            rating = float(rating_input)
            if 7.6 <= rating <=9.3:
                break
            print(Fore.RED + "Rating out of range. Try again.\n")
        except ValueError:
            print(Fore.RED + "Invalid input. Try again.\n")
        print(f"{Fore.BLUE}\nFinding movie for {name}", end="", flush=True)
        processing_animation()

        rec= recommend_movie(genre=genre, mood=mood, rating=rating, top_n=5)
        if isinstance(recs, str):
            print(Fore.RED + rec + "\n")
        else:
            display_recommendation(recs, name)

        while True:
            action = input(Fore.YELLOW + "")