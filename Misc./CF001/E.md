You are a novice magician, and are perfecting a trick using special colored cards: each card is red on one side and blue on the other, and each side has a number on it.

As part of your magician's training you often exercise your brain with the following challenge:

For each ith (1-based) card you know the number written on its red side redSides[i - 1], and the number written on its blue side blueSides[i - 1]. The task is to lay the cards down on a table in such a way that the sum of numbers written on their visible sides is as high as possible, and the difference between the number of cards with visible red sides and those with visible blue sides is not greater than the given diff by the absolute value.

Return the maximum sum you will get by solving the task.

Example

For redSides = [1, 1], blueSides = [2, 2] and diff = 1, the output should be
coloredCards(redSides, blueSides, diff) = 3.

Both cards have the same numbers on corresponding sides. You could get the maximum sum by lying out the cards with blue sides up, but that way the second condition wouldn't be satisfied. So, one card should be laid red side up, and the other blue side up. The answer is then 1 + 2 = 3.

For redSides = [1, 1, 2], blueSides = [2, 3, 1] and diff = 1, the output should be
coloredCards(redSides, blueSides, diff) = 7.

The solution is to lay the first and second cards blue side up, and the third red side up. The answer is 2 + 3 + 2 = 7.

Input/Output

[time limit] 4000ms (py)
[input] array.integer redSides

An array of integers, redSides[i] is the number written on the red side of the (i + 1)th card.

Constraints:
1 ≤ redSides.length ≤ 5 * 104,
1 ≤ redSides[i] ≤ 1000.

[input] array.integer blueSides

An array of integers, blueSides[i] is the number written on the blue side of the (i + 1)th card.

Constraints:
blueSides.length = redSides.length,
1 ≤ blueSides[i] ≤ 1000.

[input] integer diff

An integer, the maximal allowable difference between the number of cards with visible red and blue sides.

Constraints:
0 ≤ diff ≤ redSides.length.

[output] integer

The sum of the numbers written on the visible cards' sides laid out optimallyYou are a novice magician, and are perfecting a trick using special colored cards: each card is red on one side and blue on the other, and each side has a number on it.

As part of your magician's training you often exercise your brain with the following challenge:

For each ith (1-based) card you know the number written on its red side redSides[i - 1], and the number written on its blue side blueSides[i - 1]. The task is to lay the cards down on a table in such a way that the sum of numbers written on their visible sides is as high as possible, and the difference between the number of cards with visible red sides and those with visible blue sides is not greater than the given diff by the absolute value.

Return the maximum sum you will get by solving the task.

Example

For redSides = [1, 1], blueSides = [2, 2] and diff = 1, the output should be
coloredCards(redSides, blueSides, diff) = 3.

Both cards have the same numbers on corresponding sides. You could get the maximum sum by lying out the cards with blue sides up, but that way the second condition wouldn't be satisfied. So, one card should be laid red side up, and the other blue side up. The answer is then 1 + 2 = 3.

For redSides = [1, 1, 2], blueSides = [2, 3, 1] and diff = 1, the output should be
coloredCards(redSides, blueSides, diff) = 7.

The solution is to lay the first and second cards blue side up, and the third red side up. The answer is 2 + 3 + 2 = 7.

Input/Output

[time limit] 4000ms (py)
[input] array.integer redSides

An array of integers, redSides[i] is the number written on the red side of the (i + 1)th card.

Constraints:
1 ≤ redSides.length ≤ 5 * 104,
1 ≤ redSides[i] ≤ 1000.

[input] array.integer blueSides

An array of integers, blueSides[i] is the number written on the blue side of the (i + 1)th card.

Constraints:
blueSides.length = redSides.length,
1 ≤ blueSides[i] ≤ 1000.

[input] integer diff

An integer, the maximal allowable difference between the number of cards with visible red and blue sides.

Constraints:
0 ≤ diff ≤ redSides.length.

[output] integer

The sum of the numbers written on the visible cards' sides laid out optimally.
