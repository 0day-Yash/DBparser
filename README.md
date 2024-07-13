# Email Hash Parser and Search Tool

This tool helps you parse through hundreds of text files filled with email hashes and search for a specific query across all of them.

## Step-by-Step Instructions

### Step 1: Organize Your Files

Make sure all your `.txt` files are in a single directory. This will make it easier for the script to access and parse them.

### Step 2: Use the Script

The provided Python script will read all `.txt` files in the specified directory and search for a specific query within these files.

### Prerequisites

- Python 3.x installed on your system.

### Installation

1. **Download Python**: If you don't have Python installed, download it from the [official Python website](https://www.python.org/downloads/).

### Usage

1. **Save the Script**: Save the following script in the parent directory

2. **Modify the Script**:
    - Replace `'path_to_your_directory'` with the actual path where your `.txt` files are stored.
    - Replace `'your_query_here'` with the query you want to search for.

3. **Run the Script**:
    - Open a terminal or command prompt.
    - Navigate to the directory where you saved the script.
    - Run the script using the following command:
    
    ```sh
    python search_email_hashes.py
    ```

## Example

Suppose your `.txt` files are located in `/home/user/email_hashes/`, and you want to search for the query `example@example.com`. You would modify the script as follows:

```python
def main():
    directory = '/home/user/email_hashes'  # Path to your directory
    query = 'example@example.com'  # Your search query
```

Then run the script:

```sh
python search_email_hashes.py
```

### Output

The script will output the matches found along with the filenames where the query was found.

```sh
Found 3 matches for 'example@example.com':
In file file1.txt: example@example.com
In file file2.txt: example@example.com
In file file3.txt: example@example.com
```

If no matches are found, it will display:

```sh
No matches found for 'example@example.com'.
```

## Notes

- Ensure your text files are encoded in UTF-8 to avoid encoding issues.
- The script only searches for exact matches. For partial matches or regular expressions, the script can be modified accordingly.


### MADE BY YASH KULKARNI; a.k.a. PurpleRain
```sh

########  ##     ## ########  ########  ##       ######## ########     ###    #### ##    ## 
##     ## ##     ## ##     ## ##     ## ##       ##       ##     ##   ## ##    ##  ###   ## 
##     ## ##     ## ##     ## ##     ## ##       ##       ##     ##  ##   ##   ##  ####  ## 
########  ##     ## ########  ########  ##       ######   ########  ##     ##  ##  ## ## ## 
##        ##     ## ##   ##   ##        ##       ##       ##   ##   #########  ##  ##  #### 
##        ##     ## ##    ##  ##        ##       ##       ##    ##  ##     ##  ##  ##   ### 
##         #######  ##     ## ##        ######## ######## ##     ## ##     ## #### ##    ## 

