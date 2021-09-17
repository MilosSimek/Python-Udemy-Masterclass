def banner_text(text):
    screen_width = 80
    if len(text) > screen_width - 4:
        print("EEK!!")
        print("THE TEXT IS TO LONG TO FINT IN THE SPECIFIED WIDTH")
    
    if text == "*":
        print("*" * screen_width)
    else:
        centered_text = text.center(screen_width - 4)
        output_string  = "*{}*".format(centered_text)
        print(output_string)


banner_text("*")
banner_text("AAA")
banner_text("AAAAAAAAAAAAAAAAAA")
banner_text("*")

result = banner_text("Nothing to return")
print(result)

numbers = [4, 2, 6, 5, 9, 1, 4, 8]
print(numbers.sort())