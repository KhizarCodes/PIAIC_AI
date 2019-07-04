#PIAIC Official Assignment 3.
#Text and HTML file parser.

from html.parser import HTMLParser

def Text_Parser(file_name):
    try:
        with open(file_name,"r") as f_r:
            text_in_file = f_r.read()
            print("\nParsing Text file: ",file_name,"\n")
            total_words = text_in_file.split()
            print ("Total words = ",len(total_words))
            total_lines = text_in_file.count("\n")
            print("Total lines = ",total_lines+1)
            total_spaces = text_in_file.count(" ")
            print("Total spaces = ",total_spaces)
            total_tabs = text_in_file.count("\t")
            print("Total tabs = ",total_tabs)
            total_paragraphs = text_in_file.count("\n\n") + 1
            print("Total paragraphs = ",total_paragraphs)
            
    except FileNotFoundError:
        print ("\nFile name "+file_name+" was not found !")

    
def HTML_Parser(file_name):
    try:
        with open(file_name,"r") as hf_r:
            text_in_file = hf_r.read()
            tags_encountered = []
            class Parser(HTMLParser):
                def handle_starttag(self,tag,attrs):
                    tags_encountered.append(tag)
                def handle_endtag(self,tag):
                    tags_encountered.append(tag)
            ParserInit = Parser()
            ParserInit.feed(text_in_file)
            tags_with_occurance = {}
            for i in range(len(tags_encountered)):
                under_observation = tags_encountered[i]
                total_occurance = 0
                for j in range(len(tags_encountered)):
                    if tags_encountered[j] == under_observation:
                        total_occurance = total_occurance + 1
                    tags_with_occurance [under_observation] = [total_occurance]
            print("Parsing HTML file: ",file_name,"\n")
            for each_key,each_value in tags_with_occurance.items():
                print("\nTag \"",each_key,"\" occurs ",each_value," times.")

    except FileNotFoundError:
        print ("File name "+file_name+" was not found !")

print ("\nWhat do you want to Parse? (Select an option)\n\n\t(1) Text file (2) HTML file")
usr_input = int(input("\nOption number --> "))

if usr_input == 1:
    file_path = input ("\nEnter the path of the file: ")
    Text_Parser(file_path)
elif usr_input == 2:
    file_path = input("\nEnter the path of the file: ")
    HTML_Parser(file_path)
