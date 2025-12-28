def File_Loader(FilePath):
    """
    Simplified & Robust Loader: 
    Reads the entire file content. This avoids splitting errors that 
    cause skills like 'Machine Learning' to be missed.
    """
    try:
        with open(FilePath, "r", encoding="utf-8") as f:
            content = f.read().splitlines()
            cleaned_content = [line.strip().lower() for line in content if line.strip()]   
            return cleaned_content
            
    except FileNotFoundError:
        print(f"Error: The file at {FilePath} was not found.")
        return []
    except Exception as e:
        print(f"Error reading file: {e}")
        return []