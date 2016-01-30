import sys
import os
import bs4
__author__ = "John Smith"

CURRENT_DIRECTORY = os.getcwd() if os.getcwd().endswith("/") else (os.getcwd() + "/")
print CURRENT_DIRECTORY


def main():
    index = open("index.html", "r+")
    soup = bs4.BeautifulSoup(index, "html.parser")
    tag = soup.find("terster")
    print tag.text
    print soup
    index.close()
    return 0

if __name__ == '__main__':
    sys.exit(main())