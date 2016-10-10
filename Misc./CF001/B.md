As a member of the Security and Encryption team, you're designing an encrypted calendar feature. The main requirement of the feature is to keep secret any date assigned to an appointment (here, date means the day of the month, i.e. a single integer). You use the following approach for the encryption:

Convert the date to a Roman numeral.
Reverse the order of the digits in the number obtained on the previous step.
If the result of the previous step represents a correct Roman numeral, convert it back into an Arabic numeral. Otherwise, the algorithm fails, i.e. the date cannot be encrypted (therefore, you don't use such a date for secret appointments).
The result of the previous step is the answer.
Given the day of the month, return it in the encrypted format, or -1 if the above-described algorithm fails to encrypt it.

Example

For date = 6, the output should be
dateEncryption(date) = 4.

In the Roman numeral system, VI stands for 6. After reversing the order of the digits, we obtain IV. This value is a correct Roman numeral that corresponds to 4.

For date = 7, the output should be
dateEncryption(date) = -1.

In the Roman numeral system, VII stands for 7. After reversing the order of the digits, we obtain IIV. This value doesn't represent a correct Roman numeral.

Input/Output

[time limit] 4000ms (py)
[input] integer date

Constraints:
1 ≤ date ≤ 31.

[output] integer
