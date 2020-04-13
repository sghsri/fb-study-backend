import json


def get_sample_of_field(field):
    with open("sample_data/sample.json") as json_file:
        return json.load(json_file)[field]


def write_sample_of_field(field, data):
    with open("sample_data/sample.json", "r+") as json_file:
        sample = json.load(json_file)
        sample[field].append(data)
        json_file.seek(0)
        json_file.write(json.dumps(sample))
        json_file.truncate()
        return data


class sample_db:
    @staticmethod
    def read_jobs():
        return get_sample_of_field("company_data")

    @staticmethod
    def write_jobs(data):
        return write_sample_of_field("company_data", data)


def validate_input(input):
    return True
