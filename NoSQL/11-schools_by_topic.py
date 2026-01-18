#!/usr/bin/env python3
"""
Module that returns schools containing a specific topic in MongoDB
"""

def schools_by_topic(mongo_collection, topic):
    """
    Returns a list of schools having a specific topic.
    """
    # The topic must be in the 'topics' array
    return list(mongo_collection.find({"topics": {"$elemMatch": {"$eq": topic}}}))
