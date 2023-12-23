"""
This file contains the scrapper exceptions
"""

class IndeedException(Exception):
    def __init__(self):
        super().__init__("Uh oh, an error occurred with Indeed")


class ZipRecruiterException(Exception):
    def __init__(self):
        super().__init__("Uh oh, an error occurred with ZipRecruiter")
