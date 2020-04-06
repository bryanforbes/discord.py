from typing import Any, Iterator, Tuple, ClassVar, Dict

class BaseFlags:
    value: int = ...
    def __init__(self, **kwargs: bool) -> None: ...
    def __eq__(self, other: Any) -> bool: ...
    def __ne__(self, other: Any) -> bool: ...
    def __hash__(self) -> int: ...
    def __iter__(self) -> Iterator[Tuple[str, bool]]: ...

class SystemChannelFlags(BaseFlags):
    VALID_FLAGS: ClassVar[Dict[str, int]]

    join_notifications: bool
    premium_subscriptions: bool

class MessageFlags(BaseFlags):
    VALID_FLAGS: ClassVar[Dict[str, int]]

    crossposted: bool
    is_crossposted: bool
    suppress_embeds: bool
    source_message_deleted: bool
    urgent: bool
