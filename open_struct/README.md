# OpenStruct sample

This is a sample class that extends dict and behaves like Ruby's OpenStruct.

## How To Play

```sh
$ docker build . -t samples
$ docker run -it --rm samples python
>>> from samples.open_struct.main import *
>>> OpenStruct({'a': 1, 'b': 2})
>>> struct = OpenStruct(a=1, b=2)
>>> struct.add({'c': 3})
OpenStruct({'a': 1, 'b': 2, 'c': 3})
>>> struct['a'] = 3
>>> struct.b = 4
>>> struct
OpenStruct({'a': 3, 'b': 4, 'c': 3})
>>> struct.is_empty()
False
>>> struct.to_dict()
{'a': 3, 'b': 4, 'c': 3}
>>> struct.add({5: "d"})
OpenStruct({'a': 3, 'b': 4, 'c': 3, 5: 'd'})
>>> struct.a
3
>>> struct.b
4
>>> struct.c
3
>>> struct[5]
'd'
>>> struct.get(5)
'd'
>>> struct.get('d')
```

## References

- https://docs.ruby-lang.org/ja/latest/class/OpenStruct.html
- https://docs.python.org/3/library/collections.abc.html#collections.abc.MutableMapping
- https://stackoverflow.com/questions/21361106/how-would-i-implement-a-dict-with-abstract-base-classes-in-python
