# coding: utf-8

def word_count(string):
    """Roughly count words by splitting on spaces."""
    return len(string.split(" "))

def expand_gnu(string):
    """Expand the 'GNU' acronym."""
    return string.replace("GNU", "GNU's Not UNIX")

def expand_unix(string):
    """Expand the UNIX 'acronym'."""
    return string.replace("UNIX", "Uniplexed Information Computing System")


if __name__ == "__main__":
    title = "GIMP"

    expanded = "GNU Image Manipulation Program"

    temp = expanded + "\n\n"

    result = title + "\n\n" + temp

    while word_count(result) < 50000:
        if "GNU" in temp:
            temp = expand_gnu(temp)
            result += temp
        if "UNIX" in temp:
            temp = expand_unix(temp)
            result += temp

    with open("GIMP_expanded.txt", "w") as f:
        f.write(result)


