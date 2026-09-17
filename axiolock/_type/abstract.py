import abc

from types import EllipsisType
from typing import TYPE_CHECKING, Callable, Self, TypeAlias, Any

    
if TYPE_CHECKING:
    _Marshallable: TypeAlias = (bool | int | float | complex | 
                               str | bytes | bytearray | slice |
                               list["_Marshallable"] | 
                               dict["_Marshallable", "_Marshallable"] | 
                               tuple["_Marshallable", ...] | 
                               set["_Marshallable"] | 
                               frozenset["_Marshallable"] | 
                               EllipsisType | StopIteration | None)
    """
    A type alias for values that can be marshalled.
    """
    
else:
    _Marshallable: TypeAlias = object


class Picklable(metaclass=abc.ABCMeta):
    """
    An abstract base class that defines the interface for picklable objects.
    """

    @abc.abstractmethod
    def __getstate__(self) -> State:
        """
        Return the state of the object for pickling.
        """
        ...

    @abc.abstractmethod
    def __setstate__(self, state: State) -> None:
        """
        Restore the state of the object from pickling.
        """
        ...

    def __reduce__(self) -> tuple[Callable[..., Self], tuple, State]:
        """
        Return a tuple that can be used to reconstruct the object.
        """
        return self.__class__, (), self.__getstate__()


Serializable: TypeAlias = _Marshallable | Picklable
"""
A type alias for values that can be serialized, which includes both marshallable and picklable objects.
"""

State: TypeAlias = dict[str, Serializable]
"""
A type alias for the state of an object, represented as a dictionary mapping string keys to serializable values.

It is used to store the state of an object for pickling and unpickling. Generally via the shelve module, the state of an object can be saved to a file and later restored, allowing for persistent storage of objects across program executions.
"""


class IntegrityCheckable(Picklable, metaclass=abc.ABCMeta):
    """
    An abstract base class that defines the interface for integrity checkable objects.
    """
    
    def __init__(self) -> None:
        """
        Initialize the integrity checkable object.
        """
        self.__cache_hash: int | None = None
    
    @abc.abstractmethod
    def __hash__(self) -> int:
        """
        Return a hash value for the serialized object.
        """
        return 0
        
    @abc.abstractmethod
    def __eq__(self, other: Any) -> bool:
        """
        Check if the object is equal to another object.
        """
        ...
    
    @abc.abstractmethod
    def __getstate__(self) -> State:
        """
        Return the state of the object for pickling.
        """
        return self.__getstate__() | {"__cache_hash": hash(self)}