__author__ = 'night'

import praw
import re as re
import time
import util

# CONFIGURATION #
USERNAME = ""
USERAGENT = ""
PASSWORD = ""
WAIT = 20
STATUS_OK = True

def login():
    """
    Attempts to login to reddit
    """
    r = praw.Reddit(USERAGENT)
    try:
        r.login(USERNAME, PASSWORD)
    except praw.errors.InvalidUserPass:
        print("Wrong password")
    return r

def send_error_message(user, error):
    """ sends an error message to the user if flair update fails. """
    global goodbot.send_message(user, "Error while applying flair\n\n[0]".format(error));

def check_mail(r):
    messages = r.get_unread()
    for message in messages:
        action = "None"
        desc = "None"
        message.mark_as_read()
        if util.clean(message.subject) == 'flair request':
            # parse flair request
            request = parse_request(message.body)

        else:
            # send confused reply
            r.send_message(message.author, 'Request not recognized',
            'A message from ' + message.author + ' was received, but it was not a valid request. If you were trying to send a request please check your subject formatting and try again.')

def parse_request(request):
    """" takes string input and returns request in the form of a tuple. """""

    tuple = []

    return tuple
def validate_request(requesttuple):


if __name__ == '__main__':
    # load config
    try:
        # credential file
        import config

        USERNAME = config.username
        PASSWORD = config.password
        USERAGENT = config.useragent


    # warn anyone who tries to copy and run this bot without including credentials
    except ImportError:
        print("Attempt to load configuration from config.py failed. Program ended.")

    goodbot = login();

    while STATUS_OK:
        check_mail()
        time.sleep(WAIT)
