import re


def ZGenerate(FullFile):
    # ZScript Generation
    print("Generating ZScript")

    # Defaults
    print("  Defaults:", end=" ")
    Pattern = re.compile("\\[Property\\](\\s*){([^{}]*)}", re.IGNORECASE)
    Call = Pattern.search(FullFile)
    while Call:
        Call = re.sub("\\s+", " ", Call.group(2))
        Sections = Call.split("[")
        Call = "Default{"
        for Section in Sections:
            if len(Section) < 2:
                continue
            Section = Section.split("]")
            SectionName = Section[0]
            for Default in Section[1].split(";"):
                if SectionName[:5] == "Flags":
                    Default = Default.split("=")
                    if len(Default) < 2:
                        continue
                    Call += "+" if Default[1] == "true" else "-"
                    if SectionName.find(".") > -1:
                        Call += SectionName.split(".")[1]+"."
                    Call += Default[0]+";"
                else:
                    if SectionName == "Type":
                        Call += Default+";"
                    else:
                        Default = Default.split("=")
                        if len(Default) < 2:
                            continue
                        if SectionName == "Info":
                            Call += "//$"+Default[0]+" "+Default[1]+"\n"
                        else:
                            if not SectionName == "Default":
                                Call += SectionName+"."
                            Call += Default[0]+" " + \
                                re.sub("[()]", "", Default[1])+";"
        FullFile = Pattern.sub(Call+"}", FullFile, 1)
        Call = Pattern.search(FullFile)
    print("Successful")

    # TODO: C-style preprocessing

    # End
    return FullFile
