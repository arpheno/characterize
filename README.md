## Synopsis

Characterize(working name) is a python library that generates characterization tests from an execution of a python program automatically.
## Code Example
at the top line of your `main.py` add `import characterize`:
~~~
import characterize
from sample_program.first.definitions import b
from sample_program.second.definitions import a
if __name__ == '__main__':
    a(3,4)
    a(6,5)
    b(12,12)
    b(13,12)
    b(11,12)
    b(16,12)
    b(10,12)
~~~
Then the tests for `a` and `b` are generated in the directory `autotests`.
## Motivation

A short description of the motivation behind the creation and maintenance of the project. This should explain **why** the project exists.

## Installation

pip install characterize

## Tests

To run the tests just execute `py.test .`

## Contributors

Let people know how they can dive into the project, include important links to things like issue trackers, irc, twitter accounts if applicable.

## License

Licensed under MIT
