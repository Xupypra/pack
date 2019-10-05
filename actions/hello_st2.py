#!/usr/bin/python3
from st2common.runners.base_action import Action

class HelloStackStorm(Action):
    def run(self):
        print("Hellow Stackstorm, want to be friends?")
        return True, "Let's be friends!"
