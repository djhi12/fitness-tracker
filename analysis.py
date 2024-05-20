import matplotlib.pyplot as plt


def main():
    print("Categories:\nBack\nBiceps\nChest\nLegs\nShoulders\nTriceps\n")

    while True:  # Infinite loop until user exits
        category = input("Choose category (or 'exit' to quit): ")

        if category.lower() == "exit":
            break  # Exit the loop if user enters 'exit'

        # Read data from CSV file
        fitness_data = 'fitness-data.csv'

        with open(fitness_data) as f:
            i = 0
            for line in f:
                i += 1
                fitness_details = line.strip()
                fitness_data_clean = fitness_details.split(",")

                # Skip the header row
                if i == 1:
                    continue

                # Assigning the data from the file
                date_fitness = fitness_data_clean[0]
                exercise = fitness_data_clean[1]
                category_type = fitness_data_clean[2]
                weight = fitness_data_clean[3]
                reps = fitness_data_clean[4]
                serie_load = fitness_data_clean[5]
                week_of_year = fitness_data_clean[6]
                week = fitness_data_clean[7]

                if category_type.lower() == category.lower():
                    # Sample data
                    x_axis = ["Weight", "Reps", "Serie Load", "Week of Year"]
                    y_axis = [float(weight), int(reps), float(
                        serie_load), int(week_of_year)]

                    # Create a plot
                    plt.plot(x_axis, y_axis)

                    # Add a title
                    plt.title('Fitness Tracker')

                    # Add x and y labels
                    plt.xlabel(
                        f"Category: {category_type} | Exercise: {exercise}")
                    # plt.ylabel(f"Values on {date_fitness}")

                    # Adding grid
                    plt.plot(x_axis, y_axis, marker='o',
                             linestyle='-', color='r')
                    plt.grid(True)

                    plt.show()

        print("Success! (View another category or exit)")


main()
