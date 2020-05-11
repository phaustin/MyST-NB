import locale, os
encoding=locale.getpreferredencoding()
print(f"here is the encoding: {encoding}")
print(f"here is the PYTHONUTF8 env variable {os.environ['PYTHONUTF8']}")
