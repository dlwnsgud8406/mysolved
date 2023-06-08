def calculate_eit(infection_date, strike_date):
    # Calculate the number of years and months between infection and strike dates
    years = strike_date[1] - infection_date[1]
    months = strike_date[0] - infection_date[0]

    # Calculate the EIT based on the rules
    if years == 0:
        eit = (0.5 / 12) * (12 - infection_date[0] + 1)
    else:
        eit = 0.5 + (years - 1) + (12 - infection_date[0] + 1) / 12

    return round(eit, 4)


# Read the number of zones
n = int(input())

# Process each zone
for _ in range(n):
    # Read the infection and strike dates
    infection_date = list(map(int, input().split()))
    strike_date = list(map(int, input().split()))

    # Calculate the EIT and print the result
    eit = calculate_eit(infection_date, strike_date)
    print('{:.4f}'.format(eit))
