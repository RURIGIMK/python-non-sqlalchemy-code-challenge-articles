class Author:
    def __init__(self, name):
        self._name = name
        self._articles = []

    @property
    def name(self):
        return self._name

    @property
    def articles(self):
        return self._articles

    def add_article(self, magazine, title):
        article = Article(self, magazine, title)
        self._articles.append(article)
        magazine.add_article(article)
        return article

    @property
    def magazines(self):
        return list(set(article.magazine for article in self.articles))

    def topic_areas(self):
        return list(set(article.magazine.category for article in self.articles))

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

    @property
    def articles(self):
        return self._articles

    def add_article(self, article):
        self._articles.append(article)

    def article_titles(self):
        if not self.articles:
            return None
        return [article.title for article in self.articles]

    def contributing_authors(self):
        author_counts = {}
        for article in self.articles:
            author = article.author
            if author in author_counts:
                author_counts[author] += 1
            else:
                author_counts[author] = 1
        return [author for author, count in author_counts.items() if count > 2]

class Article:
    def __init__(self, author, magazine, title):
        self._author = author
        self._magazine = magazine
        self._title = title

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, new_author):
        self._author = new_author

    @property
    def magazine(self):
        return self._magazine

    @magazine.setter
    def magazine(self, new_magazine):
        self._magazine = new_magazine

    @property
    def title(self):
        return self._title

    @property
    def magazine(self):
        return self._magazine

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

    @property
    def articles(self):
        return self._articles

    def add_article(self, magazine, title):
        article = Article(self, magazine, title)
        self._articles.append(article)
        magazine.add_article(article)
        return article

    @property
    def magazines(self):
        return list(set(article.magazine for article in self.articles))

    def topic_areas(self):
        return list(set(article.magazine.category for article in self.articles))

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

    @property
    def articles(self):
        return self._articles

    def add_article(self, article):
        self._articles.append(article)

    def article_titles(self):
        if not self.articles:
            return None
        return [article.title for article in self.articles]

    def contributing_authors(self):
        author_counts = {}
        for article in self.articles:
            author = article.author
            if author in author_counts:
                author_counts[author] += 1
            else:
                author_counts[author] = 1
        return [author for author, count in author_counts.items() if count > 2]

class Article:
    def __init__(self, author, magazine, title):
        self._author = author
        self._magazine = magazine
        self._title = title

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, new_author):
        self._author = new_author

    @property
    def magazine(self):
        return self._magazine

    @magazine.setter
    def magazine(self, new_magazine):
        self._magazine = new_magazine

    @property
    def title(self):
        return self._title

    @property
    def magazine(self):
        return self._magazine

    @title.setter
    def title(self, new_title):
        raise AttributeError("Title attribute is immutable.")
