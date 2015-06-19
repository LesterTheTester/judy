# judy
Judgemental Build-Reading Bot with Github and Slack Integration by LesterTheTester

Are you tired of reading build logs only to find out they failed for common,
easily observable reasons? Are your teammates tired of you endlessly reminding
them that their CI builds failed for inane reasons such as coding style checks,
unittests, or dependencies that they could have easily tested before checkin?

Enter <b>JudyTheJudgementalChicken</b>. She clucks so you don't have to!

<img src='http://s3.amazonaws.com/content-test/crash.jpg' width=300>
<img src='http://s3.amazonaws.com/content-test/lint.jpg' width=300>
<img src='http://s3.amazonaws.com/content-test/mocha.jpg' width=300>
<img src='http://s3.amazonaws.com/content-test/timeout.jpg' width=300>


<h3>Setup:</h3>

1. Install Judy

    $ sudo pip install judy-bot

2. Run

    $ judy -f RULES -t GITHUB_OAUTH_TOKEN -r AUTHOR/REPO -i ISSUE_NUMBER -s SLACK_WEBHOOK_URL BUILD.log

where...

<b>RULES</b> is a JSON file (defaults to judy.json) containing key-value pairs of
failure strings to search for, and HTML messages to post to Github / Slack:
i.e.

```
{
  "BUILD FAILED":"YOUR BUILD CRASHED!! <img src='http://s3.amazonaws.com/content-test/crash.jpg'>"
}
```

<b>GITHUB_OAUTH_TOKEN</b> is the Github OAUTH token for a user that can post comments to your project

<b>AUTHOR/REPO</b> is your Github repo, i.e. LesterTheTester/judy

<b>ISSUE_NUMBER</b> is the issue or pull request number to comment on, i.e. 1

<b>SLACK_WEBHOOK_URL</b> is the URL given by Slack for your Incoming Webhook Integration

<b>BUILD.log</b> is the build output to search through

<h4>Github and/or Slack may be used, but at least one is required, otherwise Judy will complain and just print to stdout</h4>

<h3>Environment variables:</h3>
Instead of specifying these on the commandline, you may set the environment variables:

<h4>Github Integration</h4>

<b>GITHUB_OAUTH_TOKEN

GITHUB_REPO

GITHUB_ISSUE</b>

<h4>Slack Integration</h4>

<b>SLACK_WEBHOOK_URL</b>

<h3>Continous Integration Support</h3>
Judy is easily integrated into most CI systems, take Travis-CI for example:

...in your .travis.yml, require judy and execute:

```
before_script:
 - export JUDY_REPO=LesterTheTester/judy
 - export JUDY_ISSUE=$TRAVIS_PULL_REQUEST
 - sudo pip install judy-bot
script:
 - your_build_command | tee build.log
after_script:
 - judy build.log
env:
 - JUDY_OAUTH_TOKEN="travis-encrypt your oauth token below"
 - secure: "asdfasdfasdfasdfasdfasdfasdfasdfasdfasdf"
```

<h3>Misc.</h3>

Consider physically embodying Judy with a Chicken puppet hat for your office:

http://www.amazon.com/Chicken-Hat-The-Clucker-Puppet/dp/B0040Z9ECG

Author makes no endorsement of this product nor receives any compensation for its sales.
