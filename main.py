#1. Ask the user whether they want to enter a new country or quit.
#1.1 If they want to enter a country, ask for the country name and add it to a list of countries.
#2. Ask the user again whether they want to enter a new country, see their countries, or quit.
#2.1 If they want to see their countries, show them the contents of their #list in a nice format (i.e. don't just print the variable out!)
#3. As an optional extra, you can also ask the user for when they visited the country, as well as the country name. That'll make the app a little more useful!

countries = []


def print_countries(countries):
  if not countries:
    print("You have not entered any countries yet.")
  else:
    print("Your visited countries are:")
    for i, (country, date) in enumerate(countries, 1):
      print(f"{i}. {country}, visited on {date}")


def add_country():
  country = input("Enter the country name: ").strip()
  date = input(
      "Enter the date you visited the country (e.g., YYYY-MM-DD): ").strip()
  countries.append((country, date))


def main():
  while True:
    choice = input(
        "Do you want to enter a new country or quit? 'a' for adding a new country, 'q' for quit: "
    ).strip().lower()

    if choice == 'a':
      add_country()
    elif choice == 'q':
      print("Goodbye!")
      break
    else:
      print("Invalid input. Please choose 'a' or 'q'.")
      continue

    while True:
      user_input = input(
          "What do you want to do next? 'a' for adding a new country, 's' for showing your countries, 'q' for quit: "
      ).strip().lower()

      if user_input == 'a':
        add_country()
        break
      elif user_input == 's':
        print_countries(countries)
      elif user_input == 'q':
        print("Goodbye!")
        return  # Exit both loops and end the program
      else:
        print("Invalid input. Please choose 'a', 's', or 'q'.")


if __name__ == "__main__":
  main()
  print("Program ended!")
