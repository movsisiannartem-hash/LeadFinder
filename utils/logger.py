import logging

def setup_logger():
    logger = logging.getLogger("leadfinder")
    logger.setLevel(logging.INFO)

    filehandler = logging.FileHandler("data/leadfinder.log")
    formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")

    filehandler.setFormatter(formatter)
    logger.addHandler(filehandler)

    return logger