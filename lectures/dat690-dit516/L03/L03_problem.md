## Lecture 3 problem: Validate and structure Nobel Prize dates

The `nobel.csv` file contains Nobel Prize laureate records. Each record has an award date in the `date` column, normally written as an ISO-style timestamp:

```text
2009-01-01T00:00:00Z
```

The file also contains deliberately malformed dates. Write a program that
uses regular expressions to identify valid date values and extract their
components.

### Requirements

1. Read `nobel.csv` with Python's `csv` module and build a
   dictionary-of-dictionaries keyed by the laureate's name. Each record must include the laureate's name, prize, award date, country, and city.
2. Create one regular expression for the complete award timestamp. It must:
   - require a four-digit year from 1900 through 2299;
   - accept a month from `01` through `12`;
   - accept a day from `01` through `31`;
   - accept either `-` or `/` between the date components;
   - require `T`, an `HH:MM:SS` time, and a final `Z`.
3. Use named capture groups for `year`, `month`, `day`, and `time`.
4. Validate every record with `re.fullmatch`. For every valid date, add a
   nested `date` dictionary containing the values returned by
   `match.groupdict()`.
5. Collect invalid records in a separate list. For each invalid record, keep the laureate's name and original award-date value, then print a clear
   validation report.
6. Add assertions that demonstrate the regex behavior:
   - a known valid timestamp matches;
   - an invalid month such as `1915-13-01T00:00:00Z` does not match;
   - an invalid day such as `1937-01-32T00:00:00Z` does not match;
   - the parsed dictionary contains the expected named keys.
7. Write the valid Nobel dictionary to JSON. The nested `date` dictionary
   must be present in the JSON output.

### Example output

```text
Valid records: <number>
Invalid records:
- <laureate name>: <invalid award date>
- <laureate name>: <invalid award date>
```

The number and exact content of invalid records depend on the input file.

### Consider

- Why is `re.fullmatch` more appropriate than `re.match` for validation?
- Which groups need to be capturing groups, and which can be non-capturing
  groups?
- Why should the CSV be parsed with `csv.reader` rather than one large regular expression?
- Which date errors can this regex detect, and which require a date library?
  For example, `2023-02-31` has valid numeric ranges but is not a calendar
  date.
