# This program displays a sales chart.
import matplotlib.pyplot as plt


def main():
    # not shown in text, adjust as needed for your environment
    plt.figure(figsize=(12, 12))
    plt.rcParams['font.size'] = 24

    # Create a list with the X coordinates of each bar's left edge
    left_edges = [0, 10, 20, 30, 40]

    # Create a list with the heights of each bar.
    heights = [100, 200, 300, 400, 500]

    # Create a variable for the bar width.
    bar_width = 10

    # Build the bar chart.
    # NOTE: need to add in edge color to reproduce figure in text
    # NOTE: alignment needs to be changed to reproduce text
    plt.bar(left_edges, heights, bar_width, color=('r', 'g', 'b', 'w', 'k'),
            edgecolor='black', linewidth=3, align='edge')

    # Add a title.
    plt.title('Sales by Year')

    # Add labels to the axes.
    plt.xlabel('Year')
    plt.ylabel('Sales')

    # Customize the tick marks.
    plt.xticks([5, 15, 25, 35, 45],
               ['2016', '2017', '2018', '2019', '2020'])
    plt.yticks([0, 100, 200, 300, 400, 500],
               ['$0m', '$1m', '$2m', '$3m', '$4m', '$5m'])

    # limit x range to reproduce figure in text
    plt.xlim([0, 50])

    # Display the bar chart.
    plt.show()


# Call the main function.
if __name__ == '__main__':
    main()
