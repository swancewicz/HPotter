#!/usr/bin/python3

import sys
from command_response import ssh_commands
from command_response import telnet_commands
#print(sys.path)

## This command will allow input to be a string like a normal command ex: vi /etc/shadow
console_input = ' '.join(sys.argv[1:])
#console_input = sys.argv[1]

console_input2 = "b" + str(console_input)
#print(console_input)

def ssh(console_input):
    if console_input in ssh_commands:
        answer = ssh_commands[console_input]
        print("{}".format(answer))

    else:
        print("please re-enter command")


def telnet(console_input):
    if console_input in telnet_commands:
        answer = telnet_commands[console_input]
        print("{}".format(answer))

    else:
        print("please re-enter command")

ssh(console_input)
#telnet(console_input)



