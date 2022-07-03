current_letter = input()
save_letter = ""
secret_letter_counter = 0
secret_counter_c = 0
secret_counter_o = 0
secret_counter_n = 0
counter_secret_reset = 0
invalid_letters = 0
while True:
    if current_letter == "End":
        break
    if current_letter == "c":
        secret_counter_c += 1
        if secret_counter_c > 1:
            save_letter += current_letter
        elif current_letter != "c":
            save_letter += current_letter
    elif current_letter == "o":
        secret_counter_o += 1
        if secret_counter_o > 1:
            save_letter += current_letter
        elif current_letter != "o":
            save_letter += current_letter
    elif current_letter == "n":
        secret_counter_n += 1
        if secret_counter_n > 1:
            save_letter += current_letter
        elif current_letter != "n":
            save_letter += current_letter
    elif not current_letter.isalpha():
        pass
    else:
        save_letter += current_letter
    if secret_counter_c > 0 and secret_counter_o > 0 and secret_counter_n > 0:
        counter_secret_reset += 1
        if counter_secret_reset >= 1:
            save_letter += " "
            print(save_letter, end='')
        secret_counter_o = 0
        secret_counter_c = 0
        secret_counter_n = 0
        save_letter = ""
    current_letter = input()
