"""EX01 Greetings."""

greeting = input("please enter a greeting: ")        # enter greeting
recipient = input("please enter a recipient: ")      # enter recipient
repeat = int(input("How many times to repeat? "))    # enter number of repeats
welcome = (greeting + " " + recipient + "! ")        # concatenation greeting and recipient with space
print(welcome * repeat)                              # type welcome message repeat times
