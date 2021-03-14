import os
import sys
class system_shutdown_restart:
    def __init__(self, shutdown,restart,abort_shutdown,hibernate):
        shutdown.self  = shutdown
        restart.self  = restart
        abort_shutdown.self = abort_shutdown
        hibernate.self = hibernate

    def shutdown(self , shutdown = True):
        os.getcwd("C:\WINDOWS\system32>")
        os.system("shutdown /s",shell = True)

    def restart(self , restart = True ):
        os.getcwd("C:\WINDOWS\system32>")
        os.system("shutdown /r", shell = True)

    def abort_shutdown(self,abourt_shutdown = True):
        os.getcwd("C:\WINDOWS\system32>")
        os.system("shutdown /a", shell=True)

    def hibernate(self,hibernate = True):
        os.getcwd("C:\WINDOWS\system32>")
        os.system("shutdown /h", shell=True)


