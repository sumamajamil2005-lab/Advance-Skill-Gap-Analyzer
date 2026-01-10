from pathlib import Path

def file_loader(filepath):
    """
    Simplified & Robust Loader: 
    Reads the entire file content. This avoids splitting errors that 
    cause skills like 'Machine Learning' to be missed.
    """
    my_path = Path(filepath)
    if not my_path.exists() or not my_path.is_file():
        print("Invalid file Path. ")
        return []
    
    try:
        with open(my_path , "r" , encoding="utf-8") as f:
            content = f.read().splitlines()
            clean_content = [raw_content.strip().lower() for raw_content in content if raw_content.strip()]
            return clean_content
    except Exception as e:
        print(f"Error : {e}")
        return []