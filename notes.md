how to automate? who executes? do we need review? configure file to take path etc?

If your Account column is numeric (float) vs string:
1000000.01 vs "1000000.01"

# check gl booking weekly

there's an excel file which is exported from a system.
we do a weekly check of it. one of them is

## currency check:

if col of currrency is USD, col of account should end with .01
if EUR, account should end with .02
if CHF, account should end with .13

comment + transacton type should match with account?

this doesn't match the deal type??

### later

Highlight errors (using openpyxl)
Send email automatically with issues
Turn it into a reusable script for all checks
Add more rules (e.g. account length, null checks, duplicates)

# filter dublin funds pmi invoices

exported pmi invoices(xlsx), another xlsx file contains all the legal entities that are dublin funds.

# Evelin calls & dists

copy and paste calls and dists data into word

# mmif

copy and paste

sum up and paste

# nav packs

## track nav processes

bnp zip file

every time the systems that are involved update, check if file extention changes. eg xlsx to xls.

You could extend it:

Add date to filename
Automatically find latest files
Move zip to shared folder
Add logging

windows os vs mac os

Windows → folder\file.xlsx
Mac/Linux → folder/file.xlsx
