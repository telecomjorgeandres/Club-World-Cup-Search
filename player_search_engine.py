import operator # This special tool helps us sort things later on! It's built into Python.

# --- Step 1: Say Hello! (The Welcome Message) ---
# This is a function (a mini-program) that just prints a nice welcome message.
def print_welcome_message():
    """Prints a welcome message for the Club World Cup 2025 Player Search Engine."""
    print("-------------------------------------------------------")
    print("       Hello, Football fan! Welcome to your very own              ")
    print("       Club World Cup 2025 Player Search Engine!     ")
    print("   You can find players by their name, country, role, age, value, or team. ")
    print("-------------------------------------------------------")

# --- Step 2: Our Player Data (Our Little Database!) ---
# This is a LIST of DICTIONARIES.
# Think of the list as a big box holding all our player "cards."
# Each "card" is a dictionary, holding all the details for ONE player.
# Dictionaries use 'key: value' pairs, like 'name: "Lionel Messi"'.
PLAYER_DATA = [
    {
        "name": "Lionel Messi",
        "nationality": "Argentina",
        "position": "Forward",
        "age": 38,
        "market_value": 30000000,
        "team": "Inter Miami"
    },
    {
        "name": "Cristiano Ronaldo",
        "nationality": "Portugal",
        "position": "Forward",
        "age": 40,
        "market_value": 15000000,
        "team": "Al Nassr"
    },
    {
        "name": "Kylian Mbappe",
        "nationality": "France",
        "position": "Forward",
        "age": 26,
        "market_value": 180000000,
        "team": "Real madrid"
    },
    {
        "name": "Erling Haaland",
        "nationality": "Norway",
        "position": "Forward",
        "age": 24,
        "market_value": 170000000,
        "team": "Manchester City"
    },
    {
        "name": "Kevin De Bruyne",
        "nationality": "Belgium",
        "position": "Midfielder",
        "age": 33,
        "market_value": 60000000,
        "team": "Manchester City"
    },
    {
        "name": "Virgil van Dijk",
        "nationality": "Netherlands",
        "position": "Defender",
        "age": 33,
        "market_value": 45000000,
        "team": "Liverpool"
    },
    {
        "name": "Alisson Becker",
        "nationality": "Brazil",
        "position": "Goalkeeper",
        "age": 32,
        "market_value": 40000000,
        "team": "Liverpool"
    },
    {
        "name": "Pedri",
        "nationality": "Spain",
        "position": "Midfielder",
        "age": 22,
        "market_value": 90000000,
        "team": "FC Barcelona"
    },
    {
        "name": "Jude Bellingham",
        "nationality": "England",
        "position": "Midfielder",
        "age": 21,
        "market_value": 180000000,
        "team": "Real Madrid"
    },
    {
        "name": "Vinicius Jr.",
        "nationality": "Brazil",
        "position": "Forward",
        "age": 24,
        "market_value": 150000000,
        "team": "Real Madrid"
    },
    {
        "name": "Gavi",
        "nationality": "Spain",
        "position": "Midfielder",
        "age": 20,
        "market_value": 90000000,
        "team": "FC Barcelona"
    },
    {
        "name": "Jamal Musiala",
        "nationality": "Germany",
        "position": "Midfielder",
        "age": 21,
        "market_value": 110000000,
        "team": "Bayern Munich"
    },
    {
        "name": "Ruben Dias",
        "nationality": "Portugal",
        "position": "Defender",
        "age": 27,
        "market_value": 80000000,
        "team": "Manchester City"
    },
    {
        "name": "Franco Mastantuono",
        "nationality": "Argentina",
        "position": "Midfielder",
        "age": 17,
        "market_value": 80000000,
        "team": "Real Madrid"
    },
    # --- Adding more players to make our database bigger! ---
    # Chelsea Players
    {
        "name": "Enzo Fernandez",
        "nationality": "Argentina",
        "position": "Midfielder",
        "age": 23,
        "market_value": 80000000,
        "team": "Chelsea"
    },
    {
        "name": "Reece James",
        "nationality": "England",
        "position": "Defender",
        "age": 24,
        "market_value": 50000000,
        "team": "Chelsea"
    },
    {
        "name": "Cole Palmer",
        "nationality": "England",
        "position": "Midfielder",
        "age": 22,
        "market_value": 80000000,
        "team": "Chelsea"
    },
    # Juventus Players
    {
        "name": "Federico Chiesa",
        "nationality": "Italy",
        "position": "Forward",
        "age": 26,
        "market_value": 40000000,
        "team": "Juventus"
    },
    {
        "name": "Dusan Vlahovic",
        "nationality": "Serbia",
        "position": "Forward",
        "age": 24,
        "market_value": 65000000,
        "team": "Juventus"
    },
    {
        "name": "Manuel Locatelli",
        "nationality": "Italy",
        "position": "Midfielder",
        "age": 26,
        "market_value": 30000000,
        "team": "Juventus"
    },
    # Porto Players
    {
        "name": "Pepe",
        "nationality": "Portugal",
        "position": "Defender",
        "age": 41,
        "market_value": 1000000, # Example value, adjusted for age
        "team": "Porto"
    },
    {
        "name": "Wendell",
        "nationality": "Brazil",
        "position": "Defender",
        "age": 30,
        "market_value": 15000000,
        "team": "Porto"
    },
    {
        "name": "Mehdi Taremi",
        "nationality": "Iran",
        "position": "Forward",
        "age": 31,
        "market_value": 18000000,
        "team": "Porto"
    }
]

