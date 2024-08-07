from typing import List


class UserProfile:
    def __init__(self, age: int, gender: str, likes: List[str], dislikes: List[str], comment: List[str]):
        self._age = age
        self._gender = gender
        self._likes = likes
        self._dislikes = dislikes
        self._history_comment = comment
