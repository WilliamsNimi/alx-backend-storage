!#/usr/bin/env python3
import pymongo
"""Changing topics"""


def update_topics(mongo_collection, name, topics):
    """ Changing topics in a collection
    @mongo_collection: The collection to work with
    @name: The filter for the collection
    @topics: the topic we want to add
    Return: Returns nothing
    """
    new_topics = {"$set": {"topics": topics}}
    filter_ = {"name": name}
    mongo_collection.update_many(filter_, new_topics)
