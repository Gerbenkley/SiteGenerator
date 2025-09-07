

def markdown_to_blocks(markdown):
    split_markdown = markdown.split("\n\n")
    blocks = []
    for each in split_markdown:
        if each != "":
            blocks.append(each.strip())
    return blocks