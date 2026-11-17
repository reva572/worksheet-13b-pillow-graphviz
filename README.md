
# Graphviz + Pillow: Combined Workflow

## 1. What it does
Creates a horizontal flowchart and adds a title and lavender background to it.

## 2. Libraries used
- **Graphviz:** Generates the flowchart with connected nodes.
- **Pillow:** Adds the title and background, then saves the final image.

## 3. Requirements
Install Graphviz on macOS:

```bash
brew install graphviz
```

Install the Python libraries:

```bash
pip install graphviz pillow
```

## 4. How to run

```bash
python combined_project.py
```

## 5. Output

The program creates `combined_flowchart.png`, showing a lavender title area and a horizontal flowchart:

![Combined workflow](combined_flowchart.png)

## 6. Limitations
- The flowchart has only three predefined nodes.
- The title and background colour are fixed in the code.
- The program does not accept user input to customise the diagram.
