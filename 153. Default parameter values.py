def banner_text(text, screen_width=80):
    if len(text) > screen_width - 4:
        raise ValueError(f"String {text} is larger then specified width {screen_width}")
    
    if text == "*":
        print("*" * screen_width)
    else:
        centered_text = text.center(screen_width - 4)
        output_string  = "*{}*".format(centered_text)
        print(output_string)


banner_text("*")
banner_text("Always look on the bright side of life...")
banner_text("If life seems jolly rotten,")
banner_text("There's something you've forgotten!")
banner_text("And that's to laugh and smile and dance and sing,")
banner_text(" ", 80)
banner_text("When you're feeling in the dumps,", 80)
banner_text("Don't be silly chumps,", 66)
banner_text("Just purse your lips and whistle - that's the thing!", 66)
banner_text("And... always look on the bright side of life...", 66)
banner_text("*", 66)

