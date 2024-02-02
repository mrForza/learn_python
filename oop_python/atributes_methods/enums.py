from enum import Enum, IntEnum, unique


# Enum: this is a set of constants (symbolic names) each of these bound to unique value
# The first way to define your own enum: using your own class which inherit from enum.Enum class
class Color(Enum):
    RED = {'hex': '#dc2337', 'ansi': '\033[38;05;161m'}
    GREEN = {'hex': '#4db847', 'ansi': '\033[38;05;71m'}
    BLUE = {'hex': '#1954e6', 'ansi': '\033[38;05;26m'}
    BLACK = {'hex': '#000000', 'ansi': '\033[38;05;232m'}
    YELLOW = {'hex': '#e9ba16', 'ansi': '\033[38;05;178m'}
    ORANGE = {'hex': '#e86b17', 'ansi': '\033[38;05;172m'}
    PURPLE = {'hex': '#d12e98', 'ansi': '\033[38;05;162m'}


@unique  # This decorator obliges to create an enum with unique attributes
class AsciiEnum(IntEnum):
    A = 65
    M = 77
    W = 87
    # A = 123 - The repeated attribute can cause TypeError


# Another way to define an enum without creating a class
LoggingStatus = Enum(
    value='Status',
    names=(
        ('Success', 0),
        ('Warning', 1),
        ('Error', 2),
        ('Critical Error', 3),
    )
)
