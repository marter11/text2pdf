
### Requirements

It requires python3 and at least reportlab 3.5.30 library.

### Convert plain text to PDF from shell

python3 convert.py txt_path/text_name.txt pdf_path/pdf_name.pdf
If pdf_name isn't specified then the text_name will be used as pdf_name.

### Use as a module

If you want to use it as a module you should call the

### Manipulate text output

If you want to declear properties globally do it in the top of the document and after you've done
separate them with an empty line.
Every global declearation should start with <!#~here_the_parameter>

"
<!#color "color name">

Text goes here.
And here.
"

Used to particular lines, segments:

<!#middle> center text to the middle of the page
<!#title> for centering the title horizontally
<!#color "color name">Text here</!#> for coloring text

### Automate text manipulation process (without parameters)

At the beginning of the text define the <!#auto> parameter to automate manipulation and
the working environment size in pixels withe the <!#size> parameters

It regards the spaces as text decorators.
If the text overextends then automatically splits the text.
