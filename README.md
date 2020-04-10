# Scrapers

This is a repository for all the scrapers I've learnt to write!

I'm using Python 3.7.5 for this project.

## User Guide

### Table Scraper
This script scrapes all rows in a table without pagination. It also assumes the following table structure

```html
<table>
    <thead>
        <tr>
            <th>Header A</th>
            <th>Header B</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Cell A1</td>
            <td>Cell B1</td>
        </tr>
        <tr>
            <td>Cell A2</td>
            <td>Cell B2</td>
        </tr>
    </tbody>
</table>
```
where rows are enumerated by numbers (1, 2, ...) and columns are enumerated by alphabets (A, B, ...).

To run, do

```python
python table_scraper.py "url1" "url2"

e.g.
python table_scraper.py "https://some-website-with-a-table.com/table"
```

You can input as many urls as you want, each as a separate program argument.

Results will be output to a CSV file.