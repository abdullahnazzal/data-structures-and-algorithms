def validate_brackets(brackets):
    """
    Arguments: string
    Return: boolean
    representing whether or not the brackets in the string are balanced
    """
    open_brackets={"(":0,"[":0,"{":0}
    close_brackets={")":0,"]":0,"}":0}
    for i in brackets:
        if i in open_brackets:
            open_brackets[i]+=1
        elif i in close_brackets:
            close_brackets[i]+=1
    if open_brackets["("]!=close_brackets[")"]:
        return False
    elif open_brackets["["]!=close_brackets["]"]:
        return False
    elif open_brackets["{"]!=close_brackets["}"]:
        return False
    else:
        return True
print(validate_brackets("((fgh))"))
