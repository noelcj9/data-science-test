> Pandas + Numpy + Linear Algebra + Basic Python Testing

# Installation

```sh
mkvirtualenv ds-test
workon ds-test
pip install pip-tools
pip-compile requirements.in > requirements.txt
pip install -r requirements.txt
```

# Task Overview

Given is a file (A), (`test.csv`) consisting of N, M-dimensional vectors in the Euclidean space.

## Tasks

### Task - 1

#### Background

There are two operations defined by us:
1. Rotation: If say M=3, and one vector is (1, 0, 0), then rotation by 90º about the y-axis would mean the vector would be become (0, 0, 1) 
2. Translation: If say M=3, and one vector is (1, 0, 0), then translation of the entire vector space by (0, 1, 0) would mean every point is shifted by 1-unit in the y direction, thus (1, 0, 0) would become (1, 1, 0).

#### Goal

By accepting input from the user in a loop, which would be the action and corresponding value of the action, we have to create a new file of N, M-dimensional transformed vectors, by applying the transformations collected above.


Thus, on executing the program, for example, user is presented with:
```
Enter an operation (rotate/translate): "rotate"  # user enters rotate
Enter the angle of rotation and dimension around which to do it: 35 2  # ie, 35º around dimension 2
Enter more operations? (Y/n): Y  # user wants more operations
Enter an operation (rotate/translate): "translate"  # user enters translate
Enter the vector by which to translate: 2 -3 4 5 ...M values  # user enters the translation vector
Enter more operations? (Y/n): n  # user is done
<Program exits>
```
At the end of the program, a new file is created applying the operations collected above on the input file of N, M-dimensional vectors.

#### References

1. [vec. space rotation](https://en.wikipedia.org/wiki/Rotation_matrix)
2. [rotation addl.](https://math.stackexchange.com/q/3698915)
3. [translations](https://ogldev.org/www/tutorial06/tutorial06.html#:~:text=In%20general%20we%20can%20say,P%20to%20location%20P%2BV.)

### Task - 2

#### Background

A vector space transformation can be defined as a function that takes some Q-dimensional vectors
and transforms them to Q' dimensional vectors.

#### Goal

By accepting another file (B) containing N, M'-dimensional vectors, generate the transformation that was used to go from
(A) to (B).

#### References

[1](https://en.wikipedia.org/wiki/Least_squares)
[2](https://www.geeksforgeeks.org/singular-value-decomposition-svd/)


## Requirements

1. Two scripts called `task1.py` and `task2.py` need to be committed
2. Each file should be executable directly without any additional changes
3. Both files on completion should store the desired output in files (C).
4. Both scripts should be able to handle errors gracefully, viz. wrong dimensions of inputs, etc.

## Bonus

1. Scripts should be able to accept (A) name as input as well.
2. Files should be divided into proper functions and have useful docstrings.
2. No loops should be used (in Task-1, accept another file containing operations as input)
3. Both scripts should work well for large values of N and M
