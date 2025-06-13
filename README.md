# Club World Cup 2025 Player Search Engine

## Overview
This is a simple console-based search engine built in Python to help you find players participating in the Club World Cup 2025. You can search for players by various criteria and even sort the results!

## Features
* Search players by Name, Nationality, Position, Age, Market Value, and Team.
* User-friendly prompts and error handling for input.
* Ability to sort search results by Age or Market Value (ascending/descending).

## How to Use
1.  **Save the file:** Save the `player_search_engine.py` file to your computer.
2.  **Run the script:** Open your terminal or command prompt, navigate to the directory where you saved the file, and run it using `python player_search_engine.py`.
3.  **Follow the prompts:** The program will guide you to enter search criteria (e.g., `nationality`, `team`).
4.  **Sort results:** After a search, you'll be asked if you want to sort the displayed players.
5.  **Quit:** Type `quit` to exit the program.

## Example Search

--- What would you like to search for? ---
You can search by: name, nationality, position, age, market_value, team
Just type 'quit' if you're done searching!
Enter your search idea (e.g., 'nationality'): team
Okay, what value are you looking for in 'team' (e.g., 'Brazil' or 'Forward'): Real Madrid

--- Here are your search results! --- Name Nationality Position Age Market Value Team
Jude Bellingham England Midfielder 21 $180,000,000 Real Madrid Vinicius Jr. Brazil Forward 24 $150,000,000 Real Madrid Franco Mastantuono Argentina Midfielder 17 $80,000,000 Real Madrid
Would you like to sort these results? (type 'yes' or 'no'): yes
Okay! Sort by 'age' or 'market_value'? age
Should it be 'asc' (smallest first) or 'desc' (largest first)? asc

--- Here are your results, sorted by age (smallest first)! --- Name Nationality Position Age Market Value Team
Franco Mastantuono Argentina Midfielder 17 $80,000,000 Real Madrid Jude Bellingham England Midfielder 21 $180,000,000 Real Madrid Vinicius Jr. Brazil Forward 24 $150,000,000 Real Madrid

Would you like to perform another search? (type 'yes' or 'no'): no

Thanks again for using the Player Search Engine! Have a great day!

## Technologies Used
* Python 3
