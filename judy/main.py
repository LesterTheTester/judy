__author__ = 'LesterTheTester'
import os
import requests
import json
import argparse

def parse_args():
    parser = argparse.ArgumentParser(description='Get Judgemental on your build log!')
    parser.add_argument('build_log', type=argparse.FileType('r'),
                        help='The build log for Judy to get Judgemental on!')
    parser.add_argument('-f', '--rules', type=argparse.FileType('r'), default='judy.json',
                        help='The rules file, a JSON dict of key-value pairs. KEY: string to search for in build log. VALUE: HTML message to post if KEY exists in build log.')
    parser.add_argument('-t', '--token',
                        help='The OAUTH token to use for github, defaults to env var JUDY_OAUTH_TOKEN')
    parser.add_argument('-r', '--repo',
                        help='The github repo (i.e. LesterTheTester/judy), defaults to env var JUDY_REPO')
    parser.add_argument('-i', '--issue',
                        help='The issue number to comment on (i.e., "1"), defaults to env var JUDY_ISSUE')
    parser.add_argument('-p', '--prelude', default=':chicken: cluck! cluck! :chicken:',
                        help='Prelude to include with all messages')
    parser.add_argument('-s', '--slack',
                        help='Slack Incoming Webhook URL for optional slack integration')

    arguments = parser.parse_args()
    if not arguments.token:
        try:
            arguments.token = os.environ['GITHUB_OAUTH_TOKEN']
        except KeyError:
            if not arguments.slack:
                print '--token not provided and no JUDY_OAUTH_TOKEN env var'
    if not arguments.repo:
        try:
            arguments.repo = os.environ['GITHUB_REPO']
        except KeyError:
            if not arguments.slack:
                print '--repo not provided and no JUDY_REPO env var'
    if not arguments.issue:
        try:
            arguments.issue = os.environ['GITHUB_ISSUE']
        except KeyError:
            if not arguments.slack:
                print '--issue not provided and no JUDY_ISSUE env var'
    if not arguments.slack:
        try:
            arguments.slack = os.environ['SLACK_WEBHOOK_URL']
        except KeyError:
            if not (arguments.repo and arguments.issue and arguments.token):
                print 'No Github or Slack credentials provided!'
    return arguments

def main():
    message = ''
    arguments = parse_args()
    rules = json.loads(arguments.rules.read())
    arguments.rules.close()
    build_log = arguments.build_log.read().decode('utf-8')
    arguments.build_log.close()
    for rule in rules.keys():
        if rule in build_log:
            message += '<br>' + rules[rule]
    if message:
        message = arguments.prelude + message
        print message
        # POST the message to github
        if arguments.repo and arguments.issue and arguments.token:
            URL = 'https://api.github.com/repos/%s/issues/%s/comments' % (arguments.repo, arguments.issue)
            DATA = json.dumps({'body': message})
            HEADERS = {'Authorization' : 'token %s' % arguments.token}
            response = requests.post(URL, data=DATA, headers=HEADERS)
            if response.status_code in (200, 201):
                print 'Got Judgemental! (on Github)'
            elif response.status_code == 401:
                print 'Unauthorized! Please check my Github OAUTH Token!'
            else:
                print 'Github POST Failed! Status Code: ' + str(response.status_code)
        # POST the message to slack
        if arguments.slack:
            URL = arguments.slack
            DATA = json.dumps({'payload': {'text': message}})
            response = requests.post(URL, data=DATA)
            if response.status_code in (200, 201):
                print 'Got Judgemental! (on Slack)'
            else:
                print 'Slack POST Failed! Status Code: ' + str(response.status_code)

if __name__ == '__main__':
    main()