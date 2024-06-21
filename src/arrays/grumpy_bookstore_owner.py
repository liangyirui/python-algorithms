"""
There is a bookstore owner that has a store open for n minutes. Every minute, some number of customers enter the store. You are given an integer array customers of length n where customers[i] is the number of the customer that enters the store at the start of the ith minute and all those customers leave after the end of that minute.
On some minutes, the bookstore owner is grumpy. You are given a binary array grumpy where grumpy[i] is 1 if the bookstore owner is grumpy during the ith minute, and is 0 otherwise.
When the bookstore owner is grumpy, the customers of that minute are not satisfied, otherwise, they are satisfied.
The bookstore owner knows a secret technique to keep themselves not grumpy for minutes consecutive minutes, but can only use it once.
Return the maximum number of customers that can be satisfied throughout the day.
"""

def max_satisfied(customers: list[int], grumpy: list[int], minutes: int) -> int:
    satisfied = dissatisfied = max_dissatisfied = 0
    for i, (customer, owner) in enumerate(zip(customers, grumpy)):
        satisfied += customer * (1 - owner)
        dissatisfied += customer * owner
        if i >= minutes:
            dissatisfied -= customers[i - minutes] * grumpy[i - minutes]
        max_dissatisfied = max(max_dissatisfied, dissatisfied)
    return satisfied + max_dissatisfied


if __name__ == "__main__":
    customers = [1,0,1,2,1,1,7,5]
    grumpy = [0,1,0,1,0,1,0,1]
    minutes = 3
    print(max_satisfied(customers, grumpy, minutes))
