#!/usr/bin/env python3
import pymongo
""" Listing only related topics"""


def schools_by_topic(mongo_collection, topic):
    """ Listing all topics of in a collection
    @mongo_collection: The collection to search
    @topic: The topic to search for
    Return: Returns a list of all the topics found
    """
    return (mongo_collection.find({"topics": topic}))
