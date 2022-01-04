# Web-Scarping-For-Security-Operations

The webScraping .py script sending http requests to a specified url and extracts the following information from the web-page using BeautifulSoup4 and stores it in a word document using the docx module:
- page-title
- page-links URLs
- images found on the page

The webScraping2.py script is a more sophisticated version of the webscraping.py mentioned above, as it includes class objects and methods which performs the following tasks:
- sends http request to a specified url
- extracts all unique images and the image urls
- utilizes regex to find phone numbers, emails and zip codes
- extracts all text on the webpage
- leverages the NTLK libaray to tokenize the text and find: most occuring word, all nouns, and all verbs in the text
