import pyshorteners
import os


def clear_console():
    os.system('cls')

def shortenLink(link):
    short = pyshorteners.Shortener()
    return short.tinyurl.short(link)