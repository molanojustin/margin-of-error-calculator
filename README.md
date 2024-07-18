# Margin of Error Calculator

This is a simple script that calculates the overall margin of error assuming a 95% confidence interval and a proportion percentage of 0.5. Both can be altered when calling the function.

This will also export to a csv, but a formatted xlsx with the default settings is included in the repo.

The output includes margin of errors for every sample size 40 and above at a multiple of 5 until 400 after which the multiple is changed to 10 until 2000 is reached.

To run:
- Open `moeFun.py`
- Define z-score depending on desired confidence level.
- Define p depending on proportion percentage.
- Update the range and multiples to include.
- Run `moeFun.py`