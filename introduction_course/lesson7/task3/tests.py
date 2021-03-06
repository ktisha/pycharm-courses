from test_helper import run_common_tests, get_task_windows, passed, failed, import_task_file

def test_window1():
    window = get_task_windows()[0]
    if "1" in window:
        passed()
    else:
        failed("Initialize b with 1")


def test_window2():
    window = get_task_windows()[1]
    if "b" in window and "a" in window:
        passed()
    else:
        failed("Update b with a + b")

def test_window3():
    window = get_task_windows()[2]
    if "tmp_var" in window:
        passed()
    else:
        failed("Update a with tmp_var")

def test_function():
    try:
        my_file = import_task_file()
        if my_file.fib(10) == [0, 1, 1, 2, 3, 5, 8]:
            passed()
        else:
            failed("Check your function on n = 10")
    except:
        failed("File contains syntax errors")



if __name__ == '__main__':
    run_common_tests()
    test_window1()
    test_window2()
    test_window3()
    test_function()