import pandas as pd

expected_clauses = pd.read_csv(
    "data/expected_clauses.csv"
)

publishing_loads = pd.read_csv(
    "data/publishing_loads.csv"
)


# Audit #1: Missing Clauses
# BQ: How many required clauses were not loaded into policy documents

missing_clauses = expected_clauses.merge(
    publishing_loads[["Policy_ID", "Clause_ID"]], # only brings in those two columns
    on=["Policy_ID", "Clause_ID"],
    how="left",
    indicator=True # adds a _merge column that tells you where each row came from
)

missing_clauses = missing_clauses[
    missing_clauses["_merge"] == "left_only"
]

print(missing_clauses.shape)

print(missing_clauses.head())

missing_clauses.to_csv(
    "output/missing_clause.csv",
    index=False
)

print("Missing Clauses Saved")


# Audit #2: Duplicate Clauses
# BQ: Find every clause that was published more than once for the same policy

duplicate_clauses = (
    publishing_loads
    .groupby(
        ["Policy_ID", "Clause_ID"]
    )
    .size()
    .reset_index(name="Count") # converts the size() result back into a normal DataFrame, naming the count column "Count"
)

duplicate_clauses = duplicate_clauses[
    duplicate_clauses["Count"] > 1
]

print(duplicate_clauses.shape)

print(duplicate_clauses.head())

duplicate_clauses.to_csv(
    "output/duplicate_clauses.csv",
    index=False
)

print("Duplicate Clauses Saved")


# Audit #3: Version Mismatch

version_mismatches = publishing_loads[
    publishing_loads["Loaded_Version"]
    !=
    publishing_loads["Required_Clause_Version"]
]

print(version_mismatches.shape)

print(version_mismatches.head())

version_mismatches.to_csv(
    "output/version_mismatches.csv",
    index=False
)

print("Version Mismatches Saved")


# Audit Summary Table

audit_summary = pd.DataFrame({
    "Audit_Type": [
        "Missing Clause",
        "Duplicate Clause",
        "Version Mismatch"
    ],
    "Findings": [
        len(missing_clauses),
        len(duplicate_clauses),
        len(version_mismatches)
    ]
})

print(audit_summary)

audit_summary.to_csv(
    "output/audit_summary.csv",
    index=False
)

print("Audit Summary Saved")