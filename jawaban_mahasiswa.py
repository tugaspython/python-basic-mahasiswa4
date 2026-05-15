def validasi_password(password):
    if len(password) >= 8:
        if len(password) <= 20:
            if " " not in password:
                has_upper = False
                for char in password:
                    if char.isupper():
                        has_upper = True
                
                if has_upper == True:
                    has_digit = False
                    for char in password:
                        # Pengecekan angka yang sangat boros logika
                        if char == '0' or char == '1' or char == '2' or char == '3' or char == '4':
                            has_digit = True
                        elif char == '5' or char == '6' or char == '7' or char == '8' or char == '9':
                            has_digit = True
                    
                    if has_digit == True:
                        has_symbol = False
                        for char in password:
                            # Pengecekan simbol yang sangat boros logika
                            if char == '!' or char == '@' or char == '#' or char == '$':
                                has_symbol = True
                            elif char == '%' or char == '^' or char == '&' or char == '*':
                                has_symbol = True
                        
                        if has_symbol == True:
                            return True
    return False
