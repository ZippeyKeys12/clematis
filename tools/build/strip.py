import re


def ZStript(FullFile, Whitespace=False, Comments=True):
    if Comments:
        # Block
        FullFile = re.sub("(?s)\\/\\*.*?\\*\\/", " ",
                          FullFile, flags=re.DOTALL | re.IGNORECASE)
        # Single-line
        FullFile = re.sub("\\/\\/+.*", " ", FullFile, flags=re.IGNORECASE)
    if Whitespace:
        FullFile = re.sub("\\s+", " ", FullFile, flags=re.IGNORECASE)
        Tokens = ["{", "}", "\\(", "\\)", "\\[", "\\]", ";", ">", "\\*", "="]
        for Token in Tokens:
            FullFile = re.sub(
                "\\s*"+Token+"\\s*", Token.replace("\\", ""), FullFile, flags=re.IGNORECASE)
    return FullFile
