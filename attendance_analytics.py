\"\"\"
Attendance analytics engine for calculating percentage, threshold alerts, and student performance correlations.
\"\"\"
from typing import List, Dict, Any

class AttendanceAnalytics:
    @staticmethod
    def calculate_attendance_rate(present_days: int, total_days: int) -> float:
        if total_days <= 0:
            return 0.0
        return round((present_days / total_days) * 100, 2)

    @staticmethod
    def identify_at_risk_students(records: List[Dict[str, Any]], threshold: float = 75.0) -> List[Dict[str, Any]]:
        at_risk = []
        for student in records:
            rate = AttendanceAnalytics.calculate_attendance_rate(
                student.get('present_days', 0),
                student.get('total_days', 0)
            )
            if rate < threshold:
                student_copy = dict(student)
                student_copy['attendance_percentage'] = rate
                student_copy['alert_flag'] = True
                at_risk.append(student_copy)
        return at_risk