## 📘 Odin Recipes — Project Instructions

This project is built in multiple iterations to create a simple multi-page recipe website using basic HTML.

---

### 🔹 Iteration 1 — Initial Structure

1. Inside the `odin-recipes` directory, create a file named `index.html`.
2. Add the standard HTML boilerplate.
3. Inside the `<body>`, add a main heading:

   `<h1>Odin Recipes</h1>`

This file will serve as the homepage of the website.

---

### 🔹 Iteration 2 — Recipe Page

1. Create a new folder inside `odin-recipes` named `recipes`.
2. Inside the `recipes` folder, create a new HTML file named after your recipe  
   (e.g., `lasagna.html`, `adobo.html`, etc.).
3. Add the standard HTML boilerplate to this file.
4. Inside the `<body>`, add an `<h1>` containing the recipe name.

#### 🔗 Link the Recipe to the Homepage

In `index.html`, add a link to the recipe page below the main heading:

`<a href="recipes/recipename.html">Recipe Title</a>`

Replace `recipename.html` and `Recipe Title` with your actual recipe.

#### 🔙 Add Navigation Back to Home

On your recipe page, add a link back to the homepage:

`<a href="../index.html">Home</a>`

This allows users to easily return to the main page.

---

### 🔹 Iteration 3 — Recipe Page Content

Each recipe page should include the following:

#### 🖼️ Image
A free image of the finished dish placed below the recipe title.

#### 📝 Description
A heading titled **Description**, followed by one or two paragraphs describing the dish.

#### 🥘 Ingredients
A heading titled **Ingredients**, followed by an unordered list of the ingredients needed for the recipe.

#### 👩‍🍳 Steps
A heading titled **Steps**, followed by an ordered list of the steps required to prepare the dish.

---

### 🔹 Iteration 4 — Add More Recipes

1. Create **two additional recipe pages** using the same structure as your first recipe page.
2. Add links to these new recipes on the homepage (`index.html`).

For better organization, place all recipe links inside an unordered list:

