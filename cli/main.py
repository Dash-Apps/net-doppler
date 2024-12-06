import cmd
import subprocess
import scapy.all as scapy
import re
#function for parsing arguments in commands.
def get_args(line):
    args = re.findall("-?[\\w.]+",line)
    return args

class ndCLI(cmd.Cmd):
    prompt = "ndCLI >>> "
    intro= "Thankyou for using Net Doppler!"
    def __init__(self):
        super().__init__()
    #parses the command before running any code
    def precmd(self,line):
        return line
    #allows you to perform commands respective to your os using subprocess
    def do_os_command(self,line):
        args =
        output = subprocess.Popen(['uname', '-a'], stdout=subprocess.PIPE).communicate()[0]
    #pings an ip address using the specified method
    def do_ping(self, line):
        print("Hello, World!")
    #returns your ip address
    def do_ip(self,line):
        pass
    def do_sp(self,line):
        print("")
    #exits the CLI
    def do_quit(self, line):
        return True

#if __name__ == '__main__':
 #   ndCLI().cmdloop()
print(get_args("ping -tcp -127.0.0.1 -test -test"))