import re

from python.backend.source_code.generic_parser import PatientDetails


class Patientparser(PatientDetails):
    def __init__(self,text):
        PatientDetails.__init__(self,text)

    def parse(self):
        return {
            "patient_name": self.get_field('patient_name'),
            'Phone_number': self.get_field('Phone_number'),
            'Hepatitis_vaccineStatus': self.get_field('Hepatitis_vaccineStatus'),
            'Any_MedicalProblems': self.get_field('Any_MedicalProblems')
        }

    def remove_noise_from_name(self, name):
        name = name.replace('Birth Date', '').strip()
        date_pattern = '((Jan|Feb|March|April|May|June|July|Aug|Sep|Oct|Nov|Dec)[ \d]+)'
        date_matches = re.findall(date_pattern, name)
        if date_matches:
            date = date_matches[0][0]
            name = name.replace(date, '').strip()
        return name

    def get_field(self,field_name):
        pattern_dict = {
            'patient_name':{'pattern': 'Patient Information(.*?)\(\d{3}\)','flags': re.DOTALL},
            'Phone_number':{'pattern': 'Patient Information(.*?)(\(\d{3}\) \d{3}-\d{4})','flags': re.DOTALL},
            'Hepatitis_vaccineStatus':{'pattern': 'Have you had the Hepatitis B vaccination?.*(Yes|No)','flags': re.DOTALL},
            'Any_MedicalProblems':{'pattern': 'List any Medical Problems .*?:(.*)\w+','flags': re.DOTALL},
        }

        pattern_object = pattern_dict.get(field_name)
        if pattern_object:
            matches = re.findall(pattern_object['pattern'], self.text, flags=pattern_object['flags'])
            name = ''
            if (field_name)=="patient_name":
                if matches:
                    print(name)
                    name = self.remove_noise_from_name(matches[0])
                return name

            if (field_name) == "Phone_number":
                return matches[0][-1]

            # Extracts only word of disease, wont go to new line
            elif (field_name)=="Any_MedicalProblems":
                find = matches[0]
                string = ''
                for i in find:
                    string+=i
                split_bynewLine = string.split('\n')
                return (split_bynewLine[2].strip())


            else:
                if len(matches) > 0:
                    return matches[0].strip()


if __name__ == '__main__':
    doc_text =  '''
    
    Patient Medical Record . : :

    Patient Information


    Birth Date
    Kathy Crawford May 6 1972
    (737) 988-0851 Weight:
    9264 Ash Dr 95
    New York City, 10005 a
    United States Height:
    190
    In Case of Emergency
    ee oe
    Simeone Crawford 9266 Ash Dr
    New York City, New York, 10005
    Home phone United States
    (990) 375-4621
    Work phone
    Genera! Medical History
    I i
    Chicken Pox (Varicella): Measies:
    IMMUNE IMMUNE

    Have you had the Hepatitis B vaccination?

    No

    List any Medical Problems (asthma, seizures, headaches):

    Migraine
    
    Removal Thing Will be Done!
    s'''
    pp = Patientparser(doc_text)
    print(pp.parse())

