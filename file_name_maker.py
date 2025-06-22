import secrets
import string
from pathlib import Path




def generate_secure_random_string(length=16, chars=string.ascii_letters + string.digits):
    return ''.join(secrets.choice(chars) for _ in range(length))


def file_name(file, link):
    dynamic_name = generate_secure_random_string(20)
    static_name = file.filename
    child_path = static_name + '_' + dynamic_name
    nested_directory_path = Path(f'\A2A-main\load_files\{child_path}')

    try:
        nested_directory_path.mkdir(parents=True, exist_ok=True)
        print(f"Directory '{nested_directory_path}' created successfully.")
    except OSError as e:
        print(f"Error creating directory: {e}")

