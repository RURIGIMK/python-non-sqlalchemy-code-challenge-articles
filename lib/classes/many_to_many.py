# many_to_many.py

class Article:
    def __init__(self, author, magazine, title):
        self._title = title
        self.author = author
        self.magazine = magazine
        self.magazine.add_article(self)
        self.author.add_article(self)

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, new_title):
        raise AttributeError("Title attribute is immutable.")

class Author:
    def __init__(self, name):
        self._name = name
        self._articles = []

    @property
    def name(self):
        return self._name

    def add_article(self, article):
        self._articles.append(article)

    def articles(self):
        return self._articles

class Magazine:
    def __init__(self, name, category):
        self._name = name
        self._category = category
        self._articles = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        if not isinstance(new_name, str) or not (2 <= len(new_name) <= 16):
            raise ValueError("Name must be a string between 2 and 16 characters.")
        self._name = new_name

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, new_category):
        if not isinstance(new_category, str) or len(new_category) == 0:
            raise ValueError("Category must be a non-empty string.")
        self._category = new_category

    def add_article(self, article):
        self._articles.append(article)

    def articles(self):
        return self._articles

    def contributors(self):
        contributors = set()
        for article in self._articles:
            contributors.add(article.author)
        return list(contributors)

    def article_titles(self):
        return [article.title for article in self._articles]

    def contributing_authors(self):
        authors_dict = {}
        for article in self._articles:
            if article.author in authors_dict:
                authors_dict[article.author] += 1
            else:
                authors_dict[article.author] = 1
        return [author for author, count in authors_dict.items() if count > 2]

    def __str__(self):
        return f"{self._name} ({self._category})"
