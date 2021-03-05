# HTML AND CSS
## 1. HTML
### 1.1 Introduction
#### What is HTML ?
*HTML is a hyper-text markup language used to structure content on a web page(images,text,forms etc..)
*We strucutre content using HTML tags:
``` javascript
    <p> content </p>
    <a> link </a>
    <image> 
```
#### Basic HTML Tags
* ``` <!DOCTYPE> ``` Defines the document type
* ``` <html> ``` Defines the HTML document
* ``` <head> ``` contains the metadata information
* ``` <body> ``` Defines the body of the document
* ``` <h1> to <h6> ``` Different HTML headings
* ``` <p> ``` defines the paragraph
* ``` <br> ``` Inserts a single break
* ``` <hr> ``` defines the change in document
* ``` <!--  --> ``` comment in html
* ```<div>``` defines a section
* ```<span>``` defines a section
* ```<header>``` header of the document
* ```<footer>``` footer of the document

#### Forms and Input Tags
* ```<form>``` defines the html form for user input
* ```<input>``` defines the input control
* ```<button>``` defines a clickable button
* ```<select>``` drop down list
* ```<label>``` defines the label

#### Image tags
* ```<img>``` defines the image
* ```<svg>``` defines the container for the svg graphics

#### list
* ```<ul>``` unorderd list
* ```<ol>``` ordered list

#### links
* ```<a>``` Defines a hyperlink
* ```<link>``` defines the relationship between a document and a external source
* ```<nav>``` navigation links

#### HTML SAMPLE SYNTAX
``` html
    <html>
    <body>
    <p> content </p>
    <a> link </a>
    </body>
    </html>
```

``` html 
    <html>
    <body>
      <ul>
        <li> Apple </li>
        <li> orange </li>
        <li> Graped </li>
      </ul>
    </body>
    </html>
```

#### HTML FORMS
``` html
  <html>
    <body>
      <div>
        <form>
          <input type ="text" id = "username">
        </form>
      </div>              
    </body>
  </html>
```
## CSS
### CSS Basics
* Cascading Style Sheets, fondly referred to as CSS, is a simple design language intended to simplify the process of making
web pages presentable.
* CSS handles the look and feel part of a web page. Using CSS, you can control the color of the text, the style of fonts, the spacing between paragraphs, how columns are sized and laid out, what background images or colors are used, layout
designs,variations in display for different devices and screen sizes as well as a variety of other effects.
* We create a seperate file line ```styles.css```file inorder to write the css property. Then we will link this css file with the HTML file. To do that, we should link that file in the header of the HTML file.

#### Sample css
``` html
   <html>
          <head>
             <title>basics</title>
             <rel ="stylesheet" href ="./styles.css">
             </head>
          <body>
            <div>
                <form>
                <label for ="username"></label> 
                <input type ="text id ="username">
                </form>
            </div>              
          </body>
        </html>
```
#### CSS Properties
* ```color``` This property is used to change the color of the text
* ```background``` Used to change the background color
* ```background-image``` used set the background image
* ```display``` display the behaviour 
* ```height``` Element height 
* ```width``` width of the element
* ```min-width``` Minimum Width.
* ```min-height``` Minimum height.
* ```max-height``` Maximum height.
* ```margin``` Outter margins property.
* ```padding``` Inner margin property.   
* ```border``` - Border property.
* ```border-color``` - Border color.
* ```border-width``` - Border width.
* ```border-radius``` - Radius of the border.
* ```font```- Font properties.
* ```font-family``` - Defines the font.
* ```font-style``` - Font style.
* ```font-weight``` - Thickness of the font
* ```position``` -Type of positioning used for an element.
* ```z-index``` - Sets the order of overlapping elements.
* ```text-decoration``` - This is used to add decorations to the text.
* ```text-align``` - This changes the alignment of the text.

### POSTION AND LAYOUT
* ```static``` :Here the positon is not specifically mentioned. The elements get arranged by the default properties.
* ```Relative``` :The position of the item can be changed to anywhere if th position property is selected as relative.
* ```Fixed``` : Here, the position of this item will not be changed and it will be there forever even the page is scrolled.
* ```absolute``` : The position of the child can be perfectly arranged by taking the space of the parent.
* ```sticky``` :Once the sticky property applied, we can stick anything to the page while its scrolling.

### Pseudo Classes & Elements
*Style elements when they are in a particular statw. - hover,focus,first child of a prent. - :hover :focus :first-childg

#### What are Pseudo-Elements?
-A CSS pseudo-element is used to style specified parts of an element. For example, it can be used to:
*Style the first letter, or line, of an element
*Insert content before, or after, the content of an element

###  Semantic Tags
*Semantic HTML is the use of HTML markup to reinforce the semantics, or meaning, of the information in webpages and web applications rather than merely to define its presentation or look.

### Media quries
* Creates responsive desgins.
* Tell the browser how to style an element at particular viewport dimentions.

### Responsive Images
* Only load smaller images for mobile devices.
``` html
  @media screen and (max-width: 1400px) {
    width:80%;
  }
```
## CSS Flex-Box
* FLexbox is a CSS display type designed to help us craft CSS layouts much easier
* Controls the position, size and spcing of each other. Works great responsively

### Flex-Box Basics
* Apply adisplay type of flex to the parent continer. The children element in that parent directly become flex items.
* There is how we can maked them to grow and shrink accordance with our need.

### FLEX CONTAINERS
``` display:flex;```
* When using display as flex, the all children get stacked from left to right.

### FLEX GROW property
``` flex-grow: 1; ```
* This means the the children grow the full space of the parent.
* Adding flex-grow value is like a ratio how to grow the childre with the parent.

### FLEX SHRINK property
``` flex-shrink: 1;```
* Just opposite of flex-grow. As browser gets smaller, the shrinking rate of the child based on the value set for each. Bigger the number of flex-shrink shrinks more than others.

###  FLEX WRAP property
```flex-wrap: wrap;```
* If in the css we have specified a minimum-width for the parent or any other part, we can see that while we reduce the
browser's width, after reduced the minimum-width, there will be a scroll bar appear at the bottom to preserve the width of
that body.

```flex-wrap: wrap-reverse;```
* Wrap reverse does opposit of flex wrap. When the width of the browser goes down to the minimum width, instead of going the last element of the flex to the next line, it will go the upper line and remaining elements will become under the last element.

### FLEX BASIS
``` flex-basis: 500px;```
* Flex basis is like minimum width of the flex box.The application of use of flex basis is, even the size of the children become reduced below the minimum pixel value, intead of displaying bottom scroll bar, it will shrink again.
``` flex : 1 0 200px; ```
* Basically what happens here is, the flex grow property is 1, flex shrink property is 1 and flex basis is zero.

### Justify Properites Of Flex
``` justify-content: center;``` This property is used to align the all children to the center of the main body.
``` justify-content: space-between;``` This property gives the space between elements
``` justify-content: space-around;``` Each side of each element gets spaced.
``` justify-content: flex-end;``` This property is used to align the all children into the end, probably the right side of the main body.
``` justify-content: flex-start;``` This is the default behaviour of flex box. Items get arranged to the left side of the main body.

### Align and Center
``` flex-flow: row;``` 

``` flex-flow:column;```

When we use flex box, there are two axis.Main axis(x) and cross axis(y)
When we change the value of the flex flow, we are chagning the direction of the axis.
flex-flow:row main axis is the horizontal axis. The children line-up on the main axis. The down vertical axis will be
the cross axis.flex-flow: column main axis is the vertical axis. The children line-up on the main axis. The horizontal axis will be the cross.