import matplotlib.pyplot as plt
# import pandas as pd


def categories(category):
    pass

    return


def main():
    print("Categories:\nBack\nBiceps\nChest\nLegs\nShoulders\nTriceps\n")
    category = input("Choose category: ")
    print("\nChoose Date: Between May 13, 2022 - Aug. 13, 2022.")
    date = input("Type here: (e.g. 2022-08-13): ")

    # Read data from CSV file
    fitness_data = 'fitness-data.csv'

    with open(fitness_data) as fitness_data:
        i = 0
        for fitness in fitness_data:
            i += 1
            fitness_details = fitness.strip()
            fitness_data_clean = fitness_details.split(",")

            fitness_data_clean[0]  # Date
            fitness_data_clean[1]  # Exercise
            fitness_data_clean[2]  # Category
            fitness_data_clean[3]  # Weight
            fitness_data_clean[4]  # Reps
            fitness_data_clean[5]  # Serie Load
            fitness_data_clean[6]  # Week of Year
            fitness_data_clean[7]  # Week

            if i > 1 and fitness_data_clean[2].lower() == category.lower():

                # Sample data
                x_axis = [1, 2, 3, 4, 5]
                y_axis = [0, 100, 200, 500, 1000]

                # Create a plot
                plt.plot(x_axis, y_axis)

                # Add a title
                plt.title('Fitness Tracker')

                # # Add x and y labels
                plt.xlabel(f"Category: {fitness_data_clean[2]}")
                plt.ylabel(f"Date: {type(fitness_data_clean[0])}")

                # Adding grid
                plt.plot(x_axis, y_axis, marker='o',
                         linestyle='-', color='r')
                plt.grid(True)

                plt.show()

    print("Success!")


main()
