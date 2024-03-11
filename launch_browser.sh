#!/bin/sh

#TODO - Add a check to see if Chrome is already running
#TODO - Add a check to see if the remote debugging port is already in use
#TODO - Support for other browsers and platforms [Linux, osx] -> Hi Phil :)

# Kill any existing Chrome processes
ps aux | grep -i 'google chrome' | awk '{print $2}' | xargs kill -9

# Launch Chrome with remote debugging port
cd ~ && open -n -a /Applications/Google\ Chrome.app --args --remote-debugging-port=9222