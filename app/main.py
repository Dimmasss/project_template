import app.io.input as input_implementation
import app.io.output as output_implementation_


def main():
    text_input_from_console = input_implementation.text_input_from_console()
    text_from_file = input_implementation.read_from_file_by_built_in_func("../data/input.txt")
    text_from_file_for_pandas = input_implementation.read_from_file_by_pandas("../data/data.csv")

    output_implementation_.output_to_console(text_input_from_console)
    output_implementation_.output_to_console(text_from_file)
    output_implementation_.output_to_console(text_from_file_for_pandas)

    output_implementation_.write_to_file_by_built_in_func(text_from_file, "../data/output.txt")


if __name__ == "__main__":
    main()
