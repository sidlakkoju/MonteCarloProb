import randomValueGen
# Store call duration for each trial
wValues = []

# Run simulation for 1000 trials
for i in range(TRIAL_COUNT):
    time = 0
    call_count = 0

    # Run simulation
    while (call_count < 4):

        # Time for dialing your phone number
        time += 6
        prob = randomValueGen.randNumStart(i+1)

        # Busy Line 
        if prob < 0.2:
            time += 3
        
        # Unavailable Customer
        elif prob < 0.5:
            time += 25
        
        # Customer picks up
        else:
            x = float(np.random.exponential(12, 1))
            if x >= 25:
                time += 25
            
            # They Pick up call so end simulation
            else:
                time += x
                break
        
        call_count += 1
        time += 1   # Time to End Call
    wValues.append(time)