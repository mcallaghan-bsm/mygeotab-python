from datetime import datetime
from typing import (
    Any,
    Dict,
    List,
    Optional,
    Union,
)


def _process(data: Any) -> Any: ...


def _query(
    server: str,
    method: str,
    parameters: Dict[str, Any],
    timeout: Union[float, int] = 300,
    verify_ssl: bool = True
) -> Any: ...


def get_api_url(server: str) -> str: ...


def get_headers() -> Dict[str, str]: ...


def process_parameters(parameters: Dict[str, Any]) -> Dict[str, Any]: ...


def server_call(
    method: Optional[str],
    server: Optional[str],
    timeout: Union[float, int] = 300,
    verify_ssl: bool = True,
    **parameters
) -> str: ...


class API:
    def __init__(
        self,
        username: Optional[str],
        password: Optional[str] = None,
        database: Optional[str] = None,
        session_id: Optional[Union[int, str]] = None,
        server: Optional[str] = 'my.geotab.com',
        timeout: int = 300
    ) -> None: ...
    @property
    def _is_verify_ssl(self) -> bool: ...
    @property
    def _server(self) -> str: ...
    def add(self, type_name: str, entity: Dict[str, Union[List[Dict[str, str]], str]]) -> str: ...
    def authenticate(self, is_global: bool = True) -> Credentials: ...
    def call(self, method: Optional[str], **parameters) -> Any: ...
    @staticmethod
    def from_credentials(credentials: Credentials) -> API: ...
    def get(self, type_name: str, **parameters) -> ResultList: ...
    def multi_call(
        self,
        calls: List[Union[List[Union[str, Dict[str, Union[str, Dict[str, str]]]]], List[str]]]
    ) -> List[Union[List[Dict[str, Union[int, datetime, str, List[Dict[str, str]], List[Dict[str, Union[str, Dict[str, float]]]]]]], str]]: ...
    def remove(self, type_name: str, entity: Dict[str, Union[List[Dict[str, str]], str]]) -> Dict[str, Union[str, int]]: ...
    def set(self, type_name: str, entity: Dict[str, Union[List[Dict[str, str]], str]]) -> Dict[str, Union[str, int]]: ...


class Credentials:
    def __init__(
        self,
        username: str,
        session_id: Optional[Union[int, str]],
        database: Optional[str],
        server: Optional[str],
        password: Optional[str] = None
    ) -> None: ...
    def __str__(self) -> str: ...
    def get_param(self) -> Dict[str, str]: ...


class GeotabHTTPAdapter:
    def init_poolmanager(self, connections: int, maxsize: int, block: bool = False, **pool_kwargs) -> None: ...
