Randomly generated passwords usually contain digits, letters and other characters placed in arbitrary order, which makes memorizing them quite difficult. In order to make your life easier you decide to normalize each randomly generated password. A normalized password consists of zero or more letters, followed by zero or more digits, followed by zero or more other characters. In this form, you treat the password as a word, followed by a number, followed by some other characters. Such a password is certainly easier to remember!

After normalization, the characters of each "class" (i.e. letters, digits or other characters) should go in the same order as they appeared in the original password. Therefore, there is a unique way to normalize any string.

Given some randomly generated password, return it in the normalized form.

Example

For password = "3A12^,^b4", the output should be
passwordNormalization(password) = "Ab3124^,^".

password contains two letters (A and b), four digits (3, 1, 2 and 4) and three other characters (^, , and another ^). Note that the characters inside each "class" are listed in the same order as they occur in password. Therefore, we only need to build three strings out of them (letters = "Ab", digits = "3124", other_characters = "^,^") and to concatenate them in the following order:
<letters><digits><other_characters>.

For password = "$#", the output should be
passwordNormalization(password) = "$#".

Input/Output

[time limit] 4000ms (py)
[input] string password

Constraints:
0 ≤ password.length ≤ 100.

[output] string
