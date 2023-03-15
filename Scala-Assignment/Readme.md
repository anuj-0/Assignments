**Approach**

*Question 1:*

1. get_bucket_range function is used to find the bucket for a respective number. 
2. It gets the number behind the decimal point and checks if it is greater than equal to 50 or less than 50.
3. Accordingly it finds the bucket range for the number by finding its left and right endpoints.

*Question 2:*

1. Created a trait for player which contains all its attributes.
2. Created a case class which extends the trait, which gives the advantage of not creating an instance for the class.
3. Function get_player_info gives information about players.
4. Used Source object to read input data from the file and converted it into a list.
5. Added players as the Players object and then performed queries on it.
