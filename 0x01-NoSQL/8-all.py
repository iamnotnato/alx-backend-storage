#!/usr/bin/env python3
""" list all pymongo
"""


def list_all(mongo_collection):
    """ lists all documents in a collection
    """
    result = mongo_collection.find({})
    return result
