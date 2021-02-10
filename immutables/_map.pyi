from typing import Any
from typing import Dict
from typing import Generic
from typing import Iterable
from typing import Iterator
from typing import Mapping
from typing import Optional
from typing import Tuple
from typing import Type
from typing import Union
from typing import overload

from ._protocols import IterableItems
from ._protocols import MapItems
from ._protocols import MapKeys
from ._protocols import MapMutation
from ._protocols import MapValues
from ._protocols import HKT
from ._protocols import OKT
from ._protocols import T
from ._protocols import VT_co


class Map(Mapping[HKT, VT_co]):
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self: Map[str, VT_co], **kw: VT_co) -> None: ...
    @overload
    def __init__(
        self, __col: Union[IterableItems[HKT, VT_co], Iterable[Tuple[HKT, VT_co]]]
    ) -> None: ...
    @overload
    def __init__(
        self: Map[Union[HKT, str], VT_co],
        __col: Union[IterableItems[HKT, VT_co], Iterable[Tuple[HKT, VT_co]]],
        **kw: VT_co
    ) -> None: ...
    def __reduce__(self) -> Tuple[Type[Map[HKT, VT_co]], Tuple[Dict[HKT, VT_co]]]: ...
    def __len__(self) -> int: ...
    def __eq__(self, other: Any) -> bool: ...
    # Technically, the following two overloads are overlapping, but that is
    # how the implementation functions:
    # Map({1: "a"}).update({2: "b"}) produces Map[int, str], but
    # Map({1: "a"}).update(two="b") produces Map[Union[int, str], str]
    @overload
    def update(  # type: ignore[misc]
        self,
        __col: Union[IterableItems[OKT, T], Iterable[Tuple[OKT, T]]]
    ) -> Map[Union[HKT, OKT], Union[VT_co, T]]: ...
    @overload
    def update(
        self,
        __col: Union[IterableItems[OKT, T], Iterable[Tuple[OKT, T]]],
        **kw: T
    ) -> Map[Union[HKT, OKT, str], Union[VT_co, T]]: ...
    @overload
    def update(self, **kw: T) -> Map[Union[HKT, str], Union[VT_co, T]]: ...
    def mutate(self) -> MapMutation[HKT, VT_co]: ...
    def set(self, key: OKT, val: T) -> Map[Union[HKT, OKT], Union[VT_co, T]]: ...
    def delete(self, key: HKT) -> Map[HKT, VT_co]: ...
    @overload
    def get(self, key: HKT) -> Optional[VT_co]: ...
    @overload
    def get(self, key: HKT, default: Union[VT_co, T]) -> Union[VT_co, T]: ...
    def __getitem__(self, key: HKT) -> VT_co: ...
    def __contains__(self, key: Any) -> bool: ...
    def __iter__(self) -> Iterator[HKT]: ...
    def keys(self) -> MapKeys[HKT]: ...  # type: ignore[override]
    def values(self) -> MapValues[VT_co]: ...  # type: ignore[override]
    def items(self) -> MapItems[HKT, VT_co]: ...  # type: ignore[override]
    def __hash__(self) -> int: ...
    def __dump__(self) -> str: ...
    def __class_getitem__(cls, item: Any) -> Type[Map[Any, Any]]: ...
