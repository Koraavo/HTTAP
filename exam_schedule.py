from colors import color

print(color.BLUE + "9. Display the examination schedule."
      " (extract the date from exam_st_date)."
      "exam_st_date = (11, 12, 2014)"
      "Sample Output : The examination will start from : 11 / 12 / 2014\n\n" + color.END)

exam_st_date = (11, 12, 2014) # you can also use %i (for integers)
print ("The examination will start from: %d / %d / %d" %exam_st_date)
