from graphics import * # Import graphics library with all functions

def draw_bar(index, win, label, value, max_value, width, color): # Function to draw a bar in bar chart
    if value == 0:
        height = 0 # Set height to 0 if value is 0
        x1 = ((win.getWidth() / 4) * index) - (win.getWidth() / 8) - (width / 2) # Set x1 to the left of the bar
        y1 = win.getHeight() - (win.getHeight() // 12) # Set y1 to the bottom of the bar because height is 0
        x2 = x1 + width # Set x2 to the right of the bar
        y2 = win.getHeight() - (win.getHeight() // 12) # Set y2 to the bottom of the bar

    else: # If value is not 0, calculate heighht using formula created with max_value and value
        height = (((win.getHeight() - win.getHeight() // 8) - win.getHeight() // 12) / max_value) * value
        x1 = ((win.getWidth() / 4) * index) - (win.getWidth() / 8) - (width / 2) # Set x1 to the left of the bar
        y1 = win.getHeight() - (height + win.getHeight() // 12) # Set y1 to the top of the bar
        x2 = x1 + width # Set x2 to the right of the bar
        y2 = win.getHeight() - (win.getHeight() // 12) # Set y2 to the bottom of the bar

    bar = Rectangle(Point(x1, y1), Point(x2, y2)) # Create bar
    bar.setFill(color)
    bar.setOutline('black')
    bar.draw(win)

    label_text = Text(Point(((x1 + x2) / 2), y2 + (win.getHeight() // 60)), label) # Create label and set it below the bar
    label_text.setTextColor('slate gray')
    label_text.setSize(14)
    label_text.setStyle('bold')
    label_text.setFace('helvetica')
    label_text.draw(win)

    value_text = Text(Point(((x1 + x2) / 2), y1 - (win.getHeight() // 60)), str(value)) # Set value above the bar
    value_text.setTextColor('slate gray')
    value_text.setSize(14)
    value_text.setStyle('bold')
    value_text.setFace('helvetica')
    value_text.draw(win)

def draw_histogram(p, t, r, e): # Function to draw histogram
    win = GraphWin('Histogram', 1000, 600) # Create window
    win.setBackground('honeydew')
    title = Text(Point(200, 30), 'Histogram Results') # Create title
    title.setTextColor('dim gray')
    title.setSize(24)
    title.setStyle('bold')
    title.setFace('helvetica')
    title.draw(win)

    # Draw a line as the x axis (at the bottom of the histogram)
    bottom_line = Line(Point((win.getWidth() / 40), (win.getHeight() - (win.getHeight() // 12))), Point((win.getWidth() - (win.getWidth() / 40)), (win.getHeight() - (win.getHeight() // 12))))
    bottom_line.draw(win)
    
    max_value = max(p, t, r, e) # Get the maximum value of all outcomes to calculate height of bars
    width = 140 # Set width of bars

    # Draw bars for each outcome
    draw_bar(1, win, 'Progress', p, max_value, width, 'light green')
    draw_bar(2, win, 'Trailer', t, max_value, width, 'dark sea green')
    draw_bar(3, win, 'Retriever', r, max_value, width, 'dark khaki')
    draw_bar(4, win, 'Excluded', e, max_value, width, 'pink')

    # Display total number of outcomes
    if (p + t + r + e) == 1: # If there is only 1 outcome, change the text to singular
        total_text = Text(Point(win.getWidth() // 7, (win.getHeight() - win.getHeight() // 30)), '1 outcome.')
        total_text.setTextColor('black')
        total_text.setSize(18)
        total_text.setStyle('bold')
        total_text.setFace('helvetica')
        total_text.draw(win)
    else: # If there are more than 1 outcomes, change the text to plural
        total_text = Text(Point(win.getWidth() // 5, (win.getHeight() - win.getHeight() // 30)), f'{p + t + r + e} outcomes in total.')
        total_text.setTextColor('black')
        total_text.setSize(18)
        total_text.setStyle('bold')
        total_text.setFace('helvetica')
        total_text.draw(win)
    
    try:
        win.getMouse() # Wait for mouse click
    except GraphicsError:
        pass # If user closes window run program without error
    win.close() # Close window
    

'''
Accessed https://en.wikipedia.org/wiki/X11_color_names to get color names for histogram

Author: Mahima Dharmasena
'''