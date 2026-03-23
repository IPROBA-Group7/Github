from typing import List


def average(numbers: List[float]) -> float:
    """
    Calculate the average of a list of numbers.
    """
    if not numbers:
        raise ValueError("List must not be empty")

    if not all(isinstance(n, (int, float)) for n in numbers):
        raise TypeError("All elements must be numbers")

    return sum(numbers) / len(numbers)


if __name__ == "__main__":
    data = [10, 20, 30]
    print(f"Average: {average(data)}")
