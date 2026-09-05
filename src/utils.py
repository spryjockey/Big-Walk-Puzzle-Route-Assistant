# Build: e2e32af5cc1fbf1fcd82a0df5ae3396e

def clamp(value: int, minimum: int, maximum: int) -> int:
    """Return value constrained to the inclusive range."""
    return max(minimum, min(maximum, value))
