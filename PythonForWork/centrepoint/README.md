# XPlan User Changes — CSV Generation Service
## Documentation

---

## Overview

This tool automates the generation of structured CSV output files from Snapforms JSON submissions. It supports three job types — **Create**, **Modify**, and **Terminate** — each corresponding to an XPlan user action. The output CSVs are pre-filled with data from the JSON and follow a fixed schema template.

---

## Project Structure

```
project/
│
├── main.py                          # Entry point — runs all three jobs
│
├── source_files/
│   ├── createDataSource.json        # Raw JSON input for Create jobs
│   ├── modifyDataSource.json        # Raw JSON input for Modify jobs
│   └── terminateDataSource.json     # Raw JSON input for Terminate jobs
│
├── templates/
│   ├── createSchema.csv             # CSV template for Create output
│   ├── modifySchema.csv             # CSV template for Modify output
│   └── terminateSchema.csv          # CSV template for Terminate output
│
├── output/
│   ├── create/                      # Generated Create CSVs land here
│   ├── modify/                      # Generated Modify CSVs land here
│   └── terminate/                   # Generated Terminate CSVs land here
│
├── services/
│   ├── run_job.py                   # Validates job type and routes to correct service function
│   └── csv_generation_service.py   # Contains create/modify/terminate logic
│
└── utilities/
    └── util.py                      # Low-level helper functions
```

---

## How It Works

The flow from input to output follows this chain:

```
main.py  →  run_job.py  →  csv_generation_service.py  →  util.py
```

1. `main.py` calls `run_job()` with a JSON path, schema path, and job type.
2. `run_job.py` validates the job type and routes to the correct function in `csv_generation_service.py`.
3. The service function loads the JSON, extracts the answers, and writes a filled CSV based on the schema template.
4. `util.py` handles all the low-level work: parsing the JSON, building the answer lookup, constructing the output path, and writing the CSV.

---

## Running the Tool

### Run all three jobs at once

```bash
python main.py
```

This will process all three JSON source files and generate one output CSV per job in their respective output folders.

### Run a single job manually

You can call `run_job()` directly in your own script:

```python
from services.run_job import run_job

run_job(
    json_path   = "source_files/createDataSource.json",
    schema_path = "templates/createSchema.csv",
    job_type    = "create"
)
```

Valid values for `job_type` are: `"create"`, `"modify"`, `"terminate"`.

---

## Output Files

Generated CSVs are saved to `output/<job_type>/` and named using the following convention:

```
{job_type}_{contactname}_{response_id}.csv
```

**Examples:**
```
output/create/create_testcontactname_31061350.csv
output/modify/modify_emilywright_29790012.csv
output/terminate/terminate_sarahcollins_29790065.csv
```

The `response_id` in the filename ensures that multiple submissions from the same contact never overwrite each other.

---

## Schema Templates

The schema CSV files in `templates/` define the structure of the output. Each row follows this column layout:

| Column 0 | Column 1 | Column 2 | Column 3 |
|---|---|---|---|
| Question key | Field type | Display label | `<answer>` or static value |

- **Column 0** is the lookup key — it must exactly match the `"question"` field in the source JSON for the answer to be filled in.
- **Column 3** uses the placeholder `<answer>` to indicate where a value should be injected. Rows without `<answer>` are written as-is (e.g. section headers, blank spacer rows).

### Example schema row:
```
Form_Contact_Name,short_answer,Contact Name *,<answer>
```
When processed, this becomes:
```
Form_Contact_Name,short_answer,Contact Name *,Emily Wright
```

### Adding a new field to a schema

1. Open the relevant schema file in `templates/`.
2. Add a new row in the format: `Question Key,field_type,Display Label,<answer>`
3. Ensure the Question Key exactly matches the `"question"` value in the source JSON (case-sensitive).
4. The answer will be automatically filled on the next run.

### Adding a static/header row (no answer needed)

Leave column 3 empty or put any value other than `<answer>`:
```
,,Section Header,
```

---

## Source JSON Format

The tool supports two JSON structures from Snapforms:

**Wrapped format** (e.g. `createDataSource.json`):
```json
{
  "name": "...",
  "responses": [
    {
      "response_id": 12345,
      "datetime": "2026-02-11 18:35:34",
      "answers": [
        { "question": "First Name", "type": "short_answer", "answer": "John" }
      ]
    }
  ]
}
```

**Bare format** (e.g. `modifyDataSource.json`):
```json
{
  "response_id": 12345,
  "datetime": "2025-12-19 18:45:49",
  "answers": [
    { "question": "User name", "type": "short_answer", "answer": "jsmith" }
  ]
}
```

Both are handled automatically by `get_response()` in `util.py`.

---

## Adding a New Job Type

If a fourth job type is ever needed (e.g. `"reactivate"`):

**1. Add the service function in `csv_generation_service.py`:**
```python
def reactivate_json_to_csv(json_path, schema_path):

    with open(json_path, "r", encoding="utf-8") as f:
        json_data = json.load(f)

    response      = get_response(json_data)
    answer_lookup = build_answer_lookup(response)
    output_path   = build_output_path("reactivate", answer_lookup, "output/reactivate")

    fill_and_write_csv(schema_path, output_path, answer_lookup)

    absolute_path = os.path.abspath(output_path)
    print(f"Reactivate CSV saved to: {absolute_path}")
    return absolute_path
```

**2. Register it in `run_job.py`:**
```python
from services.csv_generation_service import (
    create_json_to_csv,
    modify_json_to_csv,
    terminate_json_to_csv,
    reactivate_json_to_csv       # add this
)

VALID_JOB_TYPES = {
    "create":     create_json_to_csv,
    "modify":     modify_json_to_csv,
    "terminate":  terminate_json_to_csv,
    "reactivate": reactivate_json_to_csv,   # add this
}
```

**3. Create the schema template** at `templates/reactivateSchema.csv` following the same column structure as the existing schemas.

**4. Create the output folder** at `output/reactivate/`.

**5. Call it from `main.py`:**
```python
run_job(
    json_path   = "source_files/reactivateDataSource.json",
    schema_path = "templates/reactivateSchema.csv",
    job_type    = "reactivate"
)
```

---

## File Reference

| File | Purpose |
|---|---|
| `main.py` | Entry point. Edit this to add, remove, or change which jobs run. |
| `services/run_job.py` | Validates job type and routes to the correct service function. Edit this when adding new job types. |
| `services/csv_generation_service.py` | One function per job type. Each loads JSON, builds the lookup, and writes the CSV. |
| `utilities/util.py` | Core helpers shared across all job types. Rarely needs editing. |
| `templates/*.csv` | Schema templates that define output structure. Edit these to add/remove fields. |
| `source_files/*.json` | Input data from Snapforms. Replace with new submissions as needed. |
| `output/` | Where all generated CSVs are saved. |