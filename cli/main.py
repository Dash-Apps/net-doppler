import cmd
import subprocess
import scapy.all as scapy
class ndCLI(cmd.Cmd):
    prompt = "ndCLI >>> "
    intro= "Thankyou for using Net Doppler!"
    def __init__(self):
        super().__init__()
    #parses the command before running any code
    def precmd(self,line):
        return line
    def do_ping(self, line):
        print("Hello, World!")
    def do_ip(self,line):
        pass
    def do_sp(self,line):
    def do_quit(self, line):
        """Exit the CLI."""
        return True
if __name__ == '__main__':
    ndCLI().cmdloop()