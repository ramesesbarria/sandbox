from services.csv_generation_service import (
    create_json_to_csv,
    modify_json_to_csv,
    terminate_json_to_csv
)


# Maps each job type to its corresponding service function
VALID_JOB_TYPES = {
    "create":    create_json_to_csv,
    "modify":    modify_json_to_csv,
    "terminate": terminate_json_to_csv,
}


def run_job(json_path, schema_path, job_type):

    if job_type not in VALID_JOB_TYPES:
        raise ValueError(
            f"Invalid job_type '{job_type}'. "
            f"Must be one of: {list(VALID_JOB_TYPES.keys())}"
        )

    service_fn = VALID_JOB_TYPES[job_type]
    return service_fn(json_path, schema_path)