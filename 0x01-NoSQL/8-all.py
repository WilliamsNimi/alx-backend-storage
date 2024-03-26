#!/usr/bin/env python3
""" Listing all docs in a collection via python"""


def list_all(mongo_collection):
    """ This function lists all documents in a mongo collection
    @mongo_collection: The collection to list all documents
    Return: Returns empty list of list of documents in a collection
    """
    if mongo_collection.count_documents({}) == 0:
        return ([])

    return (mongo_collection.find())
    
