# Script Purpose: Process a target website and extract key information using NLTK module
# Script Version: 1.0 
# Script Author:  Tala Vahedi

# Script Revision History:
# Version 1.0 Dec 6, 2021, Python 3.x

# 3rd Party Modules
from bs4 import BeautifulSoup
from nltk.tag import pos_tag 
from prettytable import PrettyTable  
from collections import Counter # counter to tally up words

# Python Standard Library
import requests
import time
import re
import nltk
from requests.api import post    

# Psuedo Constants
SCRIPT_NAME    = "Script: Process a target website and extract key information using NLTK module"
SCRIPT_VERSION = "Version 1.0"
SCRIPT_AUTHOR  = "Author: Tala Vahedi"


class getRequests:
    ''' Get request link class'''
    
    # function to print corpus length
    def getLinks(self):
        url = 'https://casl.website'

        print("Sending request to ", str(url), " please wait...")
        time.sleep(1)
        # sending get request to the url
        page = requests.get(url)   
        
        # parsing through the text with bs4    
        soup = BeautifulSoup(page.text, 'html.parser')
        print("Parsing ", str(url), " with bs4, please wait...")
        time.sleep(1)

        print("Extracting href/urls from ", str(url), ", please wait...")
        # creating a set to hold unique href/links to pages on the website
        self.links = set()

        time.sleep(1)
        # iterating through all href/links and adding to set 
        for link in soup.findAll('a'):
            if link.get('href') != None:
                try:
                    # make full url if not already
                    if 'http' not in link.get('href'):
                        l = link.get('href')
                        fullLink = url+l
                        if 'casl.website' in fullLink:
                            self.links.add(fullLink)
                    else:
                        fullLink = link.get('href')
                        if 'casl.website' in fullLink:
                            self.links.add(fullLink)
                # catch an error
                except Exception as err:
                    print(err)
                    continue  
        
        # printing out all unique links
        print("\nThe following unique URLs webpages were found on https://casl.website: ")
        for l in self.links:
            time.sleep(.5)
            print(l) 
        print("\n\n")

    # function that grabs image urls, numbers, emails and zipcodes
    def getINFO(self):
        self.imgs = set()
        self.phones = []
        self.email = []
        self.zips = []
        
        for link in self.links:
            web = requests.get(link) 
            soup = BeautifulSoup(web.text, 'html.parser')
            images = soup.findAll('img') 
            webPage = requests.get(link)
            # self object variable to get all textual content
            self.allText = ''
            text = " ".join(soup.get_text().replace("\n", " ").replace("\r", " ").replace("\t"," ").strip().split())
            self.allText = self.allText + text
            
            # regex to find phone numbers 
            phoneRegEx = re.compile(r'[\+\(]?[1-9][0-9 .\-\(\)]{8,}[0-9]')
            numbers = phoneRegEx.findall(webPage.text)
            
            # regex to find emails 
            emailRegEx = re.compile(r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4}')  
            emails = emailRegEx.findall(webPage.text)
          
            # regex to find zipcodes
            zipRegEx = re.compile(r'\b\d{5}-\d{4}\b|\b\d{5}\b\s')
            zipCodes = zipRegEx.findall(webPage.text.strip())
        
            # Process each image tag
            for eachImage in images:      
                # get source of each image
                imgURL = eachImage['src']
                
                # if URL path is relative
                if imgURL[0:4] != 'http':       
                    # try prepending the url url
                    imgURL = (link+imgURL).strip() 
                    self.imgs.add(imgURL)
        
            # iterating through all numbers and printing them out
            for num in numbers:
                self.phones.append(num)
            
            # iterating through all emails and printing them out
            for mail in emails:
                self.email.append(mail)
            
            # iterating through all zipcodes and printing them out
            for zip in zipCodes:
                self.zips.append(zip)
        
    # function that prints out all image urls found
    def printImages(self):     
        print("Parsing through all image tags found on the website, please wait...")
        time.sleep(1)
        print("Processing each image found, please wait...\n")
        time.sleep(1)
        print("\nThe following unique image URLs were found on all webpages of https://casl.website: ")
        time.sleep(1)
        # iterating through the images and printing out unique image urls
        for i in self.imgs:
            time.sleep(.5)
            print(i)    
        print("\n\n")

    # function that prints out phone numbers
    def printNums(self):       
        print("Parsing through all webpages found on the website, please wait...")
        time.sleep(1)
        print("Processing each webpage for phone numbers, please wait...\n")
        time.sleep(1)
        print("\nThe following phone numbers were found on all webpages of https://casl.website: ")
        time.sleep(1)
        # iterating through the phone numbers and printing them out
        for num in self.phones:
            time.sleep(1)
            print(num)
        print("\n")

    # function that prints out emails
    def printEmails(self):       
        print("Parsing through all webpages found on the website, please wait...")
        time.sleep(1)
        print("Processing each webpage for emails, please wait...\n")
        time.sleep(1)
        print("\nThe following emails were found on all webpages of https://casl.website: ")
        time.sleep(1)
        # iterating through all emails and printing them out
        for email in self.email:
            time.sleep(1)
            print(email)
        print("\n\n")

    # function that prints out all zip codes
    def printZip(self):       
        print("Parsing through all webpages found on the website, please wait...")
        time.sleep(1)
        print("Processing each webpage for zipcodes, please wait...\n")
        time.sleep(1)
        print("\nThe following zipcodes were found on all webpages of https://casl.website: ")
        time.sleep(1)
        # iterating through all zip codes and printing them out
        for z in self.zips:
            time.sleep(1)
            print(z)
        print("\n\n")

    # function that prints out all textual content on all webpages
    def printText(self):
        print("Parsing through all webpages found on the website, please wait...")
        time.sleep(1)
        print("Processing each webpage for textual content, please wait...\n")
        time.sleep(1)
        print("\nThe following texts were found on all webpages of https://casl.website: ")
        time.sleep(1)
        # printing out all text
        print(self.allText)
        print('\n\n')

    # function that prints out all unique vocab
    def printUniqueVocab(self):
        print("Parsing through all webpages found on the website, please wait...")
        time.sleep(1)
        print("Tokenizing each word in the text using NLTK tokenizer function, please wait...\n")
        time.sleep(1)
        # tokenizer variable to split only on words, and not special chars
        tokenizer = nltk.RegexpTokenizer(r"\w+")
        # self object variable that holds unique tokens from text
        self.uniqueWords = list(set(tokenizer.tokenize(self.allText)))
        print("The following unique words were found on all pages of the website: \n")
        # printing out all unique words
        print(self.uniqueWords)
        print("\n\n")

    # function that generates pos tags from all words in the text
    def posTags(self):
        # performing pos tags on each unique word in text
        posTags = nltk.pos_tag(self.uniqueWords)
        time.sleep(1)
        # creating a noun and verb set to hold all unique nouns and verbs
        self.nouns = set()
        self.verbs = set()

        # iterating through the postags and adding nouns and verbs to their sets
        for i in posTags:
            if 'NN' in i[1]:
                self.nouns.add(i[0])
                
            if 'VB' in i[1]:
                self.verbs.add(i[0])
        
    # function that prints the unique verbs
    def printVerbs(self):
        print("Performing pos tags on each unique word in text, please wait...\n")
        time.sleep(1)
        print("The following unique verbs were found in the text of each webpage on the website: ")
        # prints a list of all unique verbs
        print(list(self.verbs))
        print('\n\n')

    # function that prints all unique verbs
    def printNouns(self):
        print("Performing pos tags on each unique word in text, please wait...\n")
        time.sleep(1)
        print("The following unique nouns were found in the text of each webpage on the website: ")
        # prints all unique nouns
        print(list(self.nouns))
        print('\n\n')

