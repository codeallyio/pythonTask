### Word Scraper Counter

A compact customizable web scraper that takes a url and word params, scrapes the URL, and extracts the words in the document. 

Response should contain json with all/matching words count, sorted by the most common. Words that occur in url same number
of times should be sorted alphabetically. Scraper should be case <b>insensitive</b>. Words in response should be in <b>lower</b> case.

Complete the program that will take url as first argument and not specified number of word params.

##### Run your program
Run in main project directory for example:
```
python3.8 main.py http://example.com example Domain
```
it should return something like:
```
{"domain": 4, "example": 3}
```