import sys
from typing import Any
from typing import Hashable
from typing import Iterable
from typing import Iterator
from typing import NoReturn
from typing import Optional
from typing import Tuple
from typing import TypeVar
from typing import Union
from typing import overload

if sys.version_info >= (3, 8):
    from typing import Protocol
    from typing import TYPE_CHECKING
else:
    from typing_extensions import Protocol
    from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from ._map import Map

HKT = TypeVar('HKT', bound=Hashable)
OKT = TypeVar('OKT', bound=Hashable)
KT_co = TypeVar('KT_co', covariant=True)
T = TypeVar('T')
VT = TypeVar('VT')
VT_co = TypeVar('VT_co', covariant=True)
MM = TypeVar('MM', bound='MapMutation[Any, Any]')


class MapKeys(Protocol[KT_co]):
    def __len__(self) -> int: ...
    def __iter__(self) -> Iterator[KT_co]: ...


class MapValues(Protocol[VT_co]):
    def __len__(self) -> int: ...
    def __iter__(self) -> Iterator[VT_co]: ...


class MapItems(Protocol[KT_co, VT_co]):
    def __len__(self) -> int: ...
    def __iter__(self) -> Iterator[Tuple[KT_co, VT_co]]: ...


class IterableItems(Protocol[KT_co, VT_co]):
    def items(self) -> Iterable[Tuple[KT_co, VT_co]]: ...


class MapMutation(Protocol[HKT, VT]):
    def set(self, key: HKT, val: VT) -> None: ...
    def __enter__(self: MM) -> MM: ...
    def __exit__(self, *exc: Any) -> bool: ...
    def __iter__(self) -> NoReturn: ...
    def __delitem__(self, key: HKT) -> None: ...
    def __setitem__(self, key: HKT, val: VT) -> None: ...
    @overload
    def pop(self, __key: HKT) -> VT: ...
    @overload
    def pop(self, __key: HKT, __default: T) -> Union[VT, T]: ...
    @overload
    def get(self, key: HKT) -> Optional[VT]: ...
    @overload
    def get(self, key: HKT, default: Union[VT, T]) -> Union[VT, T]: ...
    def __getitem__(self, key: HKT) -> VT: ...
    def __contains__(self, key: object) -> bool: ...

    @overload
    def update(
        self,
        __col: Union[IterableItems[HKT, VT], Iterable[Tuple[HKT, VT]]]
    ) -> None: ...

    @overload
    def update(
        self: 'MapMutation[Union[OKT, str], VT]',
        __col: Union[IterableItems[HKT, VT], Iterable[Tuple[HKT, VT]]],
        **kw: VT
    ) -> None: ...

    @overload
    def update(
        self: 'MapMutation[Union[OKT, str], VT]',
        __col: Iterable[Tuple[HKT, VT]],
        **kw: VT
    ) -> None: ...
    @overload
    def update(self: 'MapMutation[Union[OKT, str], VT]', **kw: VT) -> None: ...
    def finish(self) -> 'Map[HKT, VT]': ...
    def __len__(self) -> int: ...
    def __eq__(self, other: Any) -> bool: ...
