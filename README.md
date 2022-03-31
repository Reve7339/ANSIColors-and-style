# ANSI escape code - SGR (Select Graphic Rendition) parameters

If you want to add color to your terminal output, the use of ANSI escape codes may be the best way to go.

### Initialization

First we need to initialize the scape code.

Originally it is like this: `ESC + [` but in our code we will use ` \ ` and the ASCII code of `ESC`.

So in our code it will look like this: `\x1b[` Note that `x1b` is in hexadecimal, but it can also be octal `033` or unicode `u001b`.

Then we have these three forms to initialize an escape code: `\x1b[` `\033[` `\u001b[`.

### Style

Depending on your terminal some styles and colors may or may not work. [Here we have a list of all styles.](https://en.wikipedia.org/wiki/ANSI_escape_code#SGR) (Note that 30-49 are reserved for colors).

The way to use styles is: `ESC + [` + `style`+`m`.

The last `m` character is just to tell our code that we are finishing the scape code.

In our code it looks like this: `\x1b[1m` (1 is for bold the text).

### Colors

Several attributes can be set in the same sequence, separated by semicolons. Colors can be used with styles or alone.

There are 3 ways to set the colors on our outputs depending on the terminal support. These are: 3-bit and 4-bit, 8-bit, and 24-bit.

#### 3-bit and 4-bit

The range [30-37] is for the text and the range [40-47] is for the background, we concatenate it with semicolons, so we have this in our code: `\x1b[35;42m` (35 is for magenta and 42 for green)

In the previous example we did not use style, so adding style to our code it looks like this: `\x1b[1;35;42m` (Order doesn't matter, so we can interchange the numbers separated by semicolons)

#### 8-bit

This is a little more complex, instead of using a single number to represent we will use a block of three numbers, but we will obtain a wider variety of colors. This block of three numbers cannot be interchanged and each comes strictly after the other.

For the foreground: `38;5;<n>`

For the background: `48;5;<n>`

`n` is what we will use to set the color and his range is [0-255]:

    0-7:  standard colors (as in ESC [ 30–37 m)

    8-15:  high intensity colors (as in ESC [ 90–97 m)

    16-231:  6 × 6 × 6 cube (216 colors): 16 + 36 × r + 6 × g + b (0 ≤ r, g, b ≤ 5)

    232-255:  grayscale from black to white in 24 steps

Now we have something like this: `\x1b[38;5;200m` for foreground and `\x1b[48;5;6m` for background

Mixing them looks like this: `\x1b[38;5;200;48;5;6m` and adding the style looks like this: `\x1b[1;38;5;200;48;5;6m`

You can interchange them but never forget that the sequence of three numbers for the background and foreground are strictly like we presented them.

#### 24-bit

This uses RGB to represent a color, the syntax looks like this: `38;2;⟨r⟩;⟨g⟩;⟨b⟩` for the foreground and `48;2;⟨r⟩;⟨g⟩;⟨b⟩` for the background (Note that we use `2` instead of `5` like before). You can search in your browser for a specific RGB code. As well as 8-bit color the order of these 5 numbers is strictly as I showed you.

Now in our code we have the following: `\x1b[38;2;0;0;255m` for the foreground and `\x1b[48;2;255;0;0m` for the background, mixing them we have `\x1b[38;2;0;0;255;48;2;255;0;0m`. If you want to add style, our code will be `\x1b[1;38;2;0;0;255;48;2;255;0;0m`

### Reset

Everything we have done is permanent until we reset or change it. We can reset all (colors and styles) using the following `\x1b[0m`.