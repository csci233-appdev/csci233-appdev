# This program displays a simple bar chart.
import matplotlib.pyplot as plt


def main():
    # not shown in text, adjust as needed for your environment
    plt.figure(figsize=(12, 12))
    plt.rcParams['font.size'] = 24

    # Create a list with the X coordinates of each bar's left edge
    left_edges = [0, 10, 20, 30, 40]

    # Create a list with the heights of each bar.
    heights = [100, 200, 300, 400, 500]

    # Build the bar chart.
    # NOTE: default alignment changed to center a while ago, need to
    # override by specifying alignment on edge to recreate text
    plt.bar(left_edges, heights, align='edge')

    # Display the bar chart.
    plt.show()


# Call the main function.
if __name__ == '__main__':
    main()