# --- How We Show the Players! ---
# This function takes a list of players (usually the ones found in a search)
# and prints them out nicely in a table.
def display_players(players):
    """Displays a list of player dictionaries in a formatted way."""
    if not players: # 'if not players' checks if the list is empty.
                    # If it's empty, it means we didn't find anyone!
        print("Oops! No players found matching your request. Try a different search!")
        return # 'return' means we stop this function here.

    print("\n--- Here are your search results! ---")
    # This line uses an 'f-string' (the 'f' before the quotes) to make printing
    # variables inside text super easy!
    # '{'Name':<20}' means "print 'Name', and make sure it takes up 20 spaces, aligned left."
    # This helps make our table columns look neat and tidy.
    print(f"{'Name':<20}{'Nationality':<15}{'Position':<12}{'Age':<5}{'Market Value':<15}{'Team':<20}")
    print("-" * 90) # Prints a line of 90 dashes for a nice separator.

    for player in players: # This loop goes through EACH 'player' (which is a dictionary)
                           # in the list of 'players' we received.
        # This little trick formats the market value with commas, like $30,000,000
        market_value_str = f"${player['market_value']:,}" 
        
        # Print each player's details, neatly formatted in columns.
        # 'player['name']' gets the value associated with the 'name' key for the current player.
        print(f"{player['name']:<20}{player['nationality']:<15}{player['position']:<12}{player['age']:<5}{market_value_str:<15}{player['team']:<20}")
    print("-" * 90) # Another separator line!

