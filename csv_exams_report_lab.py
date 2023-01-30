import csv

def candidate_count(exam_name):
    candidates = []
    with open('exam_results.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        for exam in reader:
            if exam['Exam Name'] == exam_name \
               and exam['Candidate ID'] not in candidates:
                candidates.append(exam['Candidate ID'])
    return len(candidates)

def exams_passed(exam_name):
    passed = 0
    with open('exam_results.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        for exam in reader:
            if exam['Exam Name'] == exam_name \
               and exam['Grade'] == 'Pass':
                passed += 1
    return passed

def exams_failed(exam_name):
    failed = 0
    with open('exam_results.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        for exam in reader:
            if exam['Exam Name'] == exam_name \
               and exam['Grade'] == 'Fail':
                failed += 1
    return failed

def worst_score(exam_name):
    worst_score = 110
    with open('exam_results.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        for exam in reader:
            if exam['Exam Name'] == exam_name \
            and int(exam['Score']) < worst_score:
                worst_score = int(exam['Score'])
    return worst_score

def best_score(exam_name):
    best_score = -110
    with open('exam_results.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        for exam in reader:
            if exam['Exam Name'] == exam_name \
            and int(exam['Score']) > best_score:
                best_score = int(exam['Score'])
    return best_score

with open('exams_report.csv', 'w') as csvout:
    fieldnames = ['Exam Name', 'Number of Candidates', 'Passed', 'Failed', 'Best', 'Worst']
    writer = csv.DictWriter(csvout, fieldnames=fieldnames)
    writer.writeheader()
    
    for subject in 'Maths', 'Physics', 'Biology':
        candidates = candidate_count(subject)
        passed = exams_passed(subject)
        failed = exams_failed(subject)
        worst = worst_score(subject)
        best = best_score(subject)
        
        writer.writerow({'Exam Name': subject,
                         'Number of Candidates' : candidates,
                         'Passed' : passed,
                         'Failed' : failed,
                         'Best' : best,
                         'Worst' : worst})
        

