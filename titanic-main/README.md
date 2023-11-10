# Titanic

We want to fill missing values in the 'Age' column  in the 'Titanic' 
dataset with median values calculated depending on the prefix in 'Name' column:

For each title from
```
 ["Mr.", "Mrs.", "Miss."]
 ```
We need to use median value calculated for every group.
Find the number of missed values and median values corresponding to every of these 3 groups ('Mr.', 'Mrs.''Miss.'). Provide the answer in the form - a list of tuples (Title of the group, number of missed values for the group, median value calculated for the 
group). The pattern for the answer is 
```
[('Mr.', x, y), ('Mrs.', k, m), ('Miss.', l, n)]
```
where x, y, k, m, l, n, are integers, which you should calculate
The median values should be rounded to the nearest integer.

## Note:
 1. Please be carefull with dot in titles.
 2. Please don't change the function's names, input parameters
