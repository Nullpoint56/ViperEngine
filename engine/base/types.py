# Define type-safe execution mode
from typing import TypeAlias, Literal

ExecutionMode: TypeAlias = Literal["sync", "async", "thread", "process"]