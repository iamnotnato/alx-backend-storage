#!/usr/bin/env python3
""" list all pymongo
"""


def list_all(mongo_collection):
    """ lists all documents in a collection
    """
    cursor = mongo_collection.find({})
    if not cursor.alive:
     return []
    else:
     return cursor

