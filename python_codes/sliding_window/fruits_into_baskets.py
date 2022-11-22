from typing import List

def fruits_into_baskets(fruits:List[str]) -> int:
    max_length = 0
    window_start = 0
    basket = {}
    for window_end in range(len(fruits)):
        # most right fruit
        right_fruit = fruits[window_end]
        # Keep adding the fruits till we get K distinct fruits
        basket[right_fruit] = 1 + basket.get(right_fruit, 0)

        # shrink the basket whenever more than K distinct fruits are found
        while len(basket) > 2:
            # get the first fruit put in the basket
            left_fruit = fruits[window_start]
            # decrement the count of the left fruit
            basket[left_fruit] -= 1
            # remove the left
            if basket[left_fruit] == 0:
                del basket[left_fruit]
            window_start += 1

        max_length = max(max_length, window_end - window_start + 1)
    return max_length;

def main():
    basket = ["orange", "mango", "orange", "apple", "grape", "orange", "orange", "grape", "grape"]
    print("Max number of fruits to be picked:", fruits_into_baskets(basket))


if __name__ == "__main__":
    main()
