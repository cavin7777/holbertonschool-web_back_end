#!/usr/bin/env python3
"""
Module that updates the 'topics' field of a school document in a MongoDB collection
"""

def update_topics(mongo_collection, name, topics):
    """
    Updates all topics of a school document based on its name.
    """
    return mongo_collection.update_many(
        { "name": name },
        { "$set": { "topics": topics } }
    )
