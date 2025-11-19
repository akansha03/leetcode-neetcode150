"""
Frequency-based sliding window pattern:
- need map (constant)
- window map (dynamic)
- have counter (tracks satisfied unique chars)
- Expand: add to window, check if threshold crossed
- Shrink: check if threshold will break, remove from window
"""
