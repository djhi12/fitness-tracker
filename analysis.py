import matplotlib.pyplot as plt  # Importing the Matplotlib library for plotting
import itertools  # Importing itertools to create an iterator for cycling through colors
import os  # Importing os to interact with the operating system


def read_fitness_data(filename):
    """
    Read fitness data from a CSV file.

    Args:
    - filename: Name of the CSV file

    Returns:
    - List of tuples containing fitness data
    """
    fitness_data = []
    with open(filename) as f:
        next(f)  # Skip header row
        for line in f:
            # Append each line as a tuple after stripping whitespace and splitting by comma
            fitness_data.append(tuple(line.strip().split(",")))
    return fitness_data


def plot_fitness_data(category, fitness_data):
    """
    Plot fitness data for a specific category.

    Args:
    - category: Category to plot
    - fitness_data: List of tuples containing fitness data
    """
    # Define a cycle of colors to use for the plots
    colors = itertools.cycle(['r', 'g', 'b', 'c', 'm', 'y', 'k'])
    found = False  # Flag to check if any data is found for the category

    for data in fitness_data:
        # Unpack the tuple into individual variables
        date_fitness, exercise, category_type, weight, reps, serie_load, week_of_year, week = data

        # Check if the current data's category matches the specified category
        if category_type.lower() == category.lower():
            found = True
            color = next(colors)  # Get the next color from the cycle

            # Prepare data for the plot
            x_axis = ["Weight", "Reps", "Serie Load", "Week of Year"]
            y_axis = [float(weight), int(reps), float(
                serie_load), int(week_of_year)]

            # Create a plot with markers and solid lines
            plt.plot(x_axis, y_axis, marker='o', linestyle='-', color=color)

            # Add a title to the plot
            plt.title('Fitness Tracker')

            # Label the x and y axes
            plt.xlabel(f"Category: {category_type} | Exercise: {exercise}")
            plt.ylabel(f"Values on {date_fitness}")

            # Add a grid to the plot
            plt.grid(True)

            # Display the plot
            plt.show()

    if not found:
        # If no data was found for the category, print a message
        print(f"No data found for the category: {category}.")


def main():
    # Print a welcome message and available categories
    print("Welcome to Fitness Tracker!\n")
    print("Categories:\nBack\nBiceps\nChest\nLegs\nShoulders\nTriceps\n")

    # Read data from CSV file
    fitness_data_file = 'fitness-data.csv'
    if not os.path.exists(fitness_data_file):
        # If the file does not exist, print an error message and exit
        print(f"Error: File '{fitness_data_file}' not found.")
        return

    # Read the fitness data from the file
    fitness_data = read_fitness_data(fitness_data_file)

    while True:  # Infinite loop until user exits
        # Prompt the user to choose a category or exit
        category = input("Choose category (or 'exit' to quit): ")

        if category.lower() == "exit":
            break  # Exit the loop if user enters 'exit'

        # Plot the fitness data for the chosen category
        plot_fitness_data(category, fitness_data)

    # Print a goodbye message upon exiting
    print("Exiting Fitness Tracker. Goodbye!")


if __name__ == "__main__":
    # Run the main function if this script is executed
    main()
