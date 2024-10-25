import logging
import traceback

from .context import Context, ctx_context


class LogContextInjectiveFilter(logging.Filter):
    """
    A filter to inject context-specific attributes into each record
    """

    def filter(self, record: logging.LogRecord) -> bool:
        context: Context = ctx_context.get()
        record.context_user = context.user
        return True


class ExceptionInjectiveFilter(logging.Filter):
    """
    A filter to inject parsed exception attributes into each record
    """

    def filter(self, record: logging.LogRecord) -> bool:
        if record.exc_info:
            # Add exception information to the logging message
            e_type, e, tb = record.exc_info
            tb_as_str_list = traceback.format_tb(tb)
            record.context_exception_type = str(e_type)
            record.context_exception = str(e)
            record.context_exception_traceback = "".join(tb_as_str_list)
        else:
            record.context_exception_type = "n/a"
            record.context_exception = "n/a"
            record.context_exception_traceback = "n/a"
        return True
