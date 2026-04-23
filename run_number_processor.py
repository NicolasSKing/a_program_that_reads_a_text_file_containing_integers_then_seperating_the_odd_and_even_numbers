from a_program_that_reads_a_text_file_containing_integers_then_separating_the_odd_and_even_numbers import NumberProcessor

processor = NumberProcessor("numbers.txt")
processor.read_numbers()
processor.separate_numbers()
processor.making_files()

print("Done! Check even.txt and odd.txt") 