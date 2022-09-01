from python.backend.source_code.parser_prescription import PrescriptionParser
import pytest

@pytest.fixture()
def doc1():
    document_text = '''
    Dr Jon Smith, MD
    2 non-Important Street
    New york, Phone (000)-111-222
    Name: marta sharun Date: 30/07/2022
    Address:9 tennis court, DC
    Prednisonse 20mg
    Lialda 2.4gm 
    Directions: 
    Prednisonse, taper 5mg every 3days
    Refill: 2times
    '''
    return PrescriptionParser(document_text)

@pytest.fixture()
def doc2():
    document_text='''
    Dr John Smith, MD
    2 Non-Important Street,
    New York, Phone (900)-343-2222
    
    Name: Virat Kohli Date: 30/07/2022
    Address: 2 cricket street, New Delhi
    omeprazole 40mg
    Directions: use two tablets daily
    Refill: 3 times 
    '''
    return PrescriptionParser(document_text)


@pytest.fixture()
def doc_3_empty():
    return PrescriptionParser('')

def test_get_name(doc1,doc2):
    assert doc1.get_field('patient_name') == 'marta sharun'
    assert doc2.get_field('patient_name') == 'Virat Kohli'


def test_get_address(doc1,doc2):
    assert doc1.get_field('patient_address') == '9 tennis court, DC'


def test_get_medicines(doc1,doc2):
    assert doc1.get_field('medicines') == 'Prednisonse 20mg\n    Lialda 2.4gm'


def test_get_directions(doc1,doc2):
    assert doc1.get_field('directions') == 'Prednisonse, taper 5mg every 3days'


def test_get_refills(doc1,doc2):
    assert doc1.get_field('refills') == '2'


def test_parse(doc_1_maria, doc_2_virat, doc_3_empty):
    record_maria = doc_1_maria.parse()
    assert record_maria['patient_name'] == 'marta sharun'
    assert record_maria['patient_address'] == '9 tennis court, DC'
    assert record_maria['medicines'] == 'Prednisone 20 mg\n  Lialda 2.4 gram'
    assert record_maria['directions'] == 'Prednisone, taper 5 mg every 3 days'
    assert record_maria['refills'] == '2'

    record_virat = doc_2_virat.parse()
    assert record_virat == {
        'patient_name': 'Virat Kohli',
        'patient_address': '2 cricket street, New Delhi',
        'medicines': 'omeprazole 40 mg',
        'directions': 'use two tablets daily',
        'refills': '3'
    }

    record_empty = doc_3_empty.parse()
    assert record_empty == {
        'patient_name': None,
        'patient_address': None,
        'medicines': None,
        'directions': None,
        'refills': None
    }


