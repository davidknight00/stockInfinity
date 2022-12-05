from pygooglenews import GoogleNews
import json


def main():
    gn = GoogleNews(lang = 'en', country = 'US')
    n = gn.search("AAPL", when="1m")
    i = 0

    print(type(n["entries"]))


if __name__ == "__main__":
    main()

