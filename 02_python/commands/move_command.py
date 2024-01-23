from .base_command import BaseCommand
import os
import shutil
from typing import List

class MoveCommand(BaseCommand):
    def __init__(self, options: List[str], args: List[str]) -> None:
        """
        Initialize the MoveCommand object.

        Args:
            options (List[str]): List of command options.
            args (List[str]): List of command arguments.
        """
        super().__init__(options, args)

        # Override the attributes inherited from BaseCommand
        self.description = 'Move a file or directory to another location'
        self.usage = 'Usage: mv [source] [destination]'

        # TODO 5-1: Initialize any additional attributes you may need.
        # Refer to list_command.py, grep_command.py to implement this.
        self.name = 'mv'
        self.options = options
        self.files = self.args[0] 
        self.dest_dir = self.args[1]
        

    def execute(self) -> None:
        """
        Execute the move command.
        Supported options:
            -i: Prompt the user before overwriting an existing file.
            -v: Enable verbose mode (print detailed information)
        
        TODO 5-2: Implement the functionality to move a file or directory to another location.
        You may need to handle exceptions and print relevant error messages.
        """
        # Your code here
        if self.file_exists(directory=self.dest_dir, file_name=self.files):
            if '-v' in self.options:
                print(f"mv: moving '{self.files}' to '{self.dest_dir}'")
            else:
                pass
            if '-i' in self.options:
                command = input(f"mv: overwite '{self.dest_dir}/{self.files}'? (y/n)")
                if command=='y':
                    shutil.move(self.files, self.dest_dir+"/")
                else: 
                    pass
            else:
                print(f"mv: cannot move '{self.files}' to '{self.dest_dir}': Destination path '{self.dest_dir}/{self.files}'\nalready exists")
        else:
            if '-v' in self.options:
                print(f"mv: moving '{self.files}' to '{self.dest_dir}'")
            else:
                pass         
            shutil.move(self.files, self.dest_dir+"/")
                
    
    def file_exists(self, directory: str, file_name: str) -> bool:
        """
        Check if a file exists in a directory.
        Feel free to use this method in your execute() method.

        Args:
            directory (str): The directory to check.
            file_name (str): The name of the file.

        Returns:
            bool: True if the file exists, False otherwise.
        """
        file_path = os.path.join(directory, file_name)
        return os.path.exists(file_path)
