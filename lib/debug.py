#!/usr/bin/env python3
import ipdb;

from classes.many_to_many import Article
from classes.many_to_many import Author
from classes.many_to_many import Magazine

if __name__ == '__main__':
    print("HELLO! :) let's debug :vibing_potato:")

    # Create some authors
    author1 = Author("RURIGI")
    author2 = Author("MAINA")

    # Create some magazines
    magazine1 = Magazine("FEELING TECHY?", "Technology")
    magazine2 = Magazine("WHAT'S YOUR BODY SAYING?", "Health")

    # Create some articles
    article1 = Article(author1, magazine1, "The Future of AI")
    article2 = Article(author1, magazine2, "Healthy Living Tips")
    article3 = Article(author2, magazine1, "Quantum Computing in today's world")

    # Add articles to authors
    author1.add_article(magazine1, "The Future of AI")
    author1.add_article(magazine2, "Healthy Living Tips")
    author2.add_article(magazine1, "Quantum Computing in today's world")

    # don't remove this line, it's for debugging!
    ipdb.set_trace()
