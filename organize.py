import pandas as pd

df = pd.read_csv("sephora_body.csv", usecols=['url','about']) # can also index sheet by name or fetch all sheets
print(df)

strings_to_find = ["What it is", "Skin type", "Skincare Concerns", "Highlighted Ingredients","Formulation","Benefits","What Else You Need to Know"]

whatitis=[]
skinconc=[]
highingr=[]
formu=[]
bene=[]
about=[]
other=[]
for item in df['about']:
    about.append(item)
    if isinstance(item, str):
        lines = item.split('\n')  # Split the text into lines
        found_start = False
        extracted_text = ''

        for line in lines:
            if "What it is" in line:
                found_start = True
                extracted_text=extracted_text + line
            elif found_start and line.strip() == "":
                break  # Break if an empty line is encountered after finding "What it is"
            elif found_start:
                extracted_text= extracted_text + line

        if extracted_text:
            whatitis.append(extracted_text)
        else:
            whatitis.append("No text found")
    else:
        whatitis.append("No about section")

    if isinstance(item, str):
        lines = item.split('\n')  # Split the text into lines
        found_start = False
        extracted_text = ''

        for line in lines:
            if "Skincare Concerns" in line:
                found_start = True
                extracted_text=extracted_text + line
            elif found_start and line.strip() == "":
                break  # Break if an empty line is encountered after finding "What it is"
            elif found_start:
                extracted_text= extracted_text + line

        if extracted_text:
            skinconc.append(extracted_text)
        else:
            skinconc.append("No text found")
    else:
        skinconc.append("No about section")

    if isinstance(item, str):
        lines = item.split('\n')  # Split the text into lines
        found_start = False
        extracted_text = ''

        for line in lines:
            if "Highlighted Ingredients" in line:
                found_start = True
                extracted_text=extracted_text + line
            elif found_start and line.strip() == "":
                break  # Break if an empty line is encountered after finding "What it is"
            elif found_start:
                extracted_text= extracted_text + line

        if extracted_text:
            highingr.append(extracted_text)
        else:
            highingr.append("No text found")
    else:
        highingr.append("No about section")

    if isinstance(item, str):
        lines = item.split('\n')  # Split the text into lines
        found_start = False
        extracted_text = ''

        for line in lines:
            if "Formulation" in line:
                found_start = True
                extracted_text=extracted_text + line
            elif found_start and line.strip() == "":
                break  # Break if an empty line is encountered after finding "What it is"
            elif found_start:
                extracted_text= extracted_text + line

        if extracted_text:
            formu.append(extracted_text)
        else:
            formu.append("No text found")
    else:
        formu.append("No about section")

    if isinstance(item, str):
        lines = item.split('\n')  # Split the text into lines
        found_start = False
        extracted_text = ''

        for line in lines:
            if "Benefits" in line:
                found_start = True
                extracted_text=extracted_text + line
            elif found_start and line.strip() == "":
                break  # Break if an empty line is encountered after finding "What it is"
            elif found_start:
                extracted_text= extracted_text + line

        if extracted_text:
            bene.append(extracted_text)
        else:
            bene.append("No text found")
    else:
        bene.append("No about section")

    if isinstance(item, str):
        lines = item.split('\n')  # Split the text into lines
        found_start = False
        extracted_text = ''

        for line in lines:
            if "What Else You Need to Know" in line:
                found_start = True
                extracted_text=extracted_text + line
            elif found_start and line.strip() == "":
                break  # Break if an empty line is encountered after finding "What it is"
            elif found_start:
                extracted_text= extracted_text + line

        if extracted_text:
            other.append(extracted_text)
        else:
            other.append("No text found")
    else:
        other.append("No about section")

# Create a new DataFrame using the extracted text dictionary
data = {'original about':about,
        'What it is':whatitis,
        'Skincare Concerns':skinconc,
        'Benefits':bene,
        'Highlighted Ingredients':highingr,
        'Formulation':formu,
        'What Else You Need to Know':other}

extracted = pd.DataFrame(data)
extracted.to_csv('organize_body.csv',index=False)
