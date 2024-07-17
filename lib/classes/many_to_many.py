class Article:
    def __init__(self, author, magazine, title):
        self._title = title
        self._author = author
        self._magazine = magazine

        if not (5 <= len(self._title) <= 50):
            raise ValueError("Title must be a string between 5 and 50 characters.")

        if not isinstance(self._author, Author):
            raise TypeError("Author must be an instance of Author class.")

        if not isinstance(self._magazine, Magazine):
            raise TypeError("Magazine must be an instance of Magazine class.")

        self._author.add_article(self)
        self._magazine.add_article(self)

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, new_title):
        raise AttributeError("Title attribute is immutable.")

    @property
    def author(self):
        return self._author

    @property
    def magazine(self):
        return self._magazine


class Author:
    def __init__(self, name):
        self._name = name
        self._articles = []

        if not isinstance(self._name, str) or len(self._name) == 0:
            raise ValueError("Name must be a non-empty string.")

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        raise AttributeError("Name attribute is immutable.")

    def add_article(self, article):
        if not isinstance(article, Article):
            raise TypeError("Article must be an instance of Article class.")
        self._articles.append(article)

    def articles(self):
        return self._articles

    def magazines(self):
        return list(set(article.magazine for article in self._articles))

    def topic_areas(self):
        return list(set(article.magazine.category for article in self._articles))


class Magazine:
    def __init__(self, name, category):
        self._name = name
        self._category = category
        self._articles = []

        if not isinstance(self._name, str) or not (2 <= len(self._name) <= 16):
            raise ValueError("Name must be a string between 2 and 16 characters.")

        if not isinstance(self._category, str) or len(self._category) == 0:
            raise ValueError("Category must be a non-empty string.")

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
        if not isinstance(article, Article):
            raise TypeError("Article must be an instance of Article class.")
        self._articles.append(article)

    def articles(self):
        return self._articles

    def contributors(self):
        return list(set(article.author for article in self._articles))

    def article_titles(self):
        return [article.title for article in self._articles]
