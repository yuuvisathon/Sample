from queryy import get_object_yuuvis, get_data_yuuvis
from parser import parse_machine


def main():
    machine_id = "Apple"
    data_type = "Blah"
    blob_data = get_object_yuuvis(machine_id, data_type)
    file_data = get_data_yuuvis(blob_data).text
    print(parse_machine(machine_id, file_data))


if __name__ == "__main__":
    main()

