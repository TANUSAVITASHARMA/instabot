from pylab import *


# make a square figure and axes
def plot_pie_chart(positive,negative):
    figure(1, figsize=(6,6))
    ax = axes([0.1, 0.1, 0.8, 0.8])

    # The slices will be ordered and plotted counter-clockwise.
    labels = 'positive Comments', 'negative Comments'
    fracs = [positive, negative]
    explode=(0, 0)

    pie(fracs, explode=explode, labels=labels,
                autopct='%1.1f%%', shadow=True, startangle=90)
                # The default startangle is 0, which would start
                # the Frogs slice on the x-axis.  With startangle=90,
                # everything is rotated counter-clockwise by 90 degrees,
                # so the plotting starts on the positive y-axis.

    title('Comparison of positive and negative comments', bbox={'facecolor':'0.8', 'pad':5})
    show()