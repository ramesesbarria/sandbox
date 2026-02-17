# Landing Page — Editing Guide

This guide walks you through how to change any part of the landing page.
Every example shows you exactly which file to open, which class to find,
and which line to change. No guessing required.

---

## How the two files connect

```
index.html   — the structure and content (words, boxes, links)
styles.css   — the appearance (colours, sizes, spacing, layout)
```

The rule is simple: **if you want to change what's on the page, edit the HTML.
If you want to change how it looks, edit the CSS.**

---

## How to find things in styles.css

Every section in `styles.css` has a comment header like this:

```css
/* =============================================
   HERO SECTION
============================================= */
```

Use your editor's find feature (`Ctrl+F` or `Cmd+F`) and search for the
section name (e.g. `HERO`) to jump straight to it.

---

## 1. HEADER

### Change the logo text
In `index.html`, find this line and change the text:
```html
<p class="logo">Header Logo</p>
```

### Change the logo size
In `styles.css`, find `.logo` and change `font-size`:
```css
.logo {
  font-size: 24px;  /* make this bigger or smaller */
}
```

### Change the nav link text
In `index.html`, find the `<ul class="nav-links">` block and edit the text
inside each `<a>` tag:
```html
<li><a href="#">header link one</a></li>
```

### Change the nav link colour
In `styles.css`, find `.nav-links a` and change `color`:
```css
.nav-links a {
  color: #E5E7EB;  /* replace this hex code with any colour you want */
}
```

### Change the space between nav links
In `styles.css`, find `.nav-links li` and change `margin-right`:
```css
.nav-links li {
  margin-right: 24px;  /* bigger = more space, smaller = less space */
}
```

### Change the header background colour
In `styles.css`, find `header` and change `background-color`:
```css
header {
  background-color: #1F2937;  /* change this hex code */
}
```

### Make the header taller or shorter
In `styles.css`, find `header` and change `padding`.
The two values are top/bottom and left/right:
```css
header {
  padding: 16px 0;  /* increase 16px to make it taller */
}
```

---

## 2. HERO SECTION

### Change the heading text
In `index.html`, find the `<h1>` tag and edit the text:
```html
<h1>This website is awesome</h1>
```

### Change the heading size
In `styles.css`, find `.hero-text h1` and change `font-size`:
```css
.hero-text h1 {
  font-size: 48px;  /* 48px is the default — try 36px or 64px */
}
```

### Change the heading colour
In `styles.css`, find `.hero-text h1` and change `color`:
```css
.hero-text h1 {
  color: #F9FAF8;
}
```

### Change the subtext below the heading
In `index.html`, find the `<p>` tag inside `.hero-text`:
```html
<p>This website has some subtext that goes here...</p>
```

### Change the space between the heading and the subtext
In `styles.css`, find `.hero-text h1` and change `margin-bottom`:
```css
.hero-text h1 {
  margin-bottom: 16px;  /* bigger = more gap below the heading */
}
```

### Change the space between the subtext and the button
In `styles.css`, find `.hero-text p` and change `margin-bottom`:
```css
.hero-text p {
  margin-bottom: 24px;  /* bigger = more gap below the paragraph */
}
```

### Make the hero section taller or shorter
In `styles.css`, find `.hero` and change `padding`:
```css
.hero {
  padding: 80px 0;  /* 80px top and bottom — increase to make it taller */
}
```

### Change the placeholder image box colour
In `styles.css`, find `.hero-image` and change `background-color`:
```css
.hero-image {
  background-color: #6B7280;  /* currently medium grey */
}
```

### Make the placeholder image box taller or shorter
In `styles.css`, find `.hero-image` and change `height`:
```css
.hero-image {
  height: 240px;  /* change this number */
}
```

### Swap the columns (put image on left, text on right)
In `index.html`, move the entire `<div class="hero-image">` block
so it appears BEFORE `<div class="hero-text">`:
```html
<div class="hero-content">
  <div class="hero-image">...</div>   <!-- image first = left column -->
  <div class="hero-text">...</div>    <!-- text second = right column -->
</div>
```

---

## 3. BUTTONS

There are two buttons on the page. Both use the `.button` class.
The CTA button also has `.button-outline` added to it.

### Change the button text
In `index.html`, find the `<a>` tags with `class="button"` and edit the text:
```html
<a href="#" class="button">Sign up</a>
```

### Change the button background colour
In `styles.css`, find `.button` and change `background-color`:
```css
.button {
  background-color: #3882F6;  /* the blue — change to any colour */
}
```
> Note: also change `border` to match, otherwise you'll see a mismatched border:
> ```css
> border: 2px solid #3882F6;
> ```

