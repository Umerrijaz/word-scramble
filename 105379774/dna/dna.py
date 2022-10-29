import csv
import sys


def main():

    # TODO: Check for command-line usage
    if len(sys.argv) != 3:
        print(len(sys.argv))
        sys.exit("Usage:python dna.py data.csv sequence.txt")

    # TODO: Read database file into a variable
    database = []
    with open(sys.argv[1]) as file:
        reader = csv.DictReader(file)
        for row in reader:
            database.append(row)


    # TODO: Read DNA sequence file into a variable
    with open(sys.argv[2]) as file:
        sequence = file.read()


    # TODO: Find longest match of each STR in DNA sequence
    # Create a list of STR by accessing the keys [1:]-> ignoring the name column
    STR = list(database[0].keys())[1:]
    # Create a dicitonary
    STR_match = {}
    # Loop through the total length of STR keys in the dictionary
    for i in range(len(STR)):
        # Access the dictionary and the STR that is created at i location is equal to the longest match
        STR_match[STR[i]] = longest_match(sequence, STR[i])


    # TODO: Check database for matching profiles
    # Loop through the length of the entire database
    # First access the list
    count = 0
    # Loop every dictionary in the list
    for i in range(len(database)):
        # Loop the length of keys in the dictionary, for example 'AGATC'+'AATC'+'TATC' = 3
        for j in range(len(STR)):
            # If the STR at j location = STR at i location in the database, then enter the if condition
            if int(STR_match[STR[j]]) == int(database[i][STR[j]]):
                count += 1
        if count == len(STR):
            print(database[i]["name"])
            return
    print("No Match")
    return



def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""

    # Initialize variables
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    # Check each character in sequence for most consecutive runs of subsequence
    for i in range(sequence_length):

        # Initialize count of consecutive runs
        count = 0

        # Check for a subsequence match in a "substring" (a subset of characters) within sequence
        # If a match, move substring to next potential match in sequence
        # Continue moving substring and checking for matches until out of consecutive matches
        while True:

            # Adjust substring start and end
            start = i + count * subsequence_length
            end = start + subsequence_length

            # If there is a match in the substring
            if sequence[start:end] == subsequence:
                count += 1

            # If there is no match in the substring
            else:
                break

        # Update most consecutive matches found
        longest_run = max(longest_run, count)

    # After checking for runs at each character in seqeuence, return longest run found
    return longest_run

main()