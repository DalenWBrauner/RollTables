---				---
--				 --
-  BASIC CONCEPT  -
--				 --
---				---
(these won't change)

Speech:		rolls on Speech table
Hair:		rolls on Hair table
Face:		rolls on Face table

Characteristics:
Randomly picks a file starting with C; rolls on that table

Personality:
Twice for Major trait, Twice for Minor trait,
Randomly picks a file starting with P; rolls on that table

Location:
if a trait is rolled that contains a * at the end,
rolls on Location table (and adds that to the original result)



---				---
--				 --
-  EDITING FILES  -
--				 --
---				---
Each line in the file follows these rules:
[Numbers][. ][Words][*]

[Numbers]:
This can either be a single number (1, 2, 3, 12347132, whatever)
Or it can be a range of numbers (1-2, 5-10, 7-12)
HOW NOT TO BREAK THINGS:
DO NOT use Negative Numbers
DO NOT use Fractions or Decimals
DO NOT put numbers out of order
DO NOT Reuse numbers
DO NOT make your Ranges Impossible
IF you skip a number, be aware this forces the program to re-roll.
This isn't so bad unless you have a list of traits that looks like
1. This will
10000000. Take forever

[. ]:
THERE MUST ALWAYS BE ". " INBETWEEN [NUMBER] AND [WORDS]
THERE MUST ALWAYS BE '. ' INBETWEEN [NUMBER] AND [WORDS]
THERE MUST ALWAYS BE (. ) INBETWEEN [NUMBER] AND [WORDS]
THERE MUST ALWAYS BE [. ] INBETWEEN [NUMBER] AND [WORDS]
THERE MUST ALWAYS BE {. } INBETWEEN [NUMBER] AND [WORDS]
THERE MUST ALWAYS BE <. > INBETWEEN [NUMBER] AND [WORDS]
THERE MUST ALWAYS BE |. | INBETWEEN [NUMBER] AND [WORDS]
THERE MUST ALWAYS BE  .   INBETWEEN [NUMBER] AND [WORDS]
Does that make sense? Here are some examples:

ACCEPTABLE:
1. Badass
2-70. Liked by everyone
71-78. Immune to all disease

UNACCEPTABLE:
10: Unpleasant
11--Disgusting
12 .Ugly
13..Horrendous
14  Never spoken to
15	Despised

OKAYGOODTHANKYOU.

[Words]:
You can put literally anything here.
No Rules,
Just Creativity.

[*]:
This is optional!
You can put an asterisk at the end of a line if you'd like!
When that happens, we roll on the Asterisk table,
and plug the result into the message for you.




---				---
--				 --
-  ADDING A FILE  -
--				 --
---				---
The best/safest way to do this:
	1. Copy an existing file
	2. Rename it whatever you like (keep the .txt)
	3. Make sure it does not start with a ~ (like the name of this file does)
	4. Edit its contents as much as your heart desires!
Additionally, if you'd like a certain table to be rolled more than once
WITHOUT having copies of the entire file,
Make sure your file is completely empty EXCEPT for the name of another file.
Minor 1.txt, Minor 2.txt and Major 2.txt are perfect examples of this!