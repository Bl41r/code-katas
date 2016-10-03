# code-katas
- This repo holds solutions for the Code Wars katas which I have worked on.

This Branch features autocomplete, which is a callable class.

usage in ipython:
```
>>> from autocomplete import AutoCompleter
>>> vocabulary = ['fix', 'fax', 'fit', 'fist', 'full', 'finch', 'final', 'finial']
>>> complete_me = AutoCompleter(vocabulary, max_completions=4)
>>> complete_me('f')
['fix', 'fax', 'fit', 'fist']
>>> complete_me('fi')
['fix', 'fit', 'fist', 'finch']
>>> complete_me('fin')
['finch', 'final', 'finial']
>>> complete_me('finally')
[]
```

* Alternatively, instead of passing vocabulary as a list, it may also be a file
containing words.
