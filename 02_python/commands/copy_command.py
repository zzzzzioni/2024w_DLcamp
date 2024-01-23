from .base_command import BaseCommand
import os
import shutil
from typing import List

class CopyCommand(BaseCommand):
    def __init__(self, options: List[str], args: List[str]) -> None:
        """
        Initialize the CopyCommand object.

        Args:
            options (List[str]): List of command options.
            args (List[str]): List of command arguments.
        """
        super().__init__(options, args)

        # Override the attributes inherited from BaseCommand
        self.description = 'Copy a file or directory to another location'
        self.usage = 'Usage: cp [source] [destination]'

        # TODO 6-1: Initialize any additional attributes you may need.
        # Refer to list_command.py, grep_command.py to implement this.
        self.name = 'cp'
        self.options = options
        self.files = self.args[0] 
        self.dest_dir = self.args[1]

    def execute(self) -> None:
        """
        Execute the copy command.
        Supported options:
            -i: Prompt the user before overwriting an existing file.
            -v: Enable verbose mode (print detailed information)
        
        TODO 6-2: Implement the functionality to copy a file or directory to another location.
        You may need to handle exceptions and print relevant error messages.
        You may use the file_exists() method to check if the destination file already exists.
        """
        # Your code here
        if self.file_exists(directory=self.dest_dir, file_name=self.files):
            if '-v' in self.options:
                print(f"cp: copying '{self.files}' to '{self.dest_dir}'")
            else:
                pass
            if '-i' in self.options:
                command = input(f"cp: overwite '{self.dest_dir}/{self.files}'? (y/n)")
                if command=='y':
                    shutil.copy(self.files, self.dest_dir+"/")
                else: 
                    pass
            else:
                shutil.copy(self.files, self.dest_dir+"/")
        else:
            if '-v' in self.options:
                print(f"cp: copying '{self.files}' to '{self.dest_dir}'")
            else:
                pass         
            shutil.copy(self.files, self.dest_dir+"/")
        

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
