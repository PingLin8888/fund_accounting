how to automate? who executes? do we need review? configure file to take path etc?

If your Account column is numeric (float) vs string:
1000000.01 vs "1000000.01"

# QR: copy and paste 2 reports and check the commitments. lux one vs non-lux one. matter???

last row is total. so compare total first, if mismatch, compare each investor
compare commitment by ID.
color mismatches red.
management share, 1 or 25 etc, ridiciously small.
why this is often missed out in the RW report?

so i had this task. i first download 2 reports from a system, then i open an excel and copy and paste those 2 reports in 2 seperate tabs. there's a third tab in the excel that checks if the totoal commitment from these 2 reports match. basically the commitment figure from those 2 reports are the last row in a specific col(say col "commitment" and col "commitment"). if they don't match, i need to find out why but about the commitment check,
how could i automate it.

dashboards? how many reports finished?

# iXBRL: annual report goes to some categories in DPL excel. and template tab extract data from diff fund tabs.

# raise ticket like luis did to control that deal type has to match account sufix which indicates currency.

# how to compare commitment from share register and driver report

the end of cirtain col should match. how to grab the end of cirtain cols(formula vs python)

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

# May 10 2026

data reconciliation tool
simple reporting dashboard
API that processes financial data
automation tool for CSV/Excel ingestion

## Typical Python automation tasks:

clean CSV/Excel files
reconcile data between systems
generate reports
send emails / alerts
simple ETL (extract-transform-load)
