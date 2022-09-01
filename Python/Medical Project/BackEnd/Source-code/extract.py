from pdf2image import convert_from_path
import pytesseract

from python.backend.source_code.parser_prescription import PrescriptionParser
from python.backend.source_code.parser_patient import Patientparser

POPPLER_PATH = r"D:\Tutorials\poppler-22.04.0\Library\bin"
pytesseract.pytesseract.tesseract_cmd = r"D:\Tutorials\opencv1\tesseract.exe"
from python.backend.source_code.util import preprocess_image

def extractor(file_path,file_format):
    #extracting text from pdf file
    pages = convert_from_path(file_path,poppler_path=POPPLER_PATH)
    document_text = ""

    if len(pages)>0:
        page = pages[0]
        processed_image = preprocess_image(page)
        text = pytesseract.image_to_string(processed_image,lang='eng')
        document_text = "\n" + text


    # extract fields from text
    if file_format == "prescription":
        extracted_data=PrescriptionParser(document_text).parse()
    elif file_format == "patient_details":
        extracted_data = Patientparser(document_text).parse()
    else:
        raise Exception(f"Invalid Document Format: {file_format}")

    return extracted_data

if __name__=="__main__":
    data = extractor(r"D:\Tutorials\codebasics\python\backend\resources\prescription\pre_1.pdf","prescription")
    print(data)
    # data1 = extract(r"D:\Tutorials\codebasics\python\backend\resources\patient_details\pd_1.pdf",'patient_details')
    # print(data1)