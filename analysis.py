import matplotlib.pyplot as plt
import itertools
import os


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
            fitness_data.append(tuple(line.strip().split(",")))
    return fitness_data


def plot_fitness_data(category, fitness_data):
    """
    Plot fitness data for a specific category.

    Args:
    - category: Category to plot
    - fitness_data: List of tuples containing fitness data
    """
    colors = itertools.cycle(['r', 'g', 'b', 'c', 'm', 'y', 'k'])
    found = False

    for data in fitness_data:
        date_fitness, exercise, category_type, weight, reps, serie_load, week_of_year, week = data

        if category_type.lower() == category.lower():
            found = True
            color = next(colors)  # Get the next color

            # Sample data
            x_axis = ["Weight", "Reps", "Serie Load", "Week of Year"]
            y_axis = [float(weight), int(reps), float(
                serie_load), int(week_of_year)]

            # Create a plot
            plt.plot(x_axis, y_axis, marker='o', linestyle='-', color=color)

            # Add a title
            plt.title('Fitness Tracker')

            # Add x and y labels
            plt.xlabel(f"Category: {category_type} | Exercise: {exercise}")
            plt.ylabel(f"Values on {date_fitness}")

            # Adding grid
            plt.grid(True)

            plt.show()

    if not found:
        print(f"No data found for the category: {category}.")


def main():
    print("Welcome to Fitness Tracker!\n")
    print("Categories:\nBack\nBiceps\nChest\nLegs\nShoulders\nTriceps\n")

    # Read data from CSV file
    fitness_data_file = 'fitness-data.csv'
    if not os.path.exists(fitness_data_file):
        print(f"Error: File '{fitness_data_file}' not found.")
        return

    fitness_data = read_fitness_data(fitness_data_file)

    while True:  # Infinite loop until user exits
        category = input("Choose category (or 'exit' to quit): ")

        if category.lower() == "exit":
            break  # Exit the loop if user enters 'exit'

        plot_fitness_data(category, fitness_data)

    print("Exiting Fitness Tracker. Goodbye!")


if __name__ == "__main__":
    main()
