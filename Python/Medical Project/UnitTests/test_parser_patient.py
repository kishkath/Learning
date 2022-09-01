import pytest

from python.backend.source_code.parser_patient import Patientparser
import pytest


@pytest.fixture()
def doc1():
    document_text = '''
17/12/2020

Patient Medical Record

Patient Information Birth Date

Kathy Crawford May 6 1972

(737) 988-0851 Weight’

9264 Ash Dr 95

New York City, 10005 '

United States Height:
190

In Case of Emergency
ee J
Simeone Crawford 9266 Ash Dr
New York City, New York, 10005
Home phone United States
(990) 375-4621
Work phone
Genera! Medical History
nn ee
Chicken Pox (Varicella): Measies:
IMMUNE

IMMUNE
Have you had the Hepatitis B vaccination?

No

List any Medical Problems (asthma, seizures, headaches}:

Migraine

.

‘Name of Insurance Company:

Random Insuarance Company - 4789 Bollinger Rd
Jersey City, New Jersey, 07030

a Policy Number:
71 1520731 3 Expiry Date:

. 30 December 2020
Do you have medical insurance?

Yes:

Medical Insurance Details

List any allergies:

Peanuts

List any medication taken regularly:
Triptans


.

‘Name of Insurance Company:

Random Insuarance Company - 4789 Bollinger Rd
Jersey City, New Jersey, 07030

a Policy Number:
71 1520731 3 Expiry Date:

. 30 December 2020
Do you have medical insurance?

Yes:

Medical Insurance Details

List any allergies:

Peanuts

List any medication taken regularly:
Triptans


'''
    return Patientparser(document_text)

@pytest.fixture()
def doc_2_empty():
    return Patientparser('')


def test_get_patientname(doc1):
    assert doc1.get_field('patient_name') == 'Kathy Crawford'


def test_get_Phone_number(doc1):
    assert doc1.get_field('Phone_number') == '(737) 988-0851'


def test_get_Hepatitis_vaccineStatus(doc1):
    assert doc1.get_field('Hepatitis_vaccineStatus') == 'Yes'


def test_get_Any_MedicalProblems(doc1):
    assert doc1.get_field('Any_MedicalProblems') == 'Migrane'




def test_parse(doc_1, doc_2_empty):
    record1 = doc1.parse()
    assert record1['patient_name'] == 'Kathy Crawford'
    assert record1['Phone_number'] == '(737) 988-0851'
    assert record1['Hepatitis_vaccineStatus'] == 'Yes'
    assert record1['Any_MedicalProblems'] == 'Migrane'

    #
    # record_empty = doc_2_empty.parse()
    # assert record_empty == {
    #     'patient_name': None,
    #     'Phone_number': None,
    #     'Hepatitis_vaccineStatus': None,
    #     'Any_MedicalProblems': None,
    #
    # }


