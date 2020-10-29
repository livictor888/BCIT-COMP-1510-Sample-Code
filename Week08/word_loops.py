# word_loops_solution.py
#
# Some fun looping exercises for you. Implement the code!

# 1. get user input using a sentinel while loop. returns a list with each item
#    being a word, ends when <CR> is typed
#
def get_user_input():
    return []

# 2. iterate over the list, and print it out one item per line, 
#    using a for item in loop   
#
def print_using_for(w_list):
    return
    
# 3. iterate over the list, and print it out one item per line, 
#    using a for item in range loop 
#
def print_using_range(w_list):
    return

# 4. iterate over the list, and print it out one item per line, 
#    using a while loop and a list index
#
def print_using_while(w_list):
    return
    
# 5. iterate over the list, and print it out one item per line in reverse order,
#    using a while loop and a list index
#
def print_in_reverse(w_list):
    return
    
# 6. iterate over the list, return the length of the longest word in the list, 
#    using a for item in loop
def long_word(w_list):
    return 0

# 7. iterate over the list, return the minimum word length in the list, 
#    using a while loop and a list index
#
def short_word(w_list):
    return 0

# 8. iterate over the list, return the average word length, 
#    using a for loop with a range
#
def avg_word_length(w_list):
    return 0

# 9. iterate over the list, create and return a new list that only contains 
#    the unique words from the original list
#
def unique_words(w_list):
    return []

# 10. iterate over the list, create and return a dictionary that has a count of 
#     the number of times each word occurs in the list
def word_counts(w_list):
    return {}  

# This is the main routine, which just tests that out Functions work. The tests
# are all written.
#
def tests():

    a_list = get_user_input()
    print("Test 1: a_list=", a_list)

    print("\nTest 2: print_using_for...")    
    print_using_for(a_list)
    
    print("\nTest 3: print_using_range...")
    print_using_range(a_list)

    print("\nTest 4: print_using_while...")
    print_using_while(a_list)
    
    print("\nTest 5: print_in_reverse...")
    print_in_reverse(a_list)

    lng = long_word(a_list)
    print("\nTest 6: longest word has %i chars" % lng)

    sht = short_word(a_list)
    print("\nTest 7: shortest word has %i chars" % sht)

    avg = avg_word_length(a_list)
    print("\nTest 8: avg word length is %.1f" % avg)

    ul = unique_words(a_list)
    print("\nTest 9: unique_list =", ul)

    wc = word_counts(a_list)
    print("\nTest 10: word_counts =", wc)

tests()