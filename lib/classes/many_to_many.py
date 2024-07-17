class Author:
    def __init__(self, name):
        self.name = name
        self._articles = []
    
    def __repr__(self):
        return f"<Author: {self.name}>"

    def articles(self):
        return self._articles

    def magazines(self):
        return list(set(article.magazine for article in self._articles))

    def add_article(self, magazine, title):
        article = Article(self, magazine, title)
        self._articles.append(article)
        magazine._articles.append(article)  # Directly accessing the _articles list
        return article

    def topic_areas(self):
        if not self._articles:
            return []
        return list(set(article.magazine.category for article in self._articles))


class Magazine:
    _all_magazines = []

    def __init__(self, name, category):
        self._name = None  # Initial value to allow the setter validation
        self._category = None  # Initial value to allow the setter validation
        self.name = name
        self.category = category
        self._articles = []
        Magazine._all_magazines.append(self)
    
    def __repr__(self):
        return f"<Magazine: {self.name}, Category: {self.category}>"

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str) and 2 <= len(value) <= 16:
            self._name = value
        else:
            raise ValueError("Name must be a string between 2 and 16 characters")

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        if isinstance(value, str) and len(value) > 0:
            self._category = value
        else:
            raise ValueError("Category must be a non-empty string")
    
    def articles(self):
        return self._articles

    def contributors(self):
        return list(set(article.author for article in self._articles))

    def article_titles(self):
        return [article.title for article in self._articles]

    def contributing_authors(self):
        author_article_count = {}
        for article in self._articles:
            if article.author not in author_article_count:
                author_article_count[article.author] = 0
            author_article_count[article.author] += 1
        return [author for author, count in author_article_count.items() if count > 2]

    @classmethod
    def top_publisher(cls):
        if not cls._all_magazines:
            return None
        return max(cls._all_magazines, key=lambda magazine: len(magazine.articles()))


class Article:
    def __init__(self, author, magazine, title):
        if not isinstance(author, Author):
            raise ValueError("Author must be an instance of Author")
        if not isinstance(magazine, Magazine):
            raise ValueError("Magazine must be an instance of Magazine")
        if not isinstance(title, str) or not (5 <= len(title) <= 50):
            raise ValueError("Title must be a string between 5 and 50 characters")
        
        self._author = author
        self._magazine = magazine
        self._title = title
    
    def __repr__(self):
        return f"<Article: {self._title}, Author: {self._author.name}, Magazine: {self._magazine.name}>"

    @property
    def title(self):
        return self._title
    
    @property
    def author(self):
        return self._author
    
    @property
    def magazine(self):
        return self._magazine
