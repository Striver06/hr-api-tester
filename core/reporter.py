import json
from datetime import datetime

class Reporter:
    def __init__(self):
        self.results = []

    def log(self, test_name, status, details=None):
        self.results.append({
            "test": test_name,
            "status": status,
            "details": details,
            "timestamp": datetime.utcnow().isoformat()
        })

    def save_json(self):
        with open("reports/latest.json", "w") as f:
            json.dump(self.results, f, indent=2)

    def save_html(self):
        rows = ""
        for r in self.results:
            rows += f"<tr><td>{r['test']}</td><td>{r['status']}</td><td>{r['details']}</td></tr>"

        html = f"""
        <html>
        <head><title>HR API Test Report</title></head>
        <body>
        <h2>HR API Test Report</h2>
        <table border="1">
            <tr><th>Test</th><th>Status</th><th>Details</th></tr>
            {rows}
        </table>
        </body>
        </html>
        """

        with open("reports/latest.html", "w") as f:
            f.write(html)
