#!/usr/bin/env python3
""" a Python function that lists all documents in a collection:
"""

def list_all(mongo_collection):
    """ a Python function that lists all documents in a collection:
    """
    result = mongo_collection.find({})
    return result
