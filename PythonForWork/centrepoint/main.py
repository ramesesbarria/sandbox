from services.run_job import run_job


# Simply call run_job function 
# run_job(
#         json_path = "",
#         schema_path = "",
#         job_type = ""
# )
# job_types = create, modify, terminate

def main():
    run_job(
        json_path   = "source_files/createDataSource.json",
        schema_path = "templates/createSchema.csv",
        job_type    = "create"
    )
    run_job(
        json_path   = "source_files/modifyDataSource.json",
        schema_path = "templates/modifySchema.csv",
        job_type    = "modify"
    )
    run_job(
        json_path   = "source_files/terminateDataSource.json",
        schema_path = "templates/terminateSchema.csv",
        job_type    = "terminate"
    )

if __name__ == "__main__":
    main()