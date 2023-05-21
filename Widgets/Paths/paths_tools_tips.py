class ToolsTips:
    URL = "https://demoqa.com/tool-tips"
    boton = "//button[contains(@id,'toolTipButton')]"
    text_field = "//input[contains(@id,'toolTipTextField')]"
    contrary_link = "//a[@href='javascript:void(0)'][contains(.,'Contrary')]"
    number_link = "//a[@href='javascript:void(0)'][contains(.,'1.10.32')]"
    list_elements = [boton, text_field, contrary_link, number_link]
    boton_text_expected = "You hovered over the Button"
    text_field_text_expected = "You hovered over the text field"
    contrary_link_text_expected = "You hovered over the Contrary"
    number_link_text_expected = "You hovered over the 1.10.32"
    lists_expected_text = [boton_text_expected, text_field_text_expected, contrary_link_text_expected,
                           number_link_text_expected]