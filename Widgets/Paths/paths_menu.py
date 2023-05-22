class menu:
    URL = "https://demoqa.com/menu#"
    main_item_1 = "//a[@href='#'][contains(.,'Main Item 1')]"
    main_item_2 = "//a[@href='#'][contains(.,'Main Item 2')]"
    main_item_3 = "//a[@href='#'][contains(.,'Main Item 3')]"
    sub_item_1 = "(//a[@href='#'][contains(.,'Sub Item')])[1]"
    sub_item_2 = "(//a[@href='#'][contains(.,'Sub Item')])[2]"
    sub_list = "//a[@href='#'][contains(.,'SUB SUB LIST »')]"
    sub_sub_list_1 = "//a[@href='#'][contains(.,'Sub Sub Item 1')]"
    sub_sub_list_2 = "//a[@href='#'][contains(.,'Sub Sub Item 2')]"
    list_items = [main_item_1, main_item_2, sub_item_1, sub_item_2, sub_list, sub_sub_list_1, sub_sub_list_2,
                  main_item_3]
    list_text_expected = ["Main Item 1", "Main Item 2", "Sub Item", "Sub Item", "SUB SUB LIST »", "Sub Sub Item 1",
                          "Sub Sub Item 2", "Main Item 3"]
