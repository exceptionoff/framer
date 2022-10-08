import pytest
import time
import tempfile
import inspect

@pytest.fixture
def marks(request):
    marks_ = [m.name for m in request.node.iter_markers()]
    if request.node.parent:
        marks_ += [m.name for m in request.node.parent.iter_markers()]
    yield marks_


@pytest.fixture(autouse=True)
def time_measure(marks):
    start_time = None
    if 'what_time' in marks:
        start_time = time.time()
    yield
    if 'what_time' in marks:
        finish_time = time.time()
        print()
        print("--- %s seconds ---" % (finish_time - start_time))



# @pytest.fixture(scope='function')
# def print_test_function_arguments(request):
#     argspec = inspect.getfullargspec(request.node.function)
#     positional_args = argspec.args
#     print(positional_args)
#     print(request.getfixturevalue('n_frames'))
#     # positional_args.remove("print_test_function_arguments")
#     # for argname in positional_args:
#     #     print(argname, "=", request.getfixturevalue(argname))

@pytest.fixture(autouse=True)
def fps(marks, request):
    start_time = None
    n_frames = None
    if 'what_fps' in marks:
        start_time = time.time()
        n_frames = request.getfixturevalue('n_frames')

    yield
    if 'what_fps' in marks:
        finish_time = time.time()
        time_ = finish_time - start_time

        print()
        print(f"fps={1/time_*n_frames}")



@pytest.fixture(scope='session')
def tmp_dir():
    with tempfile.TemporaryDirectory() as tmpdirname:
        yield tmpdirname
