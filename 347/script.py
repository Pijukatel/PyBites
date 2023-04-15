from enum import Enum


class Hand(str, Enum):
    RIGHT = "right"
    LEFT = "left"
    BOTH = "both"


LEFT_HAND_CHARS = set("QWERTASDFGZXCVB")
RIGHT_HAND_CHARS = set("YUIOPHJKLNM")
BOTH_HAND_CHARS = LEFT_HAND_CHARS | RIGHT_HAND_CHARS


def get_hand_for_word(word: str) -> Hand:
    """
    Use the LEFT_HAND_CHARS and RIGHT_HAND_CHARS sets to determine
    if the passed in word can be written with only the left or right
    hand, or if both hands are needed.
    """
    letters_in_word = set(word.upper())

    if letters_in_word.issubset(LEFT_HAND_CHARS):
        return Hand.LEFT
    if letters_in_word.issubset(RIGHT_HAND_CHARS):
        return Hand.RIGHT
    if letters_in_word.issubset(BOTH_HAND_CHARS):
        return Hand.BOTH
    raise ValueError(f"Word contains unexpected characters: {letters_in_word - BOTH_HAND_CHARS}")
