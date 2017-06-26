# tiny-lc-compiler-DeltaHeavy

Max Zinkus

Translates Lambda Calculus -> Python3 (Python3 is the implementation language *and* the target language)

`fix_recursion.py` contains the code that must be run before the output of the
translator is run/imported, so that Python3 doesn't hit recursion limits.

To run: `python3 translate.py <foo.rkt>` prints the python3 code to stdout
So to write it to `out.py`: `python3 translate.py test.rkt > out.pt`
then: `python3 -i fix_recursion.py` and in the interpreter `import out` will
start running the <1000 primes code.
