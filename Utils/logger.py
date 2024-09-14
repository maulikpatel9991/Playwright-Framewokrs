# logger.py
import logging

class DuplicateFilter(logging.Filter):
    def __init__(self):
        super().__init__()
        self.logged_messages = set()

    def filter(self, record):
        message = record.getMessage()
        if message not in self.logged_messages:
            self.logged_messages.add(message)
            return True
        return False

def setup_logger(name, log_file, level=logging.DEBUG):
    """
    Setup a logger with the given name and log file.
    
    :param name: The name of the logger
    :param log_file: The file name for the log output
    :param level: The logging level
    :return: Configured logger instance
    """
    logger = logging.getLogger(name)
    logger.setLevel(level)
    
    # Create file handler
    file_handler = logging.FileHandler(log_file)
    
    # Create formatter and set it for the handler
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)
    
    # Add custom filter to the handler
    file_handler.addFilter(DuplicateFilter())
    
    # Add handler to the logger
    logger.addHandler(file_handler)
    
    return logger

# Define loggers with specific file names
logger1 = setup_logger('Date', 'test_log.log')

