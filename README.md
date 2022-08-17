# PyPoll with Python
Election analysis using VS Code and Python.

## Overview of Election Audit
### Purpose
There are two main reasons we are doing this election analysis: to become more familiar with the programs and software we will be using, and to provide results for the US Congressional precinct in Colorado about their recent election. The coding language we will become familiar with in this analysis is Python. Python is extremely useful in many fields like finance, medical, weather and even social media. So, it is no surprise that we will be using it for election data. We will also be using VS Code since it helps to write, execute, edit, and save scripts. We are mainly using VS Code since we need to save the scripts we write, and because it is more user friendly. With VS Code we were asked to print results in the output terminal window, as well as saving those results to a text file. We are assisting a Colorado Board of Elections employee named Tom and his manager Seth. In the initial parts of this analysis, we already used code to report: the total number of votes cast, the total number of votes for each candidate, the percentage of votes for each candidate, and the winner of the election based on the popular vote. We automated this on Python so that it can be used to audit other congressional districts, senatorial districts, and even local elections. In the challenge part of this module, we are asked to include additional information from what we have already done as previously mentioned. The election commission requested us to report: the voter turnout for each county, the percentage of votes from each county out of the total count, and the county with the highest turnout. Along with getting these values, we will make sure they print in the output terminal and that they are written to the text file. 

## Election-Audit Results
I will mention here, that for any of this data to even be accessed, we needed to use Python dependencies to be able to read the CSV file that has our data. We used the `import` function to bring in the `CSV` dependencies along with `OS` dependencies to mark the path to our files. Once we have imported the dependencies and have given the path to the file locations, we can open the CSV file and obtain the data within to now manipulate.

- How many votes were cast in this congressional election?
The number of votes casted in this election can also be referred to as the total amount of votes. In this script, we labeled this as the variable `total_votes`. We obtained a value of 369,711 votes! To obtain this value, we set the variable equal to 0 so that we start counting from 0 obviously. 
```
total_votes = 0
```
Then by using for loops, we were able to run through every row and add 1 to the 'total_votes' variable with this code:
'''total_votes = total_votes + 1'''
Using the ‘Print’ function we could now display this value in the output terminal:
'''election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n\n"
        f"County Votes:\n")
    print(election_results, end="")'''
To make it easier to read, we used f strings to add text that makes it clear what the value represents, along with line breaks to separate text. We created a new variable to hold all the code for the f strings and then used the 'print' function on that new variable 'election_results'. Finally, we added this data to the text file by using the 'write' function as follows:
'''txt_file.write(election_results)'''
This same method of using the 'print' and 'write' function was used for the other data obtained in the rest of this analysis, so we will not be repeating in detail the steps and the code. The code we wrote is going to run through every row and add 1 to the total vote count until it reaches the end. We can verify this by opening the CSV file with Excel. If we use **Command + down** on one of the columns with data, it will take us to the last row of data which is row number 369,712. The first row of the data has headers which is not counted in the code we used. Therefore 369,712 – 1 = 369,711 which is our total vote count.
![Insert image][last_row_csv.png]()
![insert image][total_votes.png]()

*Provide a breakdown of the number of votes and the percentage of total votes for each.
There were three counties in this precinct which are Jefferson, Denver, and Arapahoe. Arapahoe has the smallest number of votes (24,801) which will equate to the smaller percentage of the total number of votes (6.7%). Jefferson comes next with 38,855 votes which equates to only 10.5% of the total number of votes. This leaves us with Denver having 306,055 votes which as you can see is more than half, 82.8% specifically, of the total number of votes. 
    To get these values, we need to create a list for the county names, and then a dictionary which can store key value pairs. 
