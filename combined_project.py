
import graphviz
from PIL import Image, ImageDraw

# Step 1: Create a flowchart using Graphviz
dot = graphviz.Digraph(comment="My Workflow")
dot.attr(rankdir="LR")

dot.node("A", "Start")
dot.node("B", "Process")
dot.node("C", "End")

dot.edge("A", "B")
dot.edge("B", "C")

# Save the flowchart as a PNG image
dot.render("workflow_graph", format="png", cleanup=True)

# Step 2: Open the flowchart using Pillow
graph_image = Image.open("workflow_graph.png").convert("RGB")

width, height = graph_image.size

# Step 3: Create a new image with space for a title
final_image = Image.new(
    "RGB",
    (width, height + 100),
    "lavender"
)

# Step 4: Add the title using Pillow
draw = ImageDraw.Draw(final_image)
draw.text((20, 35), "MY WORKFLOW", fill="black")

# Step 5: Paste the Graphviz flowchart below the title
final_image.paste(graph_image, (0, 100))

# Step 6: Save the final image
final_image.save("combined_flowchart.png")

print("Combined project created successfully!")
