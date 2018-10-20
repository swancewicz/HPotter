#!/usr/bin/python3

import sys
from command_response import ssh_commands
#print(sys.path)

## This command will allow input to be a string like a normal command ex: vi /etc/shadow
console_input = ' '.join(sys.argv[1:])
#console_input = sys.argv[1]


answer = ssh_commands[console_input]


print("{}".format(answer))

