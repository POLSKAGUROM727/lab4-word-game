def fib(n: int) -> int:
	"""Return the n-th Fibonacci number (recursive).

	Base cases:
	fib(0) == 0
	fib(1) == 1
	"""
	if n < 0:
		raise ValueError("n must be a non-negative integer")
	if n <= 1:
		return n
	return fib(n - 1) + fib(n - 2)


if __name__ == "__main__":
	# Quick sanity check
	n = 10
	print(f"fib({n}) = {fib(n)}")

