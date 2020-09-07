import turtle
#
# with open("labdata.txt", "r") as lb:
#     lab_data = []
#     for line in lb:
#         line = line.split()  # to deal with blank
#         if line:  # lines (ie skip them)
#             line = [int(i) for i in line]
#             lab_data.append(line)
#     print(lab_data)


def plotregression(data):

    # getting the formula_elements from the data
    all_x, all_y = [i[0] for i in plot_data], [i[1] for i in plot_data]
    all_x, all_y = [float(i) for i in all_x], [float(i) for i in all_y]
    n = len(all_x)
    XY = [all_x[i] * all_y[i] for i in range(n)]
    X_square = [all_x[i]**2 for i in range(n)]
    sumX, sumY = sum(all_x), sum(all_y)
    X_bar, Y_bar = sumX/n, sumY/n
    sumXY = sum(XY)
    sumX_square = sum(X_square)

    m = (sumXY - n * X_bar * Y_bar) / (sumX_square - n * X_bar ** 2)
    best_y = [Y_bar + m*(all_x[i] - X_bar) for i in range(len(all_x))]

    max_x = max(all_x)
    max_y = max(all_y)
    alex = turtle.Turtle()
    alex.shape("triangle")
    y_plot = turtle.Turtle()
    wn = turtle.Screen()
    wn.setworldcoordinates(0, 0, max_x, max_y)
    for i in range(n):
        alex.penup()
        alex.setposition(all_x[i], all_y[i])
        alex.stamp()

    # plot best y
    y_plot.penup()
    y_plot.setposition(0, 0)
    y_plot.color('blue')
    for i in range(n):
        y_plot.setposition(all_x[i], best_y[i])
        y_plot.pendown()

    wn.exitonclick()

with open('labdata.txt', 'r') as f:
    plot_data = [aline.split() for aline in f]
    print(plot_data)

plotregression(plot_data)