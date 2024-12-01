#!/usr/bin/env python3

class Dog:
    def __init__(self, name, breed="Mutt"):
        """
        Initialize a Dog instance with a name and optional breed.
        If no breed is specified, default to "Mutt".
        """
        self.name = name
        self.breed = breed
