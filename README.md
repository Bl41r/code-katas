# code-katas
- This repo holds solutions for the Code Wars katas which I have worked on.
- Be warned, this repo contains some downright ugly katas.  Hacky algo's, bad indentation, it's all here.  Many of these, I worked on before I began formally taking coding classes.

## Summaries

### Proper Parenthetics
- proper-parenthetics.py has a function proper_parenthetics(str) which takes a string containing parenthesis, and returns 1 if open, -1 if closed, and 0 if balanced.
- usage in ipython3:
```
%run proper-parenthetics.py
proper_parenthetics('(())()')
```

### Sum of the first nth term of a series
- Sum-of-the-first-nth-term-of-Series.py has a function series_sum(n) which returns the sum of following series up to nth term(parameter).
- Series: 1 + 1/4 + 1/7 + 1/10 + 1/13 + 1/16 +...
- usage in ipython3:
```
%run Sum-of-the-first-nth-term-of-Series.py
series_sum(5)
```
#### Rules:
- Round the answer up to 2 decimal places and return it as String.
- If the given value is 0 then it should return 0.00
- Will only be given Natural Numbers as arguments.
