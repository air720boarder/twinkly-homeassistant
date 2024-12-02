#!/bin/bash

# Remove all __pycache__ directories
find . -type d -name "__pycache__" -exec rm -r {} +

# Remove pytest cache
rm -rf .pytest_cache

# Run tests with coverage
pytest -v --cov=custom_components.twinkly --cov-report=term-missing 