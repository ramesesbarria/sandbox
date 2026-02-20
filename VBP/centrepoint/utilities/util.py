import csv
import os


def get_response(json_data):
 
    if "responses" in json_data:
        return json_data["responses"][0]
    else:
        return json_data


def build_answer_lookup(response):
   
    lookup = {}

    for item in response["answers"]:
        lookup[item["question"]] = item["answer"]

    lookup["response_id"] = str(response["response_id"])
    lookup["datetime"]    = response["datetime"]

    return lookup


def build_output_path(action_type, answer_lookup, output_dir):
   
    contact_name = answer_lookup.get("Form_Contact_Name", "unknown")
    contact_name = contact_name.lower().replace(" ", "")

    response_id = answer_lookup.get("response_id", "unknown")

    filename = f"{action_type}_{contact_name}_{response_id}.csv"

    return os.path.join(output_dir, filename)


def fill_and_write_csv(schema_path, output_path, answer_lookup):
   
    with open(schema_path, "r", newline="", encoding="utf-8") as template_file, \
         open(output_path, "w", newline="", encoding="utf-8") as output_file:

        reader = csv.reader(template_file)
        writer = csv.writer(output_file)

        for row in reader:

            while len(row) < 4:
                row.append("")

            question_key = row[0]
            placeholder  = row[3]

            if placeholder == "<answer>":
                row[3] = answer_lookup.get(question_key, "")

            writer.writerow(row)