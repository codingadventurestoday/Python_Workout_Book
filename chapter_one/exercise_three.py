""""""

def running_time():
    """Takes in how long it took for you to run 10k in minutes
    until user presses <enter>, then returns an average time ran"""
    get_input = True
    running_times = 0
    amount_of_runs = 0
    
    while get_input:
        new_entry = input("How long did it take to complete your 10k run? ")
        if new_entry == "":
            get_input = False
            break

        try:
            duration_ran = float(new_entry)
            running_times += duration_ran
            amount_of_runs += 1
    
        except ValueError:
            print("The information you entered was not a number")

    avg_10k_time = running_times / amount_of_runs
    return f"You have ran an average time of {avg_10k_time: .2f} in {amount_of_runs} runs"

print(running_time())