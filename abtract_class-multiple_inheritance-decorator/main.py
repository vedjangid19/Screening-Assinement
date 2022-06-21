import sys
from logger import logging
from custom_exception import FileParsingException

def word_replace(filename, old_word, new_word):
    """
    This function read file content.
    """
    try:
        with open(filename,mode='r') as example_file:
            data = example_file.read()
            print(data)
            logging.info(f"File content is : {data}")
        data = data.replace(old_word.lower(),new_word.lower())
        print(data)
        with open(filename,mode='w') as example_file:
            example_file.write(data)
            logging.info(f"File new content is : {data}")
        
        
    except Exception as e:
        file_parsing = FileParsingException(e,sys)
        print(file_parsing.error_message)
        logging.error(file_parsing.error_message)

def read_file(filename):
    """
    This function read file content.
    """
    try:
        with open(filename,mode='r') as example_file:
            data = example_file.read()
            
        return data
        
    except Exception as e:
        file_parsing = FileParsingException(e,sys)
        print(file_parsing.error_message)
        logging.error(file_parsing.error_message)


if __name__=="__main__":
    word_replace("example.txt","Placement","Screening")  
    print(read_file("example.txt"))      
        