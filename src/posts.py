import json
from datetime import datetime
from dateutil import parser
from os import listdir
from os.path import isfile, join


class PostHandler:
    """
    Keeps track of the image folder.

    :Args:
    - path: str, path to folder

    :Usage:
        PostHandler('<path_to_folder>',)

    """
    def __init__(self, path):
        self.path = path

    def initialize_me(self):
        """
        https://stackoverflow.com/questions/3207219/how-do-i-list-all-files-of-a-directory 
        """
        self.pictures = [f for f in listdir(self.path) if isfile(join(self.path, f))]

        with open('posts.json', 'r') as posts:
            data = json.load(posts)

            posts = self.get_posts_from_json(data),
    
    def get_posts_from_json(self, data):
        return_list = []
        for post in data['posts']:
            return_list.append(
                (
                    description = post['description'],
                    image = post['image'],
                    post_date = parser.parse(post['post_date']),
                    has_been_posted = post['has_been_posted']
                )
            )
        self.posts = return_list
        return return_list