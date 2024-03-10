def list_to_text(text):
    print_para = ""
    for i in text:
        print_line=""
        for w in i:
            print_line += w + " "
        print_para += print_line + "\n"
    print(print_para)
text=[
        ("Build","up","a","string","as","you","loop","through","the","tuple."),
        ("Then","print","it","when","you","move","between","the","tuples,"),
        ("i.e.,","the","items","in","the","main","list"),
    ]
list_to_text(text)