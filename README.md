CYBER 38 TEAM

PREMIUM SECURITY TOOLKIT

<p align="center">
  <strong>CYBER 38 TEAM — SECURITY • DIAGNOSTICS • REPORTING</strong>
</p><p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python" alt="Python">
  <img src="https://img.shields.io/badge/Platform-Termux-green?style=for-the-badge" alt="Termux">
  <img src="https://img.shields.io/badge/Environment-Android-brightgreen?style=for-the-badge&logo=android" alt="Android">
  <img src="https://img.shields.io/badge/Category-Security-red?style=for-the-badge" alt="Security">
</p>---

1. ABOUT THE PROJECT

CYBER 38 TEAM — PREMIUM SECURITY TOOLKIT is a Python-based command-line utility designed for Termux and compatible Python environments.

It provides basic website security checks, DNS lookups, SSL/TLS certificate inspection, network connectivity diagnostics, and local JSON report generation through a simple interactive terminal interface.

The project focuses on usability, portability, and clear output without requiring a large collection of external Python dependencies.

Project Information

Property| Details
Project Name| CYBER 38 TEAM
Tool Name| Premium Security Toolkit
Developer Tag| DEVELOPER BOY
Team Identity| MINISTER | HITTER
Language| Python
Primary Platform| Android / Termux
Interface| Command-Line Interface
Report Format| JSON
External Python Dependencies| None required
Project Type| Security Diagnostics

---

2. KEY FEATURES

2.1 DNS Lookup

Resolves a domain name and displays the IP addresses returned by the system resolver.

Features:

- IPv4 and IPv6 address discovery when available.
- DNS resolution error reporting.
- Automatic JSON report generation.
- Simple domain input.

2.2 Website Security Check

Performs an HTTP request to a specified website and displays its HTTP response status.

It checks for the presence of these response headers:

- "Strict-Transport-Security"
- "Content-Security-Policy"
- "X-Content-Type-Options"
- "X-Frame-Options"
- "Referrer-Policy"

The results can help identify headers that may deserve further review.

Important: A missing header does not automatically mean that a website is vulnerable.

2.3 SSL/TLS Certificate Check

Inspects the TLS connection and certificate presented by an HTTPS server.

Information includes:

- Negotiated TLS version.
- Certificate issuer.
- Certificate expiration information.
- Negotiated cipher suite.
- Certificate validation errors.

The script uses Python's default certificate validation settings.

2.4 Network Diagnostics

Performs basic connectivity checks against a specified hostname.

The tool:

- Resolves the hostname.
- Checks TCP connectivity to ports 53, 80, and 443.
- Displays whether each connection succeeded.
- Saves diagnostic results to a JSON report.

These checks are intended for connectivity troubleshooting, not comprehensive port scanning.

2.5 JSON Report Management

Results are saved locally in JSON format.

Reports contain information such as:

- Tool name.
- Report category.
- Date and time.
- Target hostname or URL.
- Results and available response details.

Users can browse and display the latest ten report files from the interactive menu.

---

3. REQUIREMENTS

Before installing the toolkit, make sure you have:

- An Android device or compatible environment.
- Termux installed.
- A working internet connection for remote checks.
- Python 3.
- Permission to test the systems you use.

No additional Python packages are required by the current script.

Some checks may fail when DNS is unavailable, the remote server is offline, a firewall blocks connections, or the network is restricted.

---

4. INSTALLATION GUIDE

Step 1 — Update Termux

pkg update -y
pkg upgrade -y

Step 2 — Install Python

pkg install python -y

Step 3 — Create the Project Directory

mkdir -p ~/CYBER38
cd ~/CYBER38

Step 4 — Create the Main Script

nano cyber38.py

Paste the complete CYBER 38 TEAM Python source code into the editor.

Save the file using:

1. Press "CTRL + X".
2. Press "Y".
3. Press "ENTER".

Step 5 — Verify the Python Syntax

python -m py_compile cyber38.py

If no error appears, the file passed Python's syntax compilation check.

This does not guarantee that every network operation will succeed.

