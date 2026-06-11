# Policy Compliance & Audit Analytics

## Overview

This project simulates a policy compliance auditing process commonly used in healthcare and insurance organizations. The solution analyzes policy, clause, and regulatory requirement data to identify compliance exceptions and support audit reviews.

The project uses **Python**, **Excel**, and **Power Query** to automate validation checks and generate audit reports.

---

## Business Objective

Review policy language records and identify potential compliance issues such as:

* Missing required clauses
* Duplicate clause loads
* Version mismatches between required and loaded clauses
* Effective-date validation checks

The goal is to improve reporting consistency and support compliance review processes.

---

## Tools Used

* Python (Pandas)
* Microsoft Excel
* Power Query
* Pivot Tables
* XLOOKUP
* Pivot Charts

---

## Project Structure

```text
Policy_Compliance_Audit/

  compliance_audit.py
  data/
     clause_library.csv
     regulatory_requirements.csv
     policy_forms.csv
     expected_clauses.csv
     publishing_loads.csv

  output/
     audit_summary.csv
     missing_clauses.csv
     duplicate_clauses.csv
     version_mismatches.csv

  Compliance_Audit.xlsx
```
---

## Audit Checks Performed

### Missing Clause Audit

Identifies required clauses that were expected but not loaded into policy records.

### Duplicate Clause Audit

Identifies policy and clause combinations loaded more than once.

### Version Mismatch Audit

Identifies loaded clause versions that do not match the approved required version.

### Effective-Date Validation

Validates whether policy effective dates align with regulatory requirement effective dates.

---

## Dashboard Reporting

An Excel dashboard was created to summarize audit results and highlight key findings.

Dashboard features include:

* KPI summary cards
* Compliance findings by audit type
* Audit summary and observations
* Automated reporting using Power Query and Excel formulas

---

## Key Findings

* Missing clauses represented the largest compliance issue.
* Duplicate clause loads suggested potential publishing or processing issues.
* Version mismatches indicated policy language may not align with approved versions.
* No effective-date violations were identified in the current sample dataset.

---

## Future Improvements

Potential enhancements include:

* Additional compliance rules (wrong state clause, expired clause, invalid product mapping)
* Power BI dashboard development
* DAX measures and KPI calculations
* Trend analysis across reporting periods
* Automated report refresh and distribution

---

## Skills Demonstrated

* Business Analysis
* Compliance Auditing
* Data Validation
* Exception Reporting
* Power Query
* Excel Reporting & Dashboarding
* Python Data Analysis
* Process Improvement
<img width="1375" height="812" alt="image" src="https://github.com/user-attachments/assets/a05fdc60-3c6f-4cf7-a3d9-6755621e0fd6" />
