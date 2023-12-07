# TODO Найдите количество книг, которое можно разместить на дискете
available_space = 1.44
number_of_pages = 100
number_of_strings = 50
number_of_chars = 25
char_wheight = 4
book_weight = number_of_pages * number_of_strings * number_of_chars * char_wheight
book_wheight_mb = book_weight / 1024**2
str_answer = str(available_space // book_wheight_mb)
print("Количество книг, помещающихся на дискету:", str_answer[0])
