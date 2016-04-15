import random

# Play with different concentrations
for concentration in [0.0, 0.5, 1.0]:

    # First customer always sits at the first table
    # To do otherwise would be insanity
    tables = [1]

    # n=1 is the first customer 
    for n in range(2,5000):

        # Gen random number 0~1
        rand = random.random()

        p_total = 0
        existing_table = False

        for index, count in enumerate(tables):

            prob = count / (n + concentration)

            p_total += prob
            if rand < p_total:
                tables[index] += 1
                existing_table = True
                break

        # New table!!
        if not existing_table:
             tables.append(1)

    for index, count in enumerate(tables):
        print index, "X"*(count/100), count
    print "----"