if __name__ == '__main__':
    # Print Basic Script Information
    print()
    print(SCRIPT_NAME)
    print(SCRIPT_VERSION)
    print(SCRIPT_AUTHOR)
    print()  
    time.sleep(2)

    print("This final scripting project will scrape the https://casl.website/ within CyberApolis")
    print("and generate a report that contains the following information:")
    time.sleep(1)
    print("1. Unique URLs of all the pages found on the website")
    time.sleep(1)
    print("2. Unique URL links to images found on the website")
    time.sleep(1)
    print("3. Extract phone numbers and emails found on the website")
    time.sleep(1)
    print("4. Extract any zipcodes")
    time.sleep(1)
    print("5. Extract all text content from each of the pages and store them in a string variable")
    time.sleep(1)
    print("6. A list of all unique vocabulary found on the website")
    time.sleep(1)
    print("7. A list of all possible verbs")
    time.sleep(1)
    print("8. A list of all possible nouns\n\n")
    time.sleep(2)

    print("1. Unique URLs of all the pages found on the website\n")
    time.sleep(1)

    c = getRequests()
    c.getLinks()

    print("2. Unique URL links to images found on the website\n")
    time.sleep(1)
    c.getINFO()
    c.printImages()
    print("3. Extract phone numbers and emails found on the website\n")
    c.printNums()
    c.printEmails()
    print("4. Extract any zipcodes")
    time.sleep(1)
    c.printZip()
    print("5. Extract all text content from each of the pages and store them in a string variable")
    time.sleep(1)
    c.printText()
    print("6. A list of all unique vocabulary found on all pages of the website\n")
    time.sleep(1)
    c.printUniqueVocab()
    time.sleep(2)
    c.posTags()
    print("7. A list of all possible verbs")
    time.sleep(1)
    c.printVerbs()
    print("8. A list of all possible nouns\n\n")
    time.sleep(2)
    c.printNouns()

    print('\nScript Complete\n')