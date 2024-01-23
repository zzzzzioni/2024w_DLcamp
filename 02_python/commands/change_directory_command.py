from .base_command import BaseCommand
import os
import shutil
from typing import List

class ChangeDirectoryCommand(BaseCommand):
    def __init__(self, options: List[str], args: List[str]) -> None:
        """
        Initialize the ChangeDirectoryCommand object.

        Args:
            options (List[str]): List of command options.
            args (List[str]): List of command arguments.
        """
        super().__init__(options, args)

        # Override the attributes inherited from BaseCommand
        self.description = 'Change the current working directory'
        self.usage = 'Usage: cd [options] [directory]'

        # TODO 7-1: Initialize any additional attributes you may need.
        # Refer to list_command.py, grep_command.py to implement this.
        self.name = 'cd'
        self.dest_dir = args[0]


    def execute(self) -> None:
        """
        Execute the cd command.
        Supported options:
            -v: Enable verbose mode (print detailed information)
        
        TODO 7-2: Implement the functionality to change the current working directory.
        You may need to handle exceptions and print relevant error messages.
        """
        # Your code here
        if os.path.exists(self.dest_dir):
            if '-v' in self.options:
                print(f"cd: changing directory to '{self.dest_dir}'")
                os.chdir(self.dest_dir)
            else:
                os.chdir(self.dest_dir)     
        else:
            if '-v' in self.options:
                print(f"cd: changing directory to '{self.dest_dir}'")
                print(f"cd: cannot change directory to '{self.dest_dir}': [Errno 2] No such file or directory: '{self.dest_dir}'")
            else:
                print(f"cd: cannot change directory to '{self.dest_dir}': [Errno 2] No such file or directory: '{self.dest_dir}'")    
            