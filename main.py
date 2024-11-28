from typing import List, Tuple


def find_two_sum(nums: List[int], target: int) -> Tuple[int, int] | None:
    # dictionary to check complements
    num_dict = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_dict:
            return num_dict[complement], i
        num_dict[num] = i
    return None


def main() -> None:
    nums = [4, 13, 7, 2]
    target = 11

    result = find_two_sum(nums, target)
    if result:
        print(f"Indexes of numbers that add up to {target}: {result}")
    else:
        print("No two numbers add up to the target.")


if __name__ == "__main__":
    main()
