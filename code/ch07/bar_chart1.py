# This program displays a simple bar chart.
import matplotlib.pyplot as plt


def main():
    # not shown in text, adjust as needed for your environment
    plt.figure(figsize=(12, 12))
    plt.rcParams['font.size'] = 24

    # Create a list with the X coordinates of each bar's center.
    # NOTE: behavior has changed from when text was made?
    # these are the locations of center of the bars that are drawn
    centers = [0, 10, 20, 30, 40]

    # Create a list with the heights of each bar.
    heights = [100, 200, 300, 400, 500]

    # Build the bar chart.
    plt.bar(centers, heights)

    # Display the bar chart.
    plt.show()


# Call the main function.
if __name__ == '__main__':
    main()
