# Quiz 1: Django ORM

## Q1

Which statement is true:

A. Django provides a layer betwen app and database.
B. Django has an inbuilt database.
C. Django only works with a specific database.
D. Django requires a database to be configured.

## Q2

When using Django, database updates can be made:

A. via the Django shell
B. in the application code
C. using raw SQL
D. in an external GUI tool
E. any of the above

## Q3

Consider this data linked to the Django model `Movie`:

| id  | title                  | year | rating | genre  |
| --- | ---------------------- | ---- | ------ | ------ |
| 24  | The Matrix             | 1999 | 5      | action |
| 910 | Star Wars IV           | 1977 | 4      | sci-fi |
| 46  | The Matrix Reloaded    | 2003 | 4      | action |
| 3   | 2001: A Space Odyssey  | 1968 | 5      | sci-fi |
| 51  | The Matrix Revolutions | 2003 | 3      | action |

How many results will the following query give?

```python
Movie.objects.filter(rating__lt=5, genre="action")
```
