
### Requirements

It requires python3 and at least reportlab 3.5.30 library.

### Convert plain text to PDF from terminal

python3 convert.py txt_path/text_name.txt pdf_path/pdf_name.pdf
If pdf_name isn't specified then the text_name will be used as pdf_name.

### Manipulate text output manually

There are three categories of text manipulation: global, line, segment.
Every parameter must be between these signs: < >
After the < must have !# it will look like this: <!# >
Must contain a value if it is not a special option.
But the different categories could have different starting, see below.

### Global declaration

It must include a parameter name and a value to that parameter.
Should be at the top of the text and an empty line between the declaration and the actual text.
Has a little difference here, the ~ sign.

Example: <!#~parameter value>

This declaration impose the properties of the rest of the document.
This could be overridden by the line and segment declaration

### Line declaration

It must be declared at the beginning of the line.

It has special options:
   <!#title> - center the selected line
   <!#new_page> - writes everything to a new page after this is called

Example: <!#title> Text goes here!
         <!#font_color red> And here also!

This could be overridden by the segment declaration.

### Segment declaration

It must contain a closing tag <!#>
It'll look like this: <!#parameter value>Text here<!#>
Selects the text segment and apply options to it based on the parameter.

### All available parameters

Only line parameter:
    title - position the text to middle
    new_line - start new line

font_color - changes the text color
font_size - changes the font size
line_height - space between the lines
left - positioning horizontally
top - positioning vertically

### Automate text manipulation process (without parameters)

At the beginning of the text define the <!#auto> parameter to automate manipulation and
the working environment size in pixels withe the <!#size> parameters

It regards the spaces as text decorators.
If the text overextends then automatically splits the text.

### Restrictions

Only accepts ASCII.
