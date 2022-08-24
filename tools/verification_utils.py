import math

def printErrorTolerance(tol: float) -> None:
    """
    Prints a tolerance using the format expected by the test harness
    """
    print(f"#L2_error_norm_tolerance: {tol}")

def computeAndPrintErrorNorm(computed_data: list, baseline_data: list) -> None:
    """
    Computes the L2 norm of the difference of computed_data and baseline_data and
    prints the result using the format expected by the test harness
    """
    error_norm = sum((x - y)**2 for x, y in zip(computed_data, baseline_data))
    error_norm = math.sqrt(error_norm)
    print(f"#L2_error_norm_value: {error_norm}")

def printLineSolution(x_data: list, computed_y_data: list, baseline_y_data) -> None:
    """
    Prints a solution computed along a line, including the position on the line and
    both the computed band baseline solution values.
    """
    print("#X, computed, analytical")
    for x, computed, baseline in zip(x_data, computed_y_data, baseline_y_data):
        print(x, computed, baseline)
