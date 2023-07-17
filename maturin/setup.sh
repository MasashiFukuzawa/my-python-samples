#!bin/bash
cd maturin/strcounter

echo "$ maturin build -i python3 --release"
maturin build -i python3 --release

echo "$ pip install ."
pip install .
