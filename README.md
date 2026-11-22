# meal-planner

A personal recipe manager and weekly meal planner, built in Python.

Planning meals for the week is tedious, especially when you want them to be
quick, healthy and high in protein. This project stores your recipes in a
structured way and does the planning for you: pick your rules, get a weekly
plan and a matching shopping list.

## Features

- **Recipe storage** with ingredient quantities, nutrition values,
  preparation time and difficulty
- **Automatic nutrition calculation** per portion, based on per-ingredient data
- **Weekly meal planner** with configurable rules, e.g. two quick, high-protein
  recipes per weekday and more elaborate dishes on weekends
- **Shopping list generation** that combines ingredients across all planned recipes
- **Search and filtering** by tags, time, calories and protein

## Status

Early development. The project starts as a command-line tool with
JSON-based storage.

## Roadmap

- [ ] Data model: ingredients, recipes, nutrition calculation
- [ ] JSON persistence
- [ ] Command-line interface
- [ ] Shopping list generation
- [ ] Weekly meal planner
- [ ] SQLite storage
- [ ] Web interface (mobile-friendly)