Step 6 — Launch the Toolkit

python cyber38.py

The interactive menu will appear in the terminal.

---

5. QUICK START

Use the following commands whenever you want to launch the toolkit.

cd ~/CYBER38
python cyber38.py

If you are already inside the project directory, simply run:

python cyber38.py

Interactive Menu

[1] DNS Lookup
[2] Website Security Check
[3] SSL/TLS Certificate Check
[4] Network Diagnostics
[5] View Saved Reports
[0] Exit

Enter the number of the operation you want to perform.

---

6. COMMAND REFERENCE

Launch the Toolkit

python cyber38.py

Check Python Version

python --version

Check Script Syntax

python -m py_compile cyber38.py

List Project Files

ls -la ~/CYBER38

List Saved Reports

ls -lh ~/CYBER38/reports/

Display a JSON Report

cat ~/CYBER38/reports/REPORT_FILENAME.json

Replace "REPORT_FILENAME.json" with the actual filename.

Display the Latest Report

ls -t ~/CYBER38/reports/*.json | head -n 1

To open the latest report directly:

latest=$(ls -t ~/CYBER38/reports/*.json | head -n 1)
[ -n "$latest" ] && cat "$latest"

Remove Python Bytecode Cache

find ~/CYBER38 -type d -name __pycache__ -exec rm -r {} +

This removes Python bytecode cache directories. It does not remove the source script or saved reports.

---

7. HOW TO USE EACH FEATURE

Option 1 — DNS Lookup

Select:

[1] DNS Lookup

Enter a domain name when prompted.

Example:

Domain: example.com

The tool attempts to resolve the domain and displays the returned IP addresses.

Possible outcomes:

- Successful DNS resolution.
- DNS lookup failure.
- Invalid or unavailable hostname.

A successful DNS lookup does not prove that a website is secure.

Option 2 — Website Security Check

Select:

[2] Website Security Check

Enter the URL of a website you own or are authorized to assess.

Example:

Authorized website URL: https://example.com

The tool displays the HTTP status and reports whether the selected security headers are present.

A header-presence check is only a basic assessment. It does not evaluate every possible security configuration or vulnerability.

Option 3 — SSL/TLS Certificate Check

Select:

[3] SSL/TLS Certificate Check

Enter an HTTPS domain.

Example:

HTTPS Domain: example.com

The tool attempts to establish a TLS connection and display certificate details.

A failed connection may indicate an invalid certificate, a DNS problem, a blocked port, an unsupported connection, or another network issue.

Option 4 — Network Diagnostics

Select:

[4] Network Diagnostics

Enter a hostname.

Example:

Test Host (default: example.com): example.com

The toolkit attempts TCP connections to ports 53, 80, and 443.

A failed connection does not necessarily mean that the port is closed. A firewall, filtering system, or network restriction may be responsible.

Option 5 — View Saved Reports

Select:

[5] View Saved Reports

The tool lists the latest ten JSON report files.

Enter the number of a report to display its contents.

Enter "0" to return from the report selection.

Option 0 — Exit

Select:

[0] Exit

The program closes normally.

---

8. REPORT STORAGE

Reports are stored inside:

~/CYBER38/reports/

Example directory structure:

CYBER38/
├── cyber38.py
├── README.md
└── reports/
    ├── 20261018_010101_123456.json
    ├── 20261018_010202_234567.json
    └── 20261018_010303_345678.json

The filenames use timestamps to help distinguish individual reports.

The actual filenames depend on when the reports are created.

Example Report Structure

{
  "tool": "CYBER 38 TEAM",
  "report_type": "DNS Lookup",
  "created_at": "2026-10-18T01:01:01",
  "host": "example.com",
  "addresses": [
    "93.184.216.34"
  ]
}

This is an illustrative example. Actual report values depend on the target and the network response.

Report files may contain hostnames, URLs, response headers, certificate details, and other diagnostic information. Store and share them responsibly.

---

9. TROUBLESHOOTING

Problem: Python Is Not Installed

Run:

pkg update
pkg install python -y

Problem: Cannot Find the Script

Run:

cd ~/CYBER38
ls -la

Confirm that "cyber38.py" exists.

Problem: Syntax Error

Run:

python -m py_compile cyber38.py

Check the line number and correct any accidental changes or missing punctuation.

Problem: DNS Resolution Failed

Check whether the internet connection works and whether the domain is spelled correctly.

You can also test DNS resolution with:

python -c "import socket; print(socket.getaddrinfo('example.com', None))"

Problem: SSL/TLS Error

Possible causes include:

- Invalid or expired certificates.
- Incorrect system date or time.
- DNS failure.
- Network filtering.
- TLS negotiation problems.

Do not disable certificate validation simply to make a failed check succeed.

Problem: Connection Timed Out

Check the network connection and try again later.

A remote server may be unavailable or may restrict connections.

Problem: No Reports Found

Run:

mkdir -p ~/CYBER38/reports
ls -la ~/CYBER38/reports

Reports are created only after a check reaches its report-saving stage successfully.

---

10. SECURITY AND RESPONSIBLE USE

CYBER 38 TEAM is intended for legitimate diagnostics, learning, and authorized security assessments.

Users are responsible for ensuring that their testing activities comply with applicable laws, policies, and permissions.

Responsible Use Guidelines

- Test only systems you own or have explicit permission to assess.
- Do not use diagnostic results to claim that a system is fully secure.
- Do not publish sensitive report contents without authorization.
- Protect saved reports if they contain private infrastructure details.
- Do not interpret a failed network connection as definitive proof of a security issue.
- Review findings carefully before making security decisions.

This toolkit does not provide a comprehensive penetration test, vulnerability scanner, exploit framework, or guarantee of security.

---

11. CURRENT LIMITATIONS

The current version has several limitations:

1. DNS results depend on the device's configured resolver.
2. Website checks inspect a limited set of HTTP response headers.
3. SSL/TLS checks inspect the presented certificate and negotiated connection.
4. Network diagnostics test only three predefined TCP ports.
5. The report viewer displays up to ten recent report filenames.
6. The script does not include a dedicated command-line "--help" interface.
7. The script does not implement automatic updates, licensing, authentication, or cloud report storage.
8. Network results can vary depending on DNS, firewalls, server availability, and the device's internet connection.

The interactive menu is the primary help and navigation interface.

---

12. PROJECT STRUCTURE

CYBER38/
├── cyber38.py
├── README.md
└── reports/

File Descriptions

File or Directory| Purpose
"cyber38.py"| Main application
"README.md"| Project documentation
"reports/"| Generated JSON reports

The "reports/" directory is created automatically when the script starts.

---

13. DEVELOPMENT AND FUTURE IMPROVEMENTS

Potential future improvements include:

- Dedicated command-line arguments and a help screen.
- Improved error handling and structured logging.
- Report export to additional formats.
- Unit tests for core functions.
- Configurable connection timeouts.
- Improved report filtering and search.
- Optional configuration files.
- Automated update checks with integrity verification.
- A more comprehensive test suite.

These are possible future features and are not included in the current implementation unless separately added.

---

14. DEVELOPER CREDITS

PROJECT: CYBER 38 TEAM

TOOL: PREMIUM SECURITY TOOLKIT

DEVELOPER TAG: DEVELOPER BOY

TEAM IDENTITY: MINISTER | HITTER

PLATFORM: TERMUX / ANDROID

LANGUAGE: PYTHON

Built for learning, diagnostics, and responsible security testing.

---

15. LICENSE

No specific open-source license is included by default.

Before distributing this project publicly, choose an appropriate license and include its terms in a "LICENSE" file. Do not claim a license that has not actually been selected.

---

16. FINAL NOTE

CYBER 38 TEAM — PREMIUM SECURITY TOOLKIT provides a simple starting point for DNS inspection, website header checks, TLS certificate inspection, network diagnostics, and local reporting.

Use it responsibly, understand the limits of its findings, and verify important security conclusions independently.

CYBER 38 TEAM — LEARN. TEST. DOCUMENT. IMPROVE.
