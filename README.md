# NoClearPick

NoClearPick is a terminal selection menu creator heavily inspired by Pick, with the main difference being that NoClearPick does not clear your terminal.

![](image.gif)

## Usage

Code:

```python
from NoClearPick import noclearpick

option, index = noclearpick(
        options = ["Hello, World!", "Howdy!", "Bonjour", "Hey", "Greetings earthling", "Guten Tag!"],
        title = "Pick the best greeting (use arrow keys to select and enter to pick):",
        indicator = "=>",
        default_index = 0
        )
print(option)
print(index)
```

Output:

```python
Pick the best greeting (use arrow keys to select and enter to pick):
 => Hello, World!
    Howdy!
    Bonjour
    Hey
    Greetings earthling
    Guten Tag!
Hello, World!
0
```

Install dependency:

```python
pip install get-key
```

## Options

*   `options`: a list of options to choose from
*   `title`: (optional) a title above options list
*   `indicator`: (optional) custom the selection indicator, defaults to \*
*   `default_index`: (optional) set this if the default selected option is not the first one