'''county_list = []
county_votes = {}'''
Using this code, we created an empty list and dictionary, respectively, to store the data we will code for later in the script. For the list which we labeled as ‘county_list’, we were able to add the names of the counties into the list by going through each row and extracting the data from column 2 or index [1] since the index starts at [0]. 
'''county_name = row[1]'''
This alone will just give all the county names but repeated. To only give the names of the counties without repeating, we will use an if statement: 
'''if county_name not in county_list:
county_list.append(county_name)'''
The code above tells the program to add the county name to the list (append) if the county name is not already in the list (not in). Now that we have the county names, we can start getting the numerical data. 
'''county_votes[county_name] = 0
county_votes[county_name] += 1'''
The code above will set the vote count, per county to 0 and then add 1 to the vote count every time the county name appears. This will give us the total number of votes each county contributed with. Now it gets more detailed:
'''for county_name in county_votes:
cvotes = county_votes.get(county_name)
cvote_percentage = float(cvotes) / float(total_votes) * 100
    county_results = (f"{county_name}: {cvote_percentage:.1f}% ({cvotes:,})\n")'''
To get the percentage of a counties votes to the total vote, we want to access the data in the dictionary we created (county_votes). This dictionary now has the key (counties) and the values (vote count per county). Using the ‘get’ function, we can retrieve the vote count and assign it as the variable ‘cvotes’. Now we can find the vote percentage (cvote_percentage). We need to turn the string data into floating point decimal numbers by using the ‘float’ function. Next, divide the county votes (cvotes) by the total votes (total_votes) and then multiply that by 100 to receive a percentage. Following the steps previously mentioned, we can print the information to the output terminal, and write the data to the text file. 
![insert image][county_votes_percentage.png]()

*Which county had the largest number of votes?
The county with the largest number of votes was Denver. This county had more than 50% of the votes for this election. We defined three variables to help with this code. 
'''largest_county_turnout = ""
largest_turnout_votes = 0
county_winning_percentage = 0'''
In order, this will represent the county with the largest votes (largest_county_turnout) as a string (name), that counties number of votes (largest_turnout_votes), and the percentage of those votes to the total votes (county_winning_percentage). 
'''if (cvotes > largest_turnout_votes) and (cvote_percentage > county_winning_percentage):
largest_turnout_votes = cvotes
largest_county_turnout = county_name
county_winning_percentage = cvote_percentage '''
This if statement will do the following: If the county vote number (cvotes) that was calculated is greater than the largest counties vote count (largest_turnout_votes), and if the counties vote percentage (cvote_percentage) that was calculated is greater than the county with the highest percentage (county_winning_percentage), then we set those values equal to their variables as shown below the if statement. Since they are originally set to 0 it will fill in Denver’s calculated values which are the largest values. Finally, we can display the county name with the highest vote count by setting that variable (county_name) equal to ‘largest_county_turnout’ as string data. For the printing and writing part in this section, we were asked only to display the name of the winning county (Denver). 
![insert image][largest_county_turnout.png]()

*Provide a breakdown of the number of votes and the percentage of the total votes each candidate received.
In the module work before the challenge, we had used code very similar to the last sections we discussed in this report. In fact, all the code I broke down above in this results section was originally mirrored from the data I obtained in the following sections. What I’m basically saying is we calculated the candidate results first and then re used the code while making modifications, to get the county results. Since the code is basically the same as I described it above, I will be brief with the information here. We had three candidates running and each had their own vote count. This can be used to calculate the percentage of votes from the total votes very much in the same way we did for the counties. We created a list and dictionary, created loops to go through the data and add the candidate names, their vote count and then calculate their vote percentage from the total votes. 
‘’’candidate_options = []
candidate_votes = {}’’’
Creating the list and dictionary for the candidates and their vote count.
‘’’candidate_name = row[2]’’’
Getting the names from column 3 or index[2].
‘’’if candidate_name not in candidate_options:
candidate_options.append(candidate_name)
candidate_votes[candidate_name] = 0
candidate_votes[candidate_name] += 1’’’
This will add the candidate name to the list making sure it doesn’t repeat and also to start the vote counter for that candidate.
‘’’for candidate_name in candidate_votes:
votes = candidate_votes.get(candidate_name)
       vote_percentage = float(votes) / float(total_votes) * 100
       candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
