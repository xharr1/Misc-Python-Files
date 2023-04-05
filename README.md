# Misc-Python-Files
Python files created at prior employer to automate day to day tasks

Most of this code was pulled from stack overflow (and possibly other sources) and edited for use in specific tasks.

CombineLetters.py and BatchPDFs.py were used together when our main letter creation system broke down. I was able to research, copy, and modify code from the internet and get the letters out within the mandated timeframe. A Microsoft Word mail merge would create the unique pages of the letters (it would slow down greatly if all pages were included), CombineLetters.py would combine those unique pages with the pages that were the same in every letter, and BatchPDFs.py would batch 200 pdfs into 1 for our print vendor.

"Combine pdfs (Check Requests).py" is a variant of CombineLetters.py. It would combine check request pdfs and the necessary backup pdfs into one file for accounting.
