#!/usr/bin/env python3
""" Inserts new document in a collection based on kwargs arguments """


def insert_school(mongo_collection, **kwargs):
    """ Inserts documents into mongo_collection
    @mongo_collection: the collection to be inserted into
    @kwargs: kwargs arguments list
    Return: Returns the new _id
    """
    new_insert = mongo_collection.insert_one(kwargs)
    return (new_insert.inserted_id)
