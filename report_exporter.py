\"\"\"
Attendance report export formatting utility (CSV / JSON formatters).
\"\"\"
import csv
import io
from typing import List, Dict, Any

class ReportExporter:
    @staticmethod
    def export_to_csv_string(records: List[Dict[str, Any]]) -> str:
        if not records:
            return ""
        output = io.StringIO()
        fieldnames = list(records[0].keys())
        writer = csv.DictWriter(output, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(records)
        return output.getvalue()