import re
from prettytable import PrettyTable

keywords = {"def", "return", "if", "print", "for", "in", "range"}
separators = {"(", ")", ",", ":"}
operators = {"+", "==", "="}
keyword_count = 0
keyword_list = []
separator_count = 0
separator_list = []
operator_count = 0
operator_list = []
literal_count = 0
literal_list = []
identifier_count = 0
identifier_list = []

# splits the string by characters and symbols
def tokenization(line):
    tokens = re.findall(r'\".*?\"|\b\w+\b|==|[=()+,:]', line)
    return tokens

# tokenized the remaining string and stores it into a list and tracks the count 
def token_count(token_array):
    global keyword_count, separator_count, operator_count, identifier_count, literal_count
    for token in token_array:
        if token in keywords:
            keyword_count += 1
            if token not in keyword_list:
                keyword_list.append(token)
        elif token in separators:
            separator_count += 1
            if token not in separator_list:
                separator_list.append(token)
        elif token in operators:
            operator_count += 1
            if token not in operator_list:
                operator_list.append(token)
        elif "\"" in token: 
            literal_count += 1
            if token not in literal_list:
                literal_list.append(token)
        elif token.isdigit():
            literal_count += 1
            if token not in literal_list:
                literal_list.append(token) 
        else:
            identifier_count += 1
            if token not in identifier_list:
                identifier_list.append(token)
            

def main():
    comment = "#"
    docstring = '"""'
    is_docstring = False

    # takes in the output file 
    file_name = input("Hello, enter the name of the text file you would like to read >> ")
    file = open(file_name, "r") 

    print("")
    # breaks up the file line by line, first removes leading whitespace, then comments, then empty lines. 
    for line in file:
        stripped_line = line.strip()

        # checks for docstring and handles everything in between 
        if stripped_line.startswith(docstring):
            is_docstring = not is_docstring
            continue
        if is_docstring:
            continue

        # checks if there is a comment in the beginning as well as if it is in the line and handles 
        if comment in stripped_line:
            if stripped_line.startswith(comment):
                continue
            else:
                new_stripped_line= ""
                for c in stripped_line:
                    new_stripped_line += c
                    if c == comment:
                        break
                    print(c, end='')

                # handles tokenization for remaining string
                tokenized_array = tokenization(new_stripped_line)
                token_count(tokenized_array)
            print("")

        # otherwise prints the line 
        elif stripped_line:
            print(stripped_line)

            # handles tokenization 
            tokenized_array = tokenization(stripped_line)
            token_count(tokenized_array)
    
    print("")
    print("")
    table = PrettyTable()
    table.field_names = ["Category", "Tokens", "Count"]
    table.add_row(["Keyword", keyword_list, keyword_count])
    table.add_row(["Separator", separator_list, separator_count])
    table.add_row(["Operator", operator_list, operator_count])
    table.add_row(["Identifier", identifier_list, identifier_count])
    table.add_row(["Literal", literal_list, literal_count])
    table.align["Category"] = "l"
    table.align["Tokens"] = "l"
    table.align["Count"] = "l"

    print(table)
    print("Total tokens:" + str(keyword_count+separator_count+operator_count+identifier_count+literal_count))
    file.close()

if __name__ == "__main__":
    main()