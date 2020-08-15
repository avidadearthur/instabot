from selenium import webdriver
from time import sleep
import os
from actions import Instactions
from upload import Instaupload
from posts import PostHandler

def main():
    user_username, user_password = os.getenv('USERNAME'), os.getenv('PASSWORD')
    path = "/Users/arthurquintao/Desktop/instabot-img/"

    # Make sure the env variables were given
    if not os.environ.get('USERNAME') or not os.environ.get('PASSWORD'):
        raise RuntimeError('\nUSERNAME or PASSWORD were not set')
    
    posthandler = PostHandler(path)
    instaupload = Instaupload(user_username, user_password)
    # instaupload.post_photo("Bip Bop tzzz - test01")
       

if __name__ == '__main__':
    main()