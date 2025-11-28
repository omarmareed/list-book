import string
from collections import Counter


class BookAnalyzer:
    def __init__(self):
        self.authors_books = {}

    def add_books(self, new_dict):
        """
        Add books to the authors' dictionary.
        """
        for author, books in new_dict.items():
            if author in self.authors_books:
                self.authors_books[author].extend(books)
            else:
                self.authors_books[author] = books

    def get_authors_books(self):
        """
        Retrieve the dictionary of authors and their books.
        """
        return self.authors_books

    def analyze_book(self, book_text):
        """
        Analyze a single book's content for statistics.
        """
        # Remove punctuation
        book_text = book_text.translate(str.maketrans('', '', string.punctuation))

        # Split into words and sentences
        words = book_text.split()
        sentences = [s.strip() for s in book_text.split('.') if s.strip()]

        # Calculate metrics
        word_lengths = [len(word) for word in words]
        sentence_lengths = [len(sentence.split()) for sentence in sentences]

        return {
            "average_word_length": sum(word_lengths) / len(words) if words else 0,
            "average_sentence_length": sum(sentence_lengths) / len(sentence_lengths) if sentence_lengths else 0,
            "word_count": len(words),
            "character_count": len(book_text),
        }

    def analyze_authors_books(self):
        """
        Analyze all books for each author in the collection.
        """
        analysis_results = {}
        for author, books in self.authors_books.items():
            books_analysis = []
            for book in books:
                analysis = self.analyze_book(book)
                analysis['book'] = book  # Add book title for context
                books_analysis.append(analysis)
            analysis_results[author] = books_analysis
        return analysis_results

    def most_frequent_word(self, linking_words=None):
        """
        Identify the most frequent word in all books, excluding linking words.
        """
        if linking_words is None:
            linking_words = []

        linking_words_set = set(linking_words)
        word_frequencies = Counter()

        for books in self.authors_books.values():
            for book in books:
                words = book.split()
                for word in words:
                    word = word.lower().strip(".,!?\"'")
                    if word not in linking_words_set:
                        word_frequencies[word] += 1

        if not word_frequencies:
            return None, 0

        most_frequent, max_frequency = word_frequencies.most_common(1)[0]
        return most_frequent, max_frequency


# Example usage:
authors_books = {
    'Ray Bradbury': ['Fahrenheit 451', 'The Martian Chronicles'],
    'George R.R. Martin': ['A Game of Thrones', 'A Clash of Kings'],
    'Stephen King': ['The Shining', 'It', 'Carrie']
}

# Create an instance of BookAnalyzer
analyzer = BookAnalyzer()

# Add books to the analyzer
analyzer.add_books(authors_books)

# Get all authors and books
print("Authors and Books:")
print(analyzer.get_authors_books())

# Analyze all authors' books
print("\nAnalysis Results:")
analysis_results = analyzer.analyze_authors_books()
for author, books_info in analysis_results.items():
    print(f"{author}:")
    for book_info in books_info:
        print(f"  - Book: {book_info['book']}, Word Count: {book_info['word_count']}")

# Find the most frequent word, excluding common linking words
linking_words = ["the", "and", "of", "to", "in", "a", "it"]
most_frequent_word, frequency = analyzer.most_frequent_word(linking_words)
print(f"\nThe most frequent word (excluding linking words) is '{most_frequent_word}' with a frequency of {frequency}.")












