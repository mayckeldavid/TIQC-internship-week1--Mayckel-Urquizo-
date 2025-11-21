import pytest
from mine import calculate_gpa
import tempfile
import os

def write_csv(content: str):
    tmp = tempfile.NamedTemporaryFile(delete=False, suffix=".csv", mode="w", encoding="utf-8")
    tmp.write(content)
    tmp.close()
    return tmp.name

def test_normal_case():
    csv_text = "name,grade\nAna,90\nLuis,80\n"
    path = write_csv(csv_text)
    try:
        assert calculate_gpa(path) == 85.0
    finally:
        os.unlink(path)

def test_invalid_rows_ignored():
    csv_text = "name,grade\nAna,90\nMalo,xx\nPedro,100\n"
    path = write_csv(csv_text)
    try:
        assert calculate_gpa(path) == 95.0
    finally:
        os.unlink(path)

def test_empty_valid_rows():
    csv_text = "name,grade\nMalo,xx\nOtra,??\n"
    path = write_csv(csv_text)
    try:
        with pytest.raises(ValueError):
            calculate_gpa(path)
    finally:
        os.unlink(path)

