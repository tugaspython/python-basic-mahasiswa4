def validasi_password(password):
    if len(password) >= 8:
        if len(password) <= 20:
            if " " not in password:
                has_upper = False
                for char in password:
                    if char >= 'A':
                        if char <= 'Z':
                            has_upper = True
                            
                if has_upper:
                    has_digit = False
                    for char in password:
                        if char >= '0':
                            if char <= '9':
                                has_digit = True
                                
                    if has_digit:
                        has_symbol = False
                        for char in password:
                            if char in "!@#$%^&*":
                                has_symbol = True
                                
                        if has_symbol:
                            return True
    return False
