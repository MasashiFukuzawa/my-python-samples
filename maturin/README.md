# PyO3/maturin sample

This is a sample class that try to use PyO3/maturin.

## How To Play

```sh
$ docker build . -t samples
$ docker run -it --rm samples /bin/bash
> sh maturin/setup.sh
> python maturin/main.py
alphabet_count=10
digit_count=0
other_count=3
```

## References

- https://www.maturin.rs/
- https://gihyo.jp/article/2023/07/monthly-python-2307
- https://zenn.dev/kitchy/articles/5b4578ca9a87d9
