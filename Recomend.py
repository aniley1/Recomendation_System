import tkinter as tk

# Sample movie data (movie, genre)
movie_data = {
    "Movie 1": "Action",
    "Movie 2": "Comedy",
    "Movie 3": "Drama",
    "Movie 4": "Horror",
    "Movie 5": "Mystery",
    "Movie 6": "Crime",
}

# Create a GUI window
window = tk.Tk()
window.title("Movie Recommendation System")

# Create labels and entry fields
label = tk.Label(window, text="Enter your favorite movie genre:")
entry = tk.Entry(window)
recommendation_label = tk.Label(window, text="Recommended Movies:")

# Create a text widget to display recommendations
recommendation_text = tk.Text(window, height=5, width=30)
recommendation_text.config(state="disabled")

# Function to get recommendations based on genre
def get_recommendations():
    genre = entry.get()
    recommendations = [movie for movie, movie_genre in movie_data.items() if movie_genre == genre]
    recommendation_text.config(state="normal")
    recommendation_text.delete(1.0, tk.END)
    if recommendations:
        for movie in recommendations:
            recommendation_text.insert(tk.END, movie + "\n")
    else:
        recommendation_text.insert(tk.END, "No recommendations found for this genre.")
    recommendation_text.config(state="disabled")

# Create a button to get recommendations
recommend_button = tk.Button(window, text="Get Recommendations", command=get_recommendations)

# Place widgets on the grid
label.grid(row=0, column=0, padx=10, pady=10)
entry.grid(row=0, column=1, padx=10, pady=10)
recommend_button.grid(row=1, columnspan=2, padx=10, pady=10)
recommendation_label.grid(row=2, columnspan=2, padx=10, pady=10)
recommendation_text.grid(row=3, columnspan=2, padx=10, pady=10)

# Start the GUI main loop
window.mainloop()
