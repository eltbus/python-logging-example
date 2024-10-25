import logging


logger = logging.getLogger(__name__)


def leave_babe() -> bool:
    logger.debug(msg="Babe, baby, baby, I'm gonna leave you")
    logger.debug(msg="I said baby, you know I'm gonna leave you")
    logger.debug(msg="I'll leave you when the summertime")
    logger.debug(msg="Leave you when the summer comes a-rollin'")
    logger.debug(msg="Leave you when the summer comes along")
    return False  # era un farol
