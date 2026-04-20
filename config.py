from enum import Flag

__all__ = ["language", "restrictions", "FILE_EXTENSION", "FLAG_LIST", "flag_class"]

###########################################
############# Edit this part ##############
###########################################
LANGUAGE_NAME = "insert_here"
LANGUAGE_PAGE = "https://esolangs.org/"
RESTRICTIONS_TIME = 60
RESTRICTIONS_OUTPUT = 128000
FILE_EXTENSION = ".insert_here"
FLAG_LIST = [ # A flags enum is made for you using this list. Import the flag enum like this: `from config import flag_class`.
    "MonkeySee",
    "MonkeyDo",
    "MonkeyTea",
    "MonkeyPeeAllOverYou"
]
###########################################
###########################################
###########################################

flag_class = Flag(f'{LANGUAGE_NAME} FLAG', FLAG_LIST)

language = {
    "name": LANGUAGE_NAME,
    "url": LANGUAGE_PAGE
}

restrictions = {
    "time_limit": RESTRICTIONS_TIME,
    "output_limit": RESTRICTIONS_OUTPUT
}