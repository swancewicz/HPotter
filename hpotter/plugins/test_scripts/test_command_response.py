#!/usr/bin/python3

import sys
from command_response import ssh_commands

console_input = ' '.join(sys.argv[1:])
#console_input = sys.argv[1]
answer = ssh_commands[console_input]


print("{}".format(answer))

