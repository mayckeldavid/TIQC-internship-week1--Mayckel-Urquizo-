import csv
import sys
from statistics import mean

def calculate_gpa(csv_path: str) -> float:
    grades = []

    with open(csv_path, newline='', encoding='utf-8') as f:
        reader = csv.reader(f)
        next(reader, None)

        for row in reader:
            if len(row) < 2:
                continue
            try:
                grade = float(row[1])
                grades.append(grade)
            except ValueError:
                continue

    if not grades:
        raise ValueError("No grades found in file.")

    return mean(grades)

def main():
    if len(sys.argv) < 2:
        print("Uso: python main.py students.csv")
        sys.exit(1)

    csv_path = sys.argv[1]

    try:
        gpa = calculate_gpa(csv_path)
        print(f"{gpa:.2f}")
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
