# CISC367-Windows
Research Project Repository for CISC367, University of Delaware

Windows_help_function.py
#In this script, we make all help functions that we need to help us get the result

get_conv_num(a_csv):
Attribute: A csv file
Make a empty list first, then import a csv file, search through the whole csv file, if the message include "http", we will append the ID of this message into the list that we made before.
After researching whole file, this function will return the list of the conversation ID that include the http's message.

get_conv(a_conv_number,a_csv):
Attribute: A interger which is the convesartion ID and a csv file
Make a empty list first, then use for loop to check through the whole csv file to find the same conversation ID's conversation message, append the name/message into the list. Put the list into Dataframe and use pandas to tranfer it to csv file.

get_new_frame(id, a_csv):
Attribute: A interger which is the convesartion ID and a csv file
Make a empty list first, then use for loop to find which line includes the http message and put the next line(Always the reply to the url) into the list, then use pandas to transfer it into csv file

sentimental(a_csv):
Attribute: A csv file
Import the csv file which includes all reply in one conversation that has the http message, put all reply into a list. Then use NLTK sentimental function which could recognize the emotion of the reply. Then we can get three floats: positive points negative points and neu points, compare three floats to find the biggest one which be the result to return from this function


Windows_py.py
#In this script, use all help function to calculate through whole conversations that include the http message

First we use get_conv_num function to get the list of conversation IDs 
Then we use for loop to get each id of the list, put the id as attribute into get_conv function to get a csv file and use get_new_frame to get the reply as a csv file. at last we use sentimental to get the result and put the result with thier id as a csv to output.
During the process we count the number of each data and calculate the percentage of each data.
