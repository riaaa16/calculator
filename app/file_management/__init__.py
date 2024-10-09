import os
import logging
from typing import Any

def setup_logging(level: int = logging.INFO) -> None:
    '''
    configures logging
    int level is the logging level to use
    '''
    logging.basicConfig(level=level, format='%(asctime)s - %(levelname)s - %(message)s')

class FileManager:
    """can read, write, and delete files"""
    def __init__(self, filename: str) -> None:
        """initializes filemanager with a specified file name"""
        self.filename = filename

    def write_file(self, data: str) -> None:
        """
        writes content to a file

        Raises:
            IOError if an I/O error occurs during writing
        """
        try:
            with open(self.filename, 'w') as file:
                file.write(data)
            logging.info(f"Successfully wrote to file: {self.filename}")
        except IOError as e:
            logging.error(f"Failed to write to file '{self.filename}'. Error: {e}")
            raise

    def read_file(self) -> str:
        """
        reads content of a file
        Raises:
            FileNotFoundError if file doesn't exist
            IOError if an I/O error occurs during reading
        """
        try:
            with open(self.filename, 'r') as file:
                content = file.read()
            logging.info(f"Successfully read from file: {self.filename}")
            return content
        except FileNotFoundError:
            logging.error(f"File not found: {self.filename}")
            raise
        except IOError as e:
            logging.error(f"Failed to read from file '{self.filename}'. Error: {e}")
            raise

    def delete_file(self) -> None:
        """
        deletes file

        Raises:
            OSError: If an error occurs during deletion.
        """
        try:
            os.remove(self.filename)
            logging.info(f"Successfully deleted file: {self.filename}")
        except FileNotFoundError:
            logging.warning(f"File not found for deletion: {self.filename}")
        except IOError as e:
            logging.error(f"Failed to delete file '{self.filename}'. Error: {e}")
            raise
