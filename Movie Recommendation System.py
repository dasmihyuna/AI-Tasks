pip install pandas scikit-learn

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

data = {
    "title": [
        "The Matrix", "John Wick", "Inception", "Interstellar",
        "The Dark Knight", "The Prestige", "Tenet",
        "Avengers: Endgame", "Iron Man", "Doctor Strange",
        "The Grand Budapest Hotel", "Pride and Prejudice", "Atonement",
        "Mean Girls", "Grown Ups", "Barbie", "IT", "Little Women",
        "Harry Potter", "La La Land", "Moana", "Despicable Me",
        "Everything Everywhere All At Once", "Before Sunrise",
        "Minecraft", "Tangled", "Aladdin", "Primal Fear", "Gone Girl",
        "Fight Club", "When Harry Met Sally", "The Truman Show",
        "Parasite", "Shrek", "Spiderman", "How to Train Your Dragon",
        "Lady Bird", "The Princess Diaries"
    ],
    "features": [
        "sci-fi hacker virtual reality Keanu Reeves",
        "action revenge assassin Keanu Reeves",
        "dream thriller sci-fi Nolan DiCaprio",
        "space time travel sci-fi Nolan McConaughey",
        "dark superhero action Nolan Batman",
        "magic illusion mystery Nolan Bale",
        "inverted time spy thriller Nolan",
        "superhero team marvel time travel infinity",
        "tech genius superhero marvel Tony Stark",
        "magic marvel multiverse doctor cape",
        "comedy quirky Wes Anderson hotel mystery",
        "romance period drama Jane Austen England",
        "romantic war drama Keira Knightley guilt",
        "high school comedy girls rivalry Lindsay Lohan",
        "comedy family Adam Sandler summer vacation",
        "fantasy satire feminism pink Ryan Gosling",
        "horror clown children Stephen King small town",
        "period drama family sisters Greta Gerwig",
        "fantasy magic school wizards Rowling",
        "musical romance jazz Emma Stone Ryan Gosling",
        "animation musical ocean princess Disney",
        "animation comedy villain minions heist",
        "sci-fi multiverse absurd action Michelle Yeoh",
        "romantic drama Vienna strangers conversation",
        "game sandbox survival pixel crafting",
        "animation fantasy princess long hair Disney",
        "animation fantasy genie princess adventure",
        "legal thriller courtroom Edward Norton",
        "thriller mystery missing wife Rosamund Pike",
        "psychological drama twist Brad Pitt",
        "romantic comedy friendship Meg Ryan",
        "sci-fi drama reality illusion Jim Carrey",
        "thriller social class Korean dark comedy",
        "animation fantasy comedy talking donkey",
        "superhero marvel spider bite city",
        "animation dragon fantasy viking friendship",
        "coming of age drama Greta Gerwig",
        "teen comedy princess royalty Anne Hathaway"
    ]
}

# Load into DataFrame
df = pd.DataFrame(data)

# Vectorize the features column
vectorizer = TfidfVectorizer()
feature_matrix = vectorizer.fit_transform(df['features'])

# Compute cosine similarity between movies
cosine_sim = cosine_similarity(feature_matrix)

# Recommendation function
def recommend(movie_title, top_n=5):
    if movie_title not in df['title'].values:
        print(f"Sorry, '{movie_title}' not found.")
        return

    idx = df[df['title'] == movie_title].index[0]
    similarity_scores = list(enumerate(cosine_sim[idx]))
    similarity_scores = sorted(similarity_scores, key=lambda x: x[1], reverse=True)

    # Skip the first one (it's the movie itself)
    recommended = [df['title'][i] for i, score in similarity_scores[1:top_n+1]]

    print(f"\nBecause you liked '{movie_title}', you might also like:")
    for movie in recommended:
        print(f"• {movie}")

# Run
if __name__ == "__main__":
    print("=== Movie Recommender ===")
    user_input = input("Enter a movie title: ").strip()
    recommend(user_input)
