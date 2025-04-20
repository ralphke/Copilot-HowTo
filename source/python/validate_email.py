def validate_email(email):
    import re
    pattern = r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$'
    return re.match(pattern, email)

result = validate_email('Ralph.Kemperdick@RaKeTeTechnology.com')
print(result)