# generalized-titles
Generate some j a z z titles for j a z z pieces.

Jazz pieces have some pretty cool names such as "Along came Betty" that have a part that you can easily generalize: "Along came {name}".

## Sources
- UCI Machine Learning Repository: Gender by Name Data Set
  - https://archive.ics.uci.edu/ml/datasets/Gender+by+Name
- color names
  - https://hexcolor.co/color-names
- world cities
  - https://simplemaps.com/data/world-cities
    - https://creativecommons.org/licenses/by/4.0/
- english adjectives and nouns
  - https://gist.github.com/hugsy/8910dc78d208e40de42deb29e62df913

## Useage

Generate 50 jazz titles:
```python generalize.py rules/jazz-titles 50```
Run this script in a directory with the needed `data` directory (if you use the script for custom data).

## How it works

### Data

First you have a directory called `data`.
Put the list of words that will be used to substitute in text files ending with `.sub`.
You can use sub directories and the recursive structure will be respected by the script.
When making rules for example, you could use `month` as a substitute as it is present: `month.sub`.
But you could also use the directory: `time` would randomly pick a substitution file from it's recursive structure and than randomly pick a word.

```
data
├── adjective.sub
├── colour.sub
├── letter.sub
├── name
│   ├── female.sub
│   └── male.sub
├── noun.sub
├── place
│   └── city.sub
└── time
    ├── day-section.sub
    ├── day.sub
    ├── month.sub
    └── season.sub
```

### Rules

Rules can be put in any old text file, as you give it as an argument.
An example of a rule is `Along Came {Betty,name}`.
It's just the sentence with an `{}` field, where the substitution happens.
The first field is the original word you are substituting for, here it's `Betty`.
The second field is the data category you want to substitute from, here it's `name`.
There are two extra field you can put after that, which are optional.
The first is a single letter field, indicating that you want the substituted word needs to start with that letter(not case sensitive):
`Blues in {Frankie,name,f}’s Flat`.
The second field is `unique`, meaning you want all substituted fields to be unique:
`{Blue,colour} in {Green,colour,unique}`.

## existing titles that could still be generalized

Could generalize: me, you, them, us, etc. But there are not many items to generalize with.
- But not for me
- Could It Be You
- I Like The Likes Of You

Could generalize but the combinations don't produce many variants.
- June In January
- September Song

## License

```
Copyright (C) 2022 Cody Bloemhard

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
```