print(candidate_results)
txt_file.write(candidate_results)’’’
This block of code will retrieve the vote count and percentage for each candidate, then print it on the output terminal along with writing it into the text file. The results are: Charles Casper Stockham with 85,213 votes which comes out to 23% of the total votes. Raymon Anthony Doane with 11,606 votes which comes out to 3.1% of the total votes. And finally, Diana DeGette with a massive 272,892 votes which takes up 73.8% of the total votes.
![insert image][candidate_vote_percentage.png]()

*which candidate won the election, what was their vote count, and what was their percentage of the total votes?
Just by the results we obtained in the last section of this report, we can see that Diana DeGette won the election with 272,892 votes! This is more than half of the votes, more specifically 73.8%. We obtained these results and displayed it just like we did with the largest county turnout. Besides switching the variables, we mainly changed the print statement to have not only the name of the winning candidate, but their stats in the same section of the text file: 
'''winning_candidate_summary = (
f"-------------------------\n"
f"Winner: {winning_candidate}\n"
f"Winning Vote Count: {winning_count:,}\n"
f"Winning Percentage: {winning_percentage:.1f}%\n"
f"-------------------------\n")
print(winning_candidate_summary)'''
Which will produce:
![insert image][ winning_candidate.png]()

## Election-Audit Summary
Creating this script originally to obtain these results can be extremely tedious and could take up more time than doing it on excel alone. Which one is faster is debatable on the amount of data given and how diverse the data is. But nevertheless, this script is more useful than what could be provided with excel since we can use this exact same script with some modifications, to analyze other elections like the ones we mentioned in the overview.
For any election looking for the same results (candidate names, county names, vote count, etc.), this script can be modified very easily to produce the same results. So, this could be another precinct election for Colorado or even another state. If the data we are provided comes as a CSV file, we just need to modify the loading and saving path presented here:
‘’’file_to_load = os.path.join("resources", "election_results.csv")
file_to_save = os.path.join("analysis", "election_analysis.txt")’’’
We would just need to change the file path to whatever folder the CSV file is located and then the name of the CSV file. Then we need to adjust the name of the text file where we save the information we obtain and whatever folder it is located. If the CSV file is presented in the same format with the same type of data, this is the only change necessary to be made to the script. Even If we are given different and multiple county names, candidate names, and insanely more or less ballots, we can still get the total vote count, all the candidate names, all the county names, and the calculations we did for each. 
In another type of election, we could be presented with different data but in the same format as the CSV file. For example, we could be given different political parties to replace the county column of the state or even added as a new column. If we are replacing the county column with the type of political party, the modifications are very simple. to start, the same modification above will have to take place for any new CSV file (making sure the right CSV file is opened and the right text file is being saved to). The main things to change for this scenario would be replacing the variables we use like changing 'county_list' to 'party_list', 'county_votes' to 'political_votes', and so on to match the column we are looking at. If we are replacing the original column, we do not even have to change the index when specifying party_name variable. 
In the second scenario of adding a completely new column with the political party, we would require a bit more work. Let’s say we want to see the current information, county and candidate results, but also want to see political party results. We could copy and paste the old code used for either county or candidate results, and then replace the variable names, and change the index. A very simple solution. Without placing too many lines of code here, I will use one block as an example:
‘’’for row in reader:
        total_votes = total_votes + 1
        candidate_name = row[2]
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            candidate_votes[candidate_name] = 0
        candidate_votes[candidate_name] += 1’’’
This is the original block of code to go through the rows of data, count the number of rows while adding to the total vote count (which will produce the total votes). We then are going to loop over the column 3 (index [2]) which is the candidate’s name, and using an if statement, add the candidate’s name in the candidate list if it hasn’t already been added as we go through the rows. Then we will add a vote to each name as we go down the row if it belongs to that candidate. 
Similarly, we can change this to political party to get the same results (adding the political party name, and the votes that the party had) by changing the variables.
‘’’for row in reader:
        total_votes = total_votes + 1
        party_name = row[3]
        if party_name not in party_options:
            party_options.append(party_name)
            party_votes[party_name] = 0
        party_votes[party_name] += 1’’’
By just defining new variables and replacing them, we will obtain the party name in a list without repeats, and the votes that party gathered. This can be mirrored for any data that is presented: county name, candidate name, state, president, political party, etc.
