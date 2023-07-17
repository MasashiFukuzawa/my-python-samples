# async/await sample

This is a sample using async/await syntax in Python, and is implemented assuming multiple calls to an external API with slow responses.

Parallel execution allows the process to be completed in 5s, whereas it would take 15s to complete the process if executed in series.

## How To Play

```sh
$ docker build . -t samples
$ docker run -it --rm samples python async_await/main.py
start:  wait for 1s.
start:  wait for 3s.
start:  wait for 5s.
start:  wait for 2s.
start:  wait for 4s.
finish: wait for 1s.
finish: wait for 2s.
finish: wait for 3s.
finish: wait for 4s.
finish: wait for 5s.
[<Response [200]>, <Response [200]>, <Response [200]>, <Response [200]>, <Response [200]>]
5s
```

## References

- https://docs.python.org/3/library/asyncio-task.html
- https://dev.classmethod.jp/articles/python-asyncio/
- https://iuk.hateblo.jp/entry/2017/01/27/173449
