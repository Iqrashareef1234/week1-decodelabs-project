def check_password_strength(password):
    """
    DecodeLabs Project 1 - Password Strength Checker
    No external modules used. Works on any online compiler.
    """
    
    if not password:
        return "Invalid", "Password cannot be empty"
    
    # Check for common weak passwords
    common = ['password', '123456', 'qwerty', 'admin', 'letmein', 'abc123']
    if password.lower() in common:
        return "Weak", "Password is too common and easily guessable"
    
    length = len(password)
    
    # Check character types manually - no regex needed
    has_upper = False
    has_lower = False
    has_digit = False
    has_symbol = False
    
    for ch in password:
        if 'A' <= ch <= 'Z':
            has_upper = True
        elif 'a' <= ch <= 'z':
            has_lower = True
        elif '0' <= ch <= '9':
            has_digit = True
        else:
            has_symbol = True
    
    score = 0
    feedback = []
    
    # Length scoring
    if length >= 12:
        score += 4
    elif length >= 8:
        score += 2
    elif length >= 6:
        score += 1
    else:
        feedback.append("Use at least 8 characters")
    
    if has_upper:
        score += 1
    else:
        feedback.append("Add uppercase letters")
    
    if has_lower:
        score += 1
    else:
        feedback.append("Add lowercase letters")
        
    if has_digit:
        score += 1
    else:
        feedback.append("Add numbers")
        
    if has_symbol:
        score += 2
    else:
        feedback.append("Add special characters like !@#$")
    
    # Final rating
    if score <= 3:
        strength = "Weak"
    elif score <= 6:
        strength = "Medium"
    else:
        strength = "Strong"
    
    message = "Password meets security baseline" if not feedback else "Suggestions: " + "; ".join(feedback)
    return strength, message

# Main program
print("="*50)
print("DecodeLabs - Password Strength Checker")
print("Project 1")
print("="*50)

while True:
    password = input("\nEnter password to check (or type 'exit' to quit): ")
    
    if password.lower() == 'exit':
        print("Exiting... Project complete!")
        break
    
    strength, feedback = check_password_strength(password)
    
    print(f"\nPassword Strength: {strength}")
    print(f"Feedback: {feedback}")
    print("-"*50)