# --- The Main Brain of Our Program! ---
# This 'main' function is where all the action happens.
def main():
    print_welcome_message() # First, let's say hello!

    # Friendly reminder about sorting options!
    print("\nQuick Tip: After a search, you can sort your results by 'age' or 'market_value'!")

    # This is a 'while True' loop. It means this part of the code will keep
    # repeating forever, unless we tell it to 'break' (stop).
    # This lets the user do many searches without restarting the program!
    while True:
        print("\n--- What would you like to search for? ---")
        print("You can search by: name, nationality, position, age, market_value, team")
        print("Just type 'quit' if you're done searching!")

        # 'input()' waits for the user to type something and press Enter.
        # '.strip()' gets rid of any extra spaces the user might type.
        # '.lower()' turns whatever the user types into lowercase. This helps
        # make sure "Nationality" or "NATIONALITY" both work like "nationality".
        search_criteria = input("Enter your search idea (e.g., 'nationality'): ").strip().lower()

        if search_criteria == 'quit': # If the user types 'quit'...
            print("Thanks for playing with the Player Search Engine! See you next time!")
            break # ...we 'break' out of the 'while True' loop, and the program stops.
        
        # --- Checking if the search idea is valid ---
        valid_criteria = ["name", "nationality", "position", "age", "market_value", "team"]
        if search_criteria not in valid_criteria: # If the user typed something we don't understand...
            print("Hmm, that's not a valid search option. Please pick from: name, nationality, position, age, market_value, team.")
            continue # ...we skip the rest of this loop and go back to the beginning to ask again.

        # If the search idea IS valid, we ask for the specific value they want to find.
        # Clarified prompt for numerical inputs
        if search_criteria in ['age', 'market_value']:
            search_value = input(f"Okay, what number are you looking for in '{search_criteria}'? (e.g., '24' or '50000000'): ").strip()
        else:
            search_value = input(f"Okay, what value are you looking for in '{search_criteria}' (e.g., 'Brazil' or 'Forward'): ").strip()


        # --- Filtering Players (Finding the Matches!) ---
        filtered_players = [] # This is an empty list. We'll add players who match our search here.

        for player in PLAYER_DATA: # This loop goes through every single player in our big database.
            # We use 'if' and 'elif' (else if) to check which search criterion the user chose.
            if search_criteria == 'name' and search_value.lower() in player['name'].lower():
                # If searching by 'name', we check if the search value is *inside* the player's name.
                # (e.g., searching "messi" will find "Lionel Messi"). We use '.lower()' to ignore capital letters.
                filtered_players.append(player) # If it's a match, we add the whole player dictionary to our 'filtered_players' list.
            
            elif search_criteria == 'nationality' and search_value.lower() == player['nationality'].lower():
                # For 'nationality', we need an exact match.
                filtered_players.append(player)
            
            elif search_criteria == 'position' and search_value.lower() == player['position'].lower():
                # Same for 'position', an exact match (ignoring case).
                filtered_players.append(player)
            
            elif search_criteria == 'age':
                # For 'age', the user must type a number. We use 'try-except' to handle mistakes!
                try:
                    age_val = int(search_value) # Try to turn the user's text into a whole number.
                    if player['age'] == age_val: # If it's a valid number, check if the player's age matches.
                        filtered_players.append(player)
                except ValueError: # If turning to a number fails (e.g., user typed "twenty")...
                    print("Oops! For 'age', please enter a valid number. Let's try that search again!")
                    filtered_players = [] # Clear any partial results from a bad input for this criterion
                    continue # Go back to the start of the 'while True' loop to ask for a new search.
            
            elif search_criteria == 'market_value':
                # Similar to 'age', we need a number here.
                try:
                    mv_val = int(search_value)
                    # For market value, we search for players whose value is GREATER THAN OR EQUAL TO what's typed.
                    if player['market_value'] >= mv_val: 
                        filtered_players.append(player)
                except ValueError:
                    print("Oops! For 'market_value', please enter a valid number. Let's try that search again!")
                    filtered_players = []
                    continue
            
            elif search_criteria == 'team' and search_value.lower() in player['team'].lower():
                # For 'team', we check if the search value is *inside* the player's team name.
                filtered_players.append(player)

        # Now that we've checked all players, let's show the ones we found!
        display_players(filtered_players)

        # --- Step 5: Sorting Our Results! ---
        if filtered_players: # We only offer to sort if we actually found some players.
            sort_choice = input("Would you like to sort these results? (type 'yes' or 'no'): ").strip().lower()
            if sort_choice == 'yes':
                sort_by = ""
                # Keep asking until we get a valid sorting option.
                while sort_by not in ['age', 'market_value']:
                    sort_by = input("Okay! Sort by 'age' or 'market_value'? ").strip().lower()
                    if sort_by not in ['age', 'market_value']:
                        print("That's not a valid sort option. Please pick 'age' or 'market_value'.")
                
                # Now, let's decide if we want ascending (smallest first) or descending (largest first) order.
                order_choice = ""
                reverse_sort = False # Default is ascending (not reversed)
                while order_choice not in ['asc', 'desc']:
                    order_choice = input("Should it be 'asc' (smallest first) or 'desc' (largest first)? ").strip().lower()
                    if order_choice == 'desc':
                        reverse_sort = True # If 'desc', we set reverse_sort to True.
                    elif order_choice != 'asc': # If it's not 'asc' or 'desc'...
                        print("Hmm, please type 'asc' or 'desc'.")


                # This is where the 'operator' tool helps!
                # 'sorted()' is a built-in Python function that makes a new, sorted list.
                # 'key=operator.itemgetter(sort_by)' tells 'sorted()' to use the value
                # of the 'age' or 'market_value' key inside each player dictionary for sorting.
                # 'reverse=reverse_sort' uses our 'True' or 'False' to decide the order.
                sorted_players = sorted(filtered_players, key=operator.itemgetter(sort_by), reverse=reverse_sort)
                
                # Let the user know how the results are sorted.
                print(f"\n--- Here are your results, sorted by {sort_by} ({'largest first' if reverse_sort else 'smallest first'})! ---")
                display_players(sorted_players) # Show the newly sorted list!
            
        # --- Step 6: Coming Soon - Multiple Filters! ---
        # TODO: This is where we'll add the super cool feature to search using MORE THAN ONE filter!
        # TODO: E.g., "Find all 'Forwards' from 'Brazil'."

        # --- Step 7: Wrapping Up - Another Search? ---
        # After displaying results and offering sorting, let's ask if they want to do another search.
        another_search = input("\nWould you like to perform another search? (type 'yes' or 'no'): ").strip().lower()
        if another_search != 'yes':
            print("Thanks again for using the Player Search Engine! Have a great day!")
            break # Exit the main 'while True' loop if not 'yes'.

# This is the starting line for our whole program!
# It makes sure that when you run the script, the 'main()' function gets called.
if __name__ == '__main__':
    main()
