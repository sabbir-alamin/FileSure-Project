
import json
import PyPDF2

with open("Form ADT-1-29092023_signed.pdf", "rb") as file:

    reader = PyPDF2.PdfReader(file)
    extracted_texts = reader.get_form_text_fields()


    formatted_key = {

        "CIN_C[0]" : "CIN",
        "CompanyName_C[0]" : "Company_Name",
        "CompanyAdd_C[0]" : "Company_Address",
        "EmailId_C[0]" : "Company_Email",
        "CurrDate[0]" : "Current_date",
        "PAN_C[0]" : "Account_number_of_auditors_firm",
        "NameAuditorFirm_C[0]" : "Firm_Name",
        "permaddress2a_C[0]" : "Permanent_Address_1",
        "permaddress2b_C[0]" : "Permanent_Address_1",
        "City_C[0]" : "City",
        "Country_C[0]" : "Country",
        "Pin_C[0]" : "Pin_code",
        "email[0]" : "Auditor_mail",
        "DateOfAccAuditedFrom_D[0]" : "Date_audit_form",
        "DateOfAccAuditedTo_D[0]" : "Date_audit_to",
        "NumOfFinanYearApp[0]" : "Number_of_final_year",
        "serialNumber[0]" : "Serial_Number",
        "Attachment_C[0]" : "Attachments",

    }

    new_dict = {}


    for key, value in extracted_texts.items():
        if value:
            if "\r" in value:
                value = value.replace("\r", " ")

            new_key = formatted_key.get(key, key)

            if "[0]" in new_key:
                continue

            new_dict[new_key] = value

with open("output.json", "w", encoding='utf-8') as new_file:
    json.dump(new_dict, new_file, indent=4)

print("The writings on the file is finished !!!")
















