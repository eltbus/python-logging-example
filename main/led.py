import logging
import asyncio


logger = logging.getLogger(__name__)


async def leave_babe() -> bool:
    logger.info(msg="Babe, baby, baby, I'm gonna leave you")
    logger.info(msg="I said baby, you know I'm gonna leave you")
    await asyncio.sleep(3)
    logger.info(msg="I'll leave you when the summertime")
    logger.info(msg="Leave you when the summer comes a-rollin'")
    logger.info(msg="Leave you when the summer comes along")
    return False  # era un farol
