import logging

from .context import Context, ctx_context


class ContextInjectionFilter(logging.Filter):
    """
    A filter to inject context-specific attributes into each record
    """

    def filter(self, record: logging.LogRecord) -> bool:
        context: Context = ctx_context.get()
        record.context_user = context.user
        return True
