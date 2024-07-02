# verification
verification problems for Plato Analyze

## running tests

From the verification directory in your build area run 'ctest', i.e.:

```shell
cd build/tests/verification
ctest
```
Once the tests have run, generate the test documentation:

```shell
make VerificationDoc
```

This will create html documentation (load html/index.html in your favorite browser) and a verification report in 'verification.pdf' for your local build of Plato Analyze.
