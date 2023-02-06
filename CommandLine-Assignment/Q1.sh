#!/bin/bash

#Current Date
curr_date=$(date +"Year: %Y, Month: %m, Day: %d") 

#Current Time
curr_time=$(date +"%T")

#Current User
curr_user=$(whoami) 

#Home Directory
home_directory=$(echo $HOME) 

#Working Directory
current_directory=$(pwd) 

# Printing the fetched variables
echo "Current date is: $curr_date"
echo "Current time is: $curr_time"
echo "Current User is: $curr_user"
echo "Home directory is located at: $home_directory"
echo "Current Working directory is located at: $current_directory"

exit 0