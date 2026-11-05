# Lecture 02 problem: Nobel prize data explorer

The file `nobel.csv` contains Nobel Prize records. Build a small data explorer that reads the data, runs useful queries, and stores the result as JSON.

## 1. Build the Nobel dataset

### 1.1 Construct the data

Implement a function named `build_noble_data(csvfile)`.

- Read the CSV using `csv.reader`.
- Return a list of dictionaries.
- Each dictionary must have these keys:
  `name`, `sex`, `award`, `date`, `time`, and `country`.
- Extract the date and time separately from the CSV timestamp column.

### 1.2 Verify the construction

Load `nobel.csv` by calling your function. Add assertions that ensure:

- The returned value is a non-empty list.
- Every item is a dictionary with exactly the expected keys.
- Every person has a non-empty `name`.

## 2. Query the dataset

### 2.1 Filter by country

Use a list comprehension to create `swedish_nobel`, containing only people
whose country is `"Sweden"`.

- Assert that every result is from Sweden.
- Print the number of Swedish recipients.

### 2.2 Find unique countries

Use a set comprehension to create `countries`, containing every unique country
in the data. Print the number of unique countries.

### 2.3 Search by name

Ask the user for a name search term. Use a case-insensitive list comprehension
to find matching people. For every match, print the person's name, award, and
country.

Your program must handle searches with no matches.

### 2.4 Verify query results

- Count the Swedish recipients without using `len(swedish_nobel)`.
- Assert that your count equals `len(swedish_nobel)`.

## 3. Store and verify the dataset

### 3.1 Store the data

Write the full list to `nobel.json` with UTF-8 encoding, `ensure_ascii=False`,
and indentation.

### 3.2 Verify the stored data

Read the file back with `json.load` and assert that the loaded value equals the
original list.

## Constraints

- Use only the Python standard library.
- Do not use `pandas`.
- Use `csv`, list comprehensions, set comprehensions, assertions, and `json`.
- Keep file access inside `with open(...)` blocks.
