## Task
You’re tasked with taking entries of personal information in multiple formats and normalizing each entry into a standard JSON format.

## Input
Your program will be fed an input file of n lines. Each line contains “entry” information, which consists of a first name, last name, phone number, color, and zip code.
The order and format of these lines vary in three separate ways. The three acceptable formats are as follows:
Lastname, Firstname, (703)-742-0996, Blue, 10013 Firstname Lastname, Red, 11237, 703 955 0373 Firstname, Lastname, 10013, 646 111 0101, Green
A line is defined as invalid if it does not comply with one of the formats shown above. Invalid lines should not interfere with the processing of subsequent valid lines. A zip code is considered valid if it has 5 digits, and no other characters. A phone number is considered valid if it has 10, and only 10, digits. A phone number may have other non-numerical characters however, as shown shown above.

##Output
The program should write a valid, formatted JSON object out to result.out. The JSON representation should be indented with two spaces. Within the JSON object should be a list named “entries”. The “entries” list should be sorted in ascending alphabetical order by (last name, first name).
Successfully processed lines should result in a normalized addition to the list associated with the “entries” key. For lines that were unable to be processed, a line number i (where 0 ≤ i < n) for each faulty line should be appended to the list associated with the “errors” key. The first line in the file is numbered 0.

## Insallation
using native packages so no need for requirements.txt

## Usage
`python parse.py data.in`

## Testing
`python test.py`

## Sample Input
```
Booker T., Washington, 87360, 373 781 7380, yellow 
Chandler, Kerri, (623)-668-9293, pink, 
123123121 
James Murphy, yellow, 83880, 018 154 6474 asdfawefawea
```
## Sample Output
```json
{
  "entries": [
    {
    "color": "yellow",
    "firstname": "James",
    "lastname": "Murphy", "phonenumber": "018-154-6474", "zipcode": "83880"
    }, {
    "color": "yellow",
    "firstname": "Booker T.", "lastname": "Washington", "phonenumber": "373-781-7380", "zipcode": "87360"
    } ],
    "errors": [ 1,
    3 ]
}
```

##TODOS
* Use threads to run segments
* More test coverage
* decorators for logging
