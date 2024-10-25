from contextvars import ContextVar
from dataclasses import dataclass, field


@dataclass
class Context:
    user: str = field(default="n/a")


ctx_context: ContextVar[Context] = ContextVar("context", default=Context())
