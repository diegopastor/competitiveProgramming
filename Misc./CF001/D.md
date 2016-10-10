Your army has been unsuccessfully laying siege to an enemy's castle for the past month. Luckily, your R&D team has developed a technology that can teleport a soldier inside the castle to a specific point (x, y). Then, once the soldier finds himself within the castle walls, he'll sneak to the gates and open them, letting your army in to crush the enemy forces easily.

You also got your hands on a plan of the castle that look something like this: to start with, consider a square with sides parallel to the axes, center at (0, 0) and side length equal to wallLength. Now draw pairs of circles with radii r1 and r2, centered at each of the square's corners. Parts of the plan between the circles (including both circumferences) belong to the castle wall, whereas points strictly inside the smallest circle correspond to the tower. Now consider four segments (parts of the square sides lying outside the circles) which join the circles. Extend each of these segments to wallWidth in such a way that the former narrow segment becomes the central axis of the wide "segment". These wide "segments" also correspond to walls.

Before teleporting your soldier you'd like to ensure that he'll end up inside the castle or, at the very least on its walls. Given the castle dimensions described above and teleportation coordinates, return the string matching the location of the point, using one of the following descriptors: "Outside the castle", "Inside the castle", "On the walls", "On the tower".

Example

For castle = [10, 2, 3, 4] and destination = [-5, 5], the output should be
castleInvasion(castle, destination) = "On the tower";

For castle = [10, 2, 3, 4] and destination = [6, 0], the output should be
castleInvasion(castle, destination) = "On the walls";

For castle = [10, 2, 3, 4] and destination = [0, 7], the output should be
castleInvasion(castle, destination) = "Outside the castle";

For castle = [10, 2, 3, 4] and destination = [3, 0], the output should be
castleInvasion(castle, destination) = "Inside the castle".

Input/Output

[time limit] 4000ms (py)
[input] array.integer castle

Description of the castle given in the following format: [wallLength, wallWidth, r1, r2].

Constraints:
7 ≤ wallLength ≤ 109,
1 ≤ wallWidth ≤ r1,
1 ≤ r1 < r2 < wallLength / 2.

[input] array.integer destination

Teleport destination point in the format [x, y].

Constraints:
-109 ≤ x, y ≤ 109.

[output] string

One of the following strings: "Outside the castle", "Inside the castle", "On the walls", "On the tower" (depending on the location of the point).
