import contextlib

@contextlib.contextmanager
def context():
    print('enter')
    try:
        yield
    finally:
        print('exit')