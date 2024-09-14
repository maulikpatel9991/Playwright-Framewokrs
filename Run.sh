# Run API tests
pytest Tests/API/ --maxfail=1 --disable-warnings -q

# Run UI tests
pytest Tests/UI/ --maxfail=1 --disable-warnings -q
