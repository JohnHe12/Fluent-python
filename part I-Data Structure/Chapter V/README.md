# Data Class Builders

Python offers a few ways to build a simple class that is just a collection of fields, with little or no extra functionality.

three ways to create data class:

* collections.namedtuple
    The simplest way—available since Python 2.6.

* typing.NamedTuple
    An alternative that requires type hints on the fields—since Python 3.5, with class syntax added in 3.6.

* @dataclasses.dataclass