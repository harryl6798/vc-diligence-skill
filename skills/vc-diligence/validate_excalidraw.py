import json
import sys

def validate(file_path):
    with open(file_path, 'r') as f:
        data = json.load(f)
    
    elements = data.get('elements', [])
    for i, el in enumerate(elements):
        el_type = el.get('type')
        el_id = el.get('id', f'index_{i}')
        
        # Check required arrays
        if not isinstance(el.get('groupIds'), list):
            print(f"ERROR: {el_id} ({el_type}) groupIds is not a list")
        
        if el.get('boundElements') is not None and not isinstance(el.get('boundElements'), list):
            print(f"ERROR: {el_id} ({el_type}) boundElements is not a list or null")
            
        # Check for mandatory properties
        required = ['seed', 'version', 'versionNonce', 'isDeleted', 'index']
        for prop in required:
            if prop not in el:
                print(f"ERROR: {el_id} ({el_type}) missing {prop}")

    print("Basic validation complete.")

if __name__ == "__main__":
    validate(sys.argv[1])
