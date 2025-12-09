##task3

# Write a function `approx_real_root(coeffs, interval)` that:

# - receives a list `coeffs` of four numbers representing a cubic polynomial,starting with the
# coefficient of the free term and finishing with the coefficient of x^3
# - receives a tuple `interval = (a, b)` with `a < b`,
# - assumes that **the polynomial has exactly one real root inside this interval**,
# - computes and returns a floating-point approximation of that root,
# - and ensures that the approximation is accurate to at least **1×10⁻⁹** in absolute error
# ---


def approx_real_root(coeffs, interval, tol=1e-9, max_iter=1000):
    c0, c1, c2, c3 = coeffs

    def f(x):
        return ((c3 * x + c2) * x + c1) * x + c0

    a, b = interval
    fa, fb = f(a), f(b)
    if fa == 0.0:
        return a
    elif fb == 0.0:
        return b
    for _ in range(max_iter):
        m = 0.5 * (a + b)
        fm = f(m)

        if abs(fm) <= tol or 0.5 * (b - a) <= tol:
            return m

        if fa * fm < 0:
            b, fb = m, fm
        else:
            a, fa = m, fm

    return 0, 5 * (a + b)
