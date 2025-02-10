# Helper function to convert adjacency matrix to mermaid graph syntax
def adjacency_to_mermaid(adj_matrix, graph_id):
    n = len(adj_matrix)
    edges = []
    for i in range(n):
        for j in range(i + 1, n):  # Only process the upper triangle of the matrix (undirected edges)
            if adj_matrix[i][j] == 1:
                edges.append(f"    {graph_id}{i} --> {graph_id}{j}")
    return "\n".join(edges)

# Function to generate Mermaid diagrams for the provided test cases
def generate_mermaid_diagrams(test_cases):
    markdown_content = "# Graph Isomorphism Test Cases with Mermaid Diagrams\n\n"

    for case in test_cases:
        markdown_content += f"## Caso {case['id']}: \n\n"
        
        # Generate the Mermaid diagram for Graph G
        markdown_content += f"**Graph G**:\n\n```mermaid\ngraph TD\n"
        markdown_content += adjacency_to_mermaid(case["G"], "G")
        markdown_content += "\n```\n\n"
        
        # Generate the Mermaid diagram for Graph P
        markdown_content += f"**Graph P**:\n\n```mermaid\ngraph TD\n"
        markdown_content += adjacency_to_mermaid(case["P"], "P")
        markdown_content += "\n```\n\n"
    
    # Return the markdown content for use
    return markdown_content

# Example test cases (as provided)
test_cases = [
    {
        "id": 1,
        "G": [
            [0, 1, 1, 0],
            [1, 0, 1, 1],
            [1, 1, 0, 1],
            [0, 1, 1, 0]
        ],
        "P": [
            [0, 1],
            [1, 0]
        ],
        "expected": True
    },
    {
        "id": 2,
        "G": [
            [0, 1, 1, 0],
            [1, 0, 1, 0],
            [1, 1, 0, 0],
            [0, 0, 0, 0]
        ],
        "P": [
            [0, 1, 1],
            [1, 0, 1],
            [1, 1, 0]
        ],
        "expected": False
    },
    {
        "id": 3,
        "G": [
            [0, 1, 1],
            [1, 0, 1],
            [1, 1, 0]
        ],
        "P": [
            [0, 1, 1],
            [1, 0, 1],
            [1, 1, 0]
        ],
        "expected": True
    },
    {
        "id": 4,
        "G": [
            [0, 1],
            [1, 0]
        ],
        "P": [
            [0, 1, 1],
            [1, 0, 1],
            [1, 1, 0]
        ],
        "expected": False
    },
    {
        "id": 5,
        "G": [
            [0, 1, 0, 1],
            [1, 0, 1, 0],
            [0, 1, 0, 1],
            [1, 0, 1, 0]
        ],
        "P": [
            [0, 1, 1],
            [1, 0, 0],
            [1, 0, 0]
        ],
        "expected": True
    }
]

# Generate the markdown content with Mermaid diagrams
markdown_content = generate_mermaid_diagrams(test_cases)

# Save to a .md file
file_path = "/home/francois/Desktop/mermaid_graps.md"
with open(file_path, "w") as f:
    f.write(markdown_content)

file_path
