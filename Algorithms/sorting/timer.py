from timeit import repeat


def run_sorting_algorithm(algorithm, array):
    """
    Set up the context and prepare the call to the specified
    algorithm using the supplied array. Only import the
    algorithm function if it's not the built-in `sorted()`
    """

    setup_code = f"from __main__ import {algorithm}" \
        if algorithm != "sorted" else ""

    stmt = f"{algorithm}({array})"
    times = repeat(setup=setup_code, stmt=stmt, repeat=3, number=10)
    print(f"Algorithm: {algorithm}. Minimum execution time: {min(times)}")
