import json
from fpdf import FPDF


# save FPDF() class into a variable pdf
pdf = FPDF("P", "mm", "Letter")

# Add a page
pdf.add_page()


# It wil act as a header
pdf.set_font("courier", "B", 14)
pdf.cell(200, 10, txt="Resume", ln=1, align='C')
pdf.ln(15)

# Read
myjsonfile = open("resume.json", "r")
jsondata = myjsonfile.read()

# Parse
j_obj = json.loads(jsondata)

# Get the list of Profile within the j_obj
P_list = j_obj["Profile"]

# Set style and size of font
pdf.set_font("courier", "B", 14)
# contains the text and align it in left positon
pdf.cell(200, 10, txt="Profile", ln=1, align='L')

# Using the for loop we could access the data within the P_list individually.
for i in range(len(P_list)):
    g_motto = P_list[i].get("=")
    j_motto = str("      :" + g_motto)
    # set style and size of font
    pdf.set_font("courier", "", 12)
    pdf.cell(100, 10, txt=j_motto, ln=1, align='L')

# Get the list of Basic_Info int the j_obj
B_list = j_obj["Basic_Info"]


pdf.cell(200, 10, txt=" ", ln=1, align='L')
pdf.set_font("courier", "B", 14)
pdf.cell(200, 10, txt="Basic Information", ln=1, align='L')


# Using the for loop we could access the data within the B_list individually.
for i in range(len(B_list)):

    # Get the equivalent value of Name within the list (B_List).
    g_name = B_list[i].get("Name")
    j_name = str("      Name:" + g_name)
    pdf.set_font("courier", "", 12)
    pdf.cell(200, 10, txt=j_name, ln=1, align='L')

    # Get the equivalent value of Age within the list (B_List).
    g_age = B_list[i].get("Age")
    j_age = str("      Age:" + g_age)
    pdf.set_font("courier", "", 12)
    pdf.cell(200, 10, txt=j_age, ln=1, align='L')

    # Get the equivalent value of Phone within the list (B_List).
    g_phone = B_list[i].get("Phone")
    j_phone = str("      Contact Number:" + g_phone)
    pdf.set_font("courier", "", 12)
    pdf.cell(200, 10, txt=j_phone, ln=1, align='L')

    # Get the equivalent value of Email within the list (B_List).
    g_email = B_list[i].get("Email")
    j_email = str("      Email:" + g_email)
    pdf.set_font("courier", "", 12)
    pdf.cell(200, 10, txt=j_email, ln=1, align='L')

# Get the list of Education_Atainment within the j_obj
E_list = j_obj["Education_Atainment"]

pdf.cell(200, 10, txt=" ", ln=1, align='L')
pdf.set_font("courier", "B", 14)
pdf.cell(200, 10, txt="Educational Attainment", ln=1, align='L')

# Using the for loop we could access the data within the E_list individually.
for i in range(len(E_list)):

    # Get the equivalent value of  Elementary  within the list (E_List).
    g_elem = E_list[i].get("Elementary")
    j_elem = str("      Elementary:" + g_elem)
    pdf.set_font("courier", "", 12)
    pdf.cell(200, 10, txt=j_elem, ln=1, align='L')

    # Get the equivalent value of  Junior High Schoolr within the list (E_List).
    g_junoir = E_list[i].get("Junior High School")
    j_junoir = str("      Junior High School:" + g_junoir)
    pdf.set_font("courier", "", 12)
    pdf.cell(200, 10, txt=j_junoir, ln=1, align='L')

    # Get the equivalent value of Senior High School within the list (E_List).
    g_senior = E_list[i].get("Senior High School")
    j_senior = str("      Senior High School:" + g_senior)
    pdf.set_font("courier", "", 12)
    pdf.cell(200, 10, txt=j_senior, ln=1, align='L')

    # Get the equivalent value of Tertiary within the list (E_List).
    g_ter = E_list[i].get("Tertiary")
    j_ter = str("      Tertiary:" + g_ter)
    pdf.set_font("courier", "", 12)
    pdf.cell(200, 10, txt=j_ter, ln=1, align='L')

# Get the list of Skills within the j_obj
S_list = j_obj["Skills"]

pdf.cell(200, 10, txt=" ", ln=1, align='L')
pdf.set_font("courier", "B", 14)
pdf.cell(200, 10, txt="Skills: ", ln=1, align='L')

# Using the for loop we could access the data within the S_list individually.
for i in range(len(S_list)):

    # Get the equivalent value of one within the list (S_List).
    g_one = S_list[i].get("one")
    j_one = str("      : " + g_one)
    pdf.set_font("courier", "", 12)
    pdf.cell(200, 10, txt=j_one, ln=1, align='L')

    # Get the equivalent value of two within the list (S_List).
    g_2 = S_list[i].get("two")
    j_2 = str("      : " + g_2)
    pdf.set_font("courier", "", 12)
    pdf.cell(200, 10, txt=j_2, ln=1, align='L')
    # Get the equivalent value of three within the list (S_List).
    g_3 = S_list[i].get("three")
    j_3 = str("      : " + g_3)
    pdf.set_font("courier", "", 12)
    pdf.cell(200, 10, txt=j_3, ln=1, align='L')

    # Get the equivalent value of four within the list (S_List).
    g_4 = S_list[i].get("four")
    j_4 = str("      : " + g_4)
    pdf.set_font("courier", "", 12)
    pdf.cell(200, 10, txt=j_4, ln=1, align='L')

# save the pdf with name .pdf
pdf.output("VILLAS_JUSTIN.pdf")
