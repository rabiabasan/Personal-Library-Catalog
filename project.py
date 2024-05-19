import tkinter as tk
from tkinter import ttk
import webbrowser

class LibrarySystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Library System")
        self.root.geometry("800x1000")
        self.root.configure(background='white')

        # Create frames
        self.main_frame = tk.Frame(self.root)
        self.main_frame.pack(fill="both", expand=True)

        # Create books frame
        self.books_frame = tk.Frame(self.main_frame, bg="#ee799f")
        self.books_frame.pack(side="left", fill="y")

        self.books_label = tk.Label(self.books_frame, text="Books", font=("Arial", 24, "bold"), bg="#ee799f", fg="white")
        self.books_label.pack(side="top", fill="x")

        self.book_list_frame = tk.Frame(self.books_frame, bg="#ee799f")
        self.book_list_frame.pack(fill="both", expand=True)

        # Create book list
        self.book_list = tk.Listbox(self.book_list_frame, width=28, height=20, bg="#cd6889", fg="white", font=("Arial", 14))
        self.book_list.pack(fill="both", expand=True)
        self.populate_book_list()

        # Create book details frame
        self.book_details_frame = tk.Frame(self.main_frame, bg="#ee799f")
        self.book_details_frame.pack(side="right", fill="both", expand=True)

        # Create search bar
        self.search_frame = tk.Frame(self.book_details_frame, bg="#8b475d", pady=10)
        self.search_frame.pack(fill="x")

        self.search_label = tk.Label(self.search_frame, text="Search for a book:", bg="#8b475d", fg="white")
        self.search_label.pack(side="left", padx=10)

        self.search_entry = tk.Entry(self.search_frame, width=30)
        self.search_entry.pack(side="left", padx=10)

        self.search_button = tk.Button(self.search_frame, text="Search", command=self.search_book, fg="black")
        self.search_button.configure(background='blue')
        self.search_button.pack(side="left", padx=10)

        # Create book details
        self.book_title_label = tk.Label(self.book_details_frame, text="", font=("Arial", 34), bg="#ee799f", fg="black")
        self.book_title_label.pack(pady=20)

        self.book_image_label = tk.Label(self.book_details_frame, bg="#ee799f")
        self.book_image_label.pack(pady=10, padx=10)

        # Create rating and comment widgets
        self.rating_label = tk.Label(self.book_details_frame, text="Rating:", bg="#ee799f", fg="white")
        self.rating_label.pack(pady=10, padx=20, anchor="w")

        self.rating_scale = ttk.Scale(self.book_details_frame, from_=0, to=5, length=200, orient="horizontal")
        self.rating_scale.pack(pady=5, padx=20, anchor="w")

        self.comment_label = tk.Label(self.book_details_frame, text="Comment:", bg="#ee799f", fg="white")
        self.comment_label.pack(pady=10, padx=20, anchor="w")

        self.comment_entry = tk.Entry(self.book_details_frame, width=40)
        self.comment_entry.pack(pady=5, padx=20, anchor="w", fill="x")

        self.submit_button = tk.Button(self.book_details_frame, text="Submit", command=self.submit_review, bg="blue", fg="BLACK")
        self.submit_button.pack(pady=10, padx=20, anchor="e")

        # Create link button
        self.link_button = tk.Button(self.book_details_frame, text="GO TO BOOK", command=lambda: self.open_link("file:///Users/azracebe/Downloads/01%20Harry%20Potter%20and%20The%20Philosopher's%20Stone.pdf"))
        self.link_button.pack(pady=10)

    def populate_book_list(self):
        # Add some sample books with image paths
        self.books = [
            {"title": "  -Harry Potter Sorcerer's Stone", "image_path": "hp1.png"},
            {"title": "  -Harry Potter Chamber of Secrets", "image_path": "hp2.png"},
            {"title": "  -Harry Potter Prisoner of Azkaban", "image_path": "hp3.png"},
            {"title": "  -Harry Potter Goblet of Fire", "image_path": "hp4.png"},
            {"title": "  -Harry Potter Order Of the Phoenix", "image_path": "hp5.png"},
            {"title": "  -Harry Potter Half-Blood Prince", "image_path": "hp6.png"},
            {"title": "  -Harry Potter and the Deathly Hallows", "image_path": "hp7.png"}
        ]

        for book in self.books:
            self.book_list.insert(tk.END, book["title"])

        # Bind listbox select event
        self.book_list.bind("<<ListboxSelect>>", self.show_book_details)

    def search_book(self):
        search_term = self.search_entry.get().lower()

        # Clear previous search results
        self.book_list.delete(0, tk.END)

        # Filter books based on search term
        for book in self.books:
            if search_term in book["title"].lower():
                self.book_list.insert(tk.END, book["title"])

    def show_book_details(self, event):
        selected_index = self.book_list.curselection()[0]
        selected_book = self.books[selected_index]

        self.book_title_label.config(text=selected_book["title"].strip())

        # Load and display book image
        image_path = selected_book.get("image_path")
        if image_path:
            image = tk.PhotoImage(file=image_path)
            image = image.subsample(2)
            self.book_image_label.config(image=image)
            self.book_image_label.image = image  # Keep a reference to avoid garbage collection

    def submit_review(self):
        rating = self.rating_scale.get()
        comment = self.comment_entry.get()

        # Process the rating and comment (for demonstration, print them)
        print(f"Rating: {rating}")
        print(f"Comment: {comment}")

        # Optionally, you can save the rating and comment to a database or file

    def open_link(self, url):
        webbrowser.open(url)

# Create the main window
root = tk.Tk()
app = LibrarySystem(root)
root.mainloop()
