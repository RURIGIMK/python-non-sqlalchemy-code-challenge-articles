class Article:
    def __init__(self, author, magazine, title):
        self._title = title
        self.author = author
        self.magazine = magazine
        self.author.add_article(self)

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, new_title):
        raise AttributeError("Title attribute is immutable.")

    def __repr__(self):
        return f"Article({self._title})"


class Author:
    def __init__(self, name):
        self.name = name
        self._articles = []
        self._magazines = set()

    @property
    def articles(self):
        return self._articles

    @property
    def magazines(self):
        return list(self._magazines)

    def add_article(self, magazine, title):
        article = Article(self, magazine, title)
        self._articles.append(article)
        return article

    def magazines(self):
        return list(self._magazines)

    def articles(self):
        return list(self._articles)


class Magazine:
    def __init__(self, name, category):
        self.name = name
        self.category = category
        self._articles = []
        self._contributors = set()

    @property
    def articles(self):
        return list(self._articles)

    @property
    def contributors(self):
        return list(self._contributors)

    def add_article(self, author, title):
        article = Article(author, self, title)
        self._articles.append(article)
        author._articles.append(article)
        self._contributors.add(author)
        return article

    def article_titles(self):
        return [article.title for article in self._articles]

    def contributing_authors(self):
        return [author for author in self._contributors if len(author.articles) > 2]
