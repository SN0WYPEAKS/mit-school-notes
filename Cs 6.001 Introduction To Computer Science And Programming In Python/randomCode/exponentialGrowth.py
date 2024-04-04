def growth():
    counter = 0
    print("Let's use exponential growth to show how quickly a number can grow.")
    print("A chessboard has 64 squares, so we'll use that as a test.")
    exponential = int(input("Please enter an int greater than one: "))
    temp = exponential
    if exponential > 1:
        while counter < 64:
            exponential = exponential*2
            counter += 1
            print(temp, "grew exponentially to", exponential)
            print("Counter is at:", counter)
        print("Filling a chessboard with grains of rice with exponential growth would give:", exponential)
    else:
        print("Sorry, but exponential growth only works if the number is larger than one.")