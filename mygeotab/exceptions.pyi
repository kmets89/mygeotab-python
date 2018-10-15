from typing import (
    Dict,
    List,
    Union,
)


class AuthenticationException:
    def __init__(self, username: str, database: str, server: str, *args, **kwargs) -> None: ...
    def __str__(self) -> str: ...
    @property
    def message(self) -> str: ...


class MyGeotabException:
    def __init__(
        self,
        full_error: Dict[str, Union[str, int, Dict[str, Union[str, int]], List[Dict[str, str]]]],
        *args,
        **kwargs
    ) -> None: ...
    def __str__(self) -> str: ...


class TimeoutException:
    def __init__(self, server: str, *args, **kwargs) -> None: ...
    def __str__(self) -> str: ...
    @property
    def message(self) -> str: ...
