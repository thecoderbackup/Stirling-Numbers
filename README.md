## Introduction

Stirling numbers are a fascinating concept in combinatorial mathematics, named after the Scottish mathematician James Stirling. They play a crucial role in various fields, including algebra, number theory, and computer science. Stirling numbers come in two distinct forms: Stirling numbers of the first kind and Stirling numbers of the second kind. [See more here](https://en.wikipedia.org/wiki/Stirling_number).

The Stirling Numbers of the First Kind (unsigned) and the Second Kind are defined by the following recursions:

```
------- Stirling Numbers of the First Kind (Unsigned) -------
c(n, k) = (n - 1) * c(n - 1, k) + c(n - 1, k - 1)
c(0, 0) = 1
c(n, 0) = 0  for n > 0
c(0, k) = 0  for k > 0


------- Stirling Numbers of the Second Kind -------
S(n, k) = k * S(n - 1, k) + S(n - 1, k - 1)
S(0, 0) = 1
S(n, 0) = 0  for n > 0
S(0, k) = 0  for k > 0


```

## The Challenge.

Write a function `stirling_numbers(n, k)` that can compute both Unsigned Stirling Numbers of the First Kind and the Second Kind and return a tuple with two values `(firstKind, secondKind)`.


## Examples.
```python 
print(stirling_numbers(0, 0)) # Output: (1, 1)
print(stirling_numbers(0, 1)) # Output: (0, 0)
print(stirling_numbers(5, 2)) # Output: (50, 15)
print(stirling_numbers(6, 2)) # Output: (274, 31)

```

**Note:  If you want a little more challenge, try to make `stirling_numbers(n, k)` recursive, and do not define any more functions than `stirling_numbers(n, k)`.**
