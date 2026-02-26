import json
import os
from utilities.util import (
    get_response,
    build_answer_lookup,
    build_output_path,
    fill_and_write_csv
)


def create_json_to_csv(json_path, schema_path):

    with open(json_path, "r", encoding="utf-8") as f:
        json_data = json.load(f)

    response      = get_response(json_data)
    answer_lookup = build_answer_lookup(response)
    output_path   = build_output_path("create", answer_lookup, "output/create")

    fill_and_write_csv(schema_path, output_path, answer_lookup)

    absolute_path = os.path.abspath(output_path)
    print(f"Create CSV saved to: {absolute_path}")
    return absolute_path


def modify_json_to_csv(json_path, schema_path):

    with open(json_path, "r", encoding="utf-8") as f:
        json_data = json.load(f)

    response      = get_response(json_data)
    answer_lookup = build_answer_lookup(response)
    output_path   = build_output_path("modify", answer_lookup, "output/modify")

    fill_and_write_csv(schema_path, output_path, answer_lookup)

    absolute_path = os.path.abspath(output_path)
    print(f"Modify CSV saved to: {absolute_path}")
    return absolute_path


def terminate_json_to_csv(json_path, schema_path):

    with open(json_path, "r", encoding="utf-8") as f:
        json_data = json.load(f)

    response      = get_response(json_data)
    answer_lookup = build_answer_lookup(response)
    output_path   = build_output_path("terminate", answer_lookup, "output/terminate")

    fill_and_write_csv(schema_path, output_path, answer_lookup)

    absolute_path = os.path.abspath(output_path)
    print(f"Terminate CSV saved to: {absolute_path}")
    return absolute_path