from nested_loop import output

word_1 = 'abc'
word_2 = 'def'

#  identify the length of the string
# We can loop through the strings and at each iteration,
# pick one character from word1 and one character from word2 (if they exist).
# If one string is shorter, we will append the remaining characters from the longer string.
# Handle the case where one string is longer:
# After the loop finishes, there may still be some characters left in one of the strings.
# We will append them to the result.
# Finally, we return the merged string.