### Make the button bigger or smaller
In `styles.css`, find `.button` and change `padding`.
The two values are top/bottom and left/right:
```css
.button {
  padding: 10px 24px;  /* increase both numbers to make a bigger button */
}
```

### Make the button text bigger or smaller
In `styles.css`, find `.button` and change `font-size`:
```css
.button {
  font-size: 16px;
}
```

### Make the button corners more or less rounded
In `styles.css`, find `.button` and change `border-radius`:
```css
.button {
  border-radius: 6px;   /* 0 = sharp corners, 50px = pill shape */
}
```

---

## 4. INFO SECTION (the four cards)

### Change the section heading
In `index.html`, find the `<h2>` tag and edit the text:
```html
<h2>Some random information.</h2>
```

### Change the heading size
In `styles.css`, find `.info-section h2` and change `font-size`:
```css
.info-section h2 {
  font-size: 36px;
}
```

### Change the space between the heading and the cards
In `styles.css`, find `.info-section h2` and change `margin-bottom`:
```css
.info-section h2 {
  margin-bottom: 48px;  /* bigger = more gap between heading and cards */
}
```

### Change a card's subtext
In `index.html`, find the `<p>` tag inside whichever `.card` you want
and edit the text:
```html
<div class="card">
  <div class="card-image"></div>
  <p>this is some subtext under an illustration or image</p>
</div>
```

### Make the card images bigger or smaller
In `styles.css`, find `.card-image` and change both `width` and `height`.
Keep them the same number to keep the square shape:
```css
.card-image {
  width: 150px;   /* change both to the same number */
  height: 150px;
}
```

### Change the card image border colour
In `styles.css`, find `.card-image` and change `border`:
```css
.card-image {
  border: 3px solid #3882F6;  /* change #3882F6 to any colour */
}
```

### Make the card image border thicker or thinner
In `styles.css`, find `.card-image` and change the first number in `border`:
```css
.card-image {
  border: 3px solid #3882F6;  /* change 3px to e.g. 1px or 6px */
}
```

### Change the space between cards
In `styles.css`, find `.card` and change `margin-right`:
```css
.card {
  margin-right: 32px;  /* bigger = more space between cards */
}
```

### Add a fifth card
In `index.html`, copy one of the existing `.card` blocks and paste it
before the closing `</div>` of `.card-row`:
```html
<div class="card">
  <div class="card-image"></div>
  <p>your new subtext here</p>
</div>
```

### Remove a card
In `index.html`, delete an entire `.card` block (from `<div class="card">`
to its closing `</div>`).

---

## 5. QUOTE SECTION

### Change the quote text
In `index.html`, find `<p class="quote-text">` and edit the text:
```html
<p class="quote-text">"Your new quote goes here."</p>
```

### Change the author name
In `index.html`, find `<p class="quote-author">` and edit the text:
```html
<p class="quote-author">-Your Name Here</p>
```

### Change the quote font size
In `styles.css`, find `.quote-text` and change `font-size`:
```css
.quote-text {
  font-size: 36px;  /* try 24px for smaller, 48px for bigger */
}
```

### Remove the italic style from the quote
In `styles.css`, find `.quote-text` and change `font-style`:
```css
.quote-text {
  font-style: italic;  /* change to: font-style: normal; */
}
```

### Change the quote section background colour
In `styles.css`, find `.quote-section` and change `background-color`:
```css
.quote-section {
  background-color: #E5E7EB;  /* currently light grey */
}
```

### Make the quote section taller or shorter
In `styles.css`, find `.quote-section` and change `padding`:
```css
.quote-section {
  padding: 80px 0;  /* increase or decrease the 80px */
}
```

---

## 6. CALL TO ACTION (CTA) SECTION

### Change the CTA heading text
In `index.html`, find `<p class="cta-heading">` and edit the text:
```html
<p class="cta-heading">Call to action! It's time!</p>
```

### Change the CTA subtext
In `index.html`, find `<p class="cta-subtext">` and edit the text:
```html
<p class="cta-subtext">Sign up for our product by clicking that button right over there!</p>
```

### Change the CTA card background colour
In `styles.css`, find `.cta-card` and change `background-color`:
```css
.cta-card {
  background-color: #3882F6;  /* currently blue */
}
```

### Make the CTA card taller or shorter
In `styles.css`, find `.cta-card` and change the first number in `padding`
(that controls top and bottom space):
```css
.cta-card {
  padding: 40px 48px;  /* increase 40px to make it taller */
}
```

### Make the CTA card narrower
In `styles.css`, find `.cta-section` and add a `max-width` smaller than 960px:
```css
.cta-section {
  max-width: 700px;  /* card will only be as wide as this */
}
```

### Make the CTA card corners more or less rounded
In `styles.css`, find `.cta-card` and change `border-radius`:
```css
.cta-card {
  border-radius: 10px;  /* 0 = sharp rectangle, higher = more rounded */
}
```

---

## 7. FOOTER

### Change the footer text
In `index.html`, find the `<p>` tag inside `<footer>` and edit the text:
```html
<p>Copyright &#169; The Odin Project 2021</p>
```
> `&#169;` is the HTML code for the © symbol. You can just type © directly
> if you prefer — both work.

### Change the footer background colour
In `styles.css`, find `footer` and change `background-color`:
```css
footer {
  background-color: #1F2937;
}
```

### Make the footer taller or shorter
In `styles.css`, find `footer` and change `padding`:
```css
footer {
  padding: 28px 0;  /* increase 28px to make it taller */
}
```

---

## 8. COLOURS — quick reference

Here are all the hex colour codes used on the page and where they appear.
To change the whole colour scheme, search for these values in `styles.css`
and replace them.

| Colour code | What it looks like   | Where it's used                        |
|-------------|----------------------|----------------------------------------|
| `#1F2937`   | Very dark blue-grey  | Header, hero, footer backgrounds       |
| `#F9FAF8`   | Near white           | Hero heading, logo text                |
| `#E5E7EB`   | Light grey           | Nav links, hero subtext, quote bg      |
| `#6B7280`   | Medium grey          | Placeholder image bg, card subtext     |
| `#3882F6`   | Blue                 | Buttons, card borders, CTA card bg     |
| `#FFFFFF`   | White                | Info section and CTA section bg        |
| `#1F2937`   | Dark (same as above) | Body text on white backgrounds         |

---

## 9. SPACING — how padding and margin work

These two properties control all the spacing on the page. It's worth
understanding them clearly because you'll use them constantly.

**`padding`** — space *inside* an element, between its edge and its content.
Making padding bigger makes the element itself grow.

**`margin`** — space *outside* an element, pushing other elements away.
Making margin bigger moves things further apart without changing their size.

When you see one value: `padding: 80px` — applies to all four sides.

When you see two values: `padding: 80px 0` — first number is top/bottom,
second is left/right.

When you see four values: `padding: 10px 24px 10px 24px` — top, right,
bottom, left (clockwise from the top).

---

## 10. TYPOGRAPHY — changing fonts and text

### Change the font for the whole page
In `styles.css`, find `body` and change `font-family`:
```css
body {
  font-family: 'Roboto', sans-serif;
}
```
To use a different Google Font, replace `'Roboto'` with your chosen font name
and update the `<link>` tag in `index.html` to load that font instead.

### Font weight reference
`font-weight` controls how bold text appears. The values used on this page:

| Value | Appearance      |
|-------|-----------------|
| `300` | Light (thin)    |
| `400` | Normal/regular  |
| `700` | Bold            |
| `900` | Extra bold      |

### Make ALL text on the page bigger
In `styles.css`, find `body` and add a `font-size`:
```css
body {
  font-size: 18px;  /* everything inherits this as a base size */
}
```
Individual elements with their own `font-size` won't be affected —
only elements that haven't been given a specific size.

---

## 11. LAYOUT — understanding the page structure

The page is made up of stacked horizontal blocks. Each block is full width.
Inside each block, a wrapper div limits the content width to 960px and
centres it on the page. That wrapper always has these properties:

```css
max-width: 960px;
margin-left: auto;
margin-right: auto;
padding-left: 24px;
padding-right: 24px;
```

`max-width: 960px` — the content won't grow wider than 960px.
`margin: auto` on both sides — centres the content horizontally.
`padding` on both sides — keeps content from touching the screen edge.

### Make all content wider or narrower
Find every place in `styles.css` where `max-width: 960px` appears and
change the number. It appears in: `.header-content`, `.hero-content`,
`.info-section`, and `.cta-section`.

### The two-column layouts use flexbox
Both the header (logo + nav) and the hero (text + image) use
`display: flex` to place things side by side. The key properties are:

- `display: flex` — activates flexbox on the parent
- `justify-content: space-between` — pushes children to opposite ends
- `align-items: center` — lines children up in the vertical middle
- `flex: 1` — makes both hero columns take equal width