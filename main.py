import os

def search_in_files(directory, query):
    matches = []
    for filename in os.listdir(directory):
        if filename.endswith('.txt'):
            filepath = os.path.join(directory, filename)
            with open(filepath, 'r', encoding='utf-8') as file:
                lines = file.readlines()
                for line in lines:
                    if query in line:
                        matches.append((filename, line.strip()))
    return matches

def main():
    directory = 'path_to_your_directory'  # Replace with the path to your directory
    query = 'your_query_here'  # Replace with your search query
    
    results = search_in_files(directory, query)
    
    if results:
        print(f"Found {len(results)} matches for '{query}':")
        for filename, line in results:
            print(f"In file {filename}: {line}")
    else:
        print(f"No matches found for '{query}'.")

if __name__ == "__main__":
    main()

