open file

create variables - totalVotes int, candidateList = {candidate: votes}

open CSV for read

for each row
total votes = totalVotes +1
if cadidateList.index(current row candidate) <1 
	then append dict to list and set votes = 0

increase vote for candidate + 1

exit for loop

create temp variables

for candidate in list
	find one with most votes ( accumulator? )
	calc and print percentage

print outPut
	
