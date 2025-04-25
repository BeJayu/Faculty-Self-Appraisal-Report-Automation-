from datetime import datetime

class AppraisalEntry:
    def __init__(self, parameter_no, subpoint, description, file_path, self_score, max_score):
        self.parameter_no = parameter_no     # 1 to 10
        self.subpoint = subpoint             # e.g., "1.A", "3.B"
        self.description = description       # Text input from user
        self.file_path = file_path           # Uploaded file name/path
        self.self_score = self_score         # Given by faculty
        self.max_score = max_score           # Max marks
        self.verified_score = None           # Admin-reviewed score (optional)

    def to_dict(self):
        return {
            "parameter_no": self.parameter_no,
            "subpoint": self.subpoint,
            "description": self.description,
            "file_path": self.file_path,
            "self_score": self.self_score,
            "max_score": self.max_score,
            "verified_score": self.verified_score
        }

class AppraisalForm:
    def __init__(self, employee_id, year, entries):
        self.employee_id = employee_id
        self.year = year
        self.entries = entries               # List of AppraisalEntry
        self.total_score = sum(entry.self_score for entry in entries)
        self.submission_date = datetime.now()
        self.submitted = True                # One-time submission flag

    def to_dict(self):
        return {
            "employee_id": self.employee_id,
            "year": self.year,
            "entries": [entry.to_dict() for entry in self.entries],
            "total_score": self.total_score,
            "submission_date": self.submission_date,
            "submitted": self.submitted
        }
