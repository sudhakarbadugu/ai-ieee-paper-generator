# IEEE Format Paper Generator

This tool mathematically parses standard Markdown (`.md`) files and translates them strictly into official double-column IEEE-formatted documents (DOCX and PDF formats).

## Setup & Environment

Ensure you are running inside the project's virtual environment which contains `python-docx`, `docx2pdf`, and `pyyaml` dependencies:

```bash
# From the project root:
source venv/bin/activate
```

If dependencies are missing, install them:

```bash
pip install python-docx docx2pdf pyyaml
```

## How to use

The script relies on a standard Markdown **YAML Frontmatter Block** at the beginning of the file to auto-populate the Title, custom Authors map, Abstract, and Index Terms:

```markdown
---
title: "Your Academic Paper Title Here"
authors:
  - name: "Your Name"
    department: "Your Department"
    organization: "Your University"
    email: "email@university.edu"
abstract: "The full text of your abstract paragraph goes here..."
index_terms: "Machine Learning, Keywords, Go Here"
---

## I. INTRODUCTION

Your markdown content here...

## REFERENCES

[1] Author, "Title," _Journal_, Year.
```

## Execution

Once your Markdown file (`data/input/input.md` by default) is correctly structured, execute the generator script:

```bash
python src/generate_ieee_format.py
```

You can also specify custom input and output files using command-line arguments:

```bash
python src/generate_ieee_format.py -i data/input/my_custom_paper.md -o data/output/my_custom_paper.docx
```

It will produce the following output files in the requested destination:

- **`my_custom_paper.docx`**
- **`my_custom_paper.pdf`**

---

### Text Extraction Utility

If you need to extract raw text from an existing DOCX or PPTX file to use as AI context, you can use the extraction utility:

```bash
python src/extract.py -i data/input/My_Presentation.pptx -o data/output/extracted_text.txt
```

## Production Error Logging

The script is hardened with production-grade exception handling. Errors such as missing Markdown files, malformed YAML metadata headers, or missing local images are intercepted gracefully to prevent hard crashes.

Detailed execution tracking and error traces are recorded in:

- **`logs/generate_ieee_format.log`**

**To monitor execution logs in real-time, you can tail the log file:**

```bash
tail -f logs/generate_ieee_format.log
```

## AI Agent / Copilot Prompt Template

If you have a raw project documentation file (e.g., a Word Document, PDF, or text file) and want an AI Assistant (like ChatGPT, Claude, GitHub Copilot, or an autonomous Agent) to automatically generate the `IEEE_Paper_Momentum_Trading.md` file for you, copy and paste the following prompt along with your document:

---

**Copy/Paste the block below into your AI Assistant:**

> I have attached my project specification document. I need you to convert this raw document into an IEEE-formatted academic paper written entirely in Markdown format.
>
> Please generate a file named `IEEE_Paper_Momentum_Trading.md` following these STRICT rules:
>
> **1. YAML Metadata Block:**
> You must begin the file with exactly the following YAML metadata frontmatter format (enclosed in `---`). Extract the Title, Authors (with name, role, department, organization, and email), Abstract paragraph, and Index Terms from the document.
>
> ```yaml
> ---
> title: "The Document Title"
> authors:
>   - name: "Your Name"
>     department: "Department Name"
>     organization: "University Name"
>     email: "email@university.edu"
> abstract: "The full text of your abstract paragraph goes here..."
> index_terms: "Machine Learning, Keywords, Go Here"
> ---
> ```
>
> **2. Content Structure & Lengths:**
> Do NOT include the Abstract, Title, or Authors in the markdown text body itself. The markdown body should start immediately with `## I. INTRODUCTION`.
>
> Extract the content into the following main headers logically, adhering strictly to these length constraints to fit the final two-column layout:
>
> - `## I. INTRODUCTION`: 2000 - 3000 characters
> - `## II. LITERATURE REVIEW`: 3500 - 5000 characters (chronological descending order)
> - `## III. PROPOSED METHODOLOGY`: 4000 - 6000 characters
> - `## IV. RESULTS AND DISCUSSION`: 3000 - 4500 characters
> - `## V. CONCLUSION & FUTURE SCOPE`: 1500 - 2000 characters
>
> **3. Formatting Specifics:**
>
> - Use `### A. Subheading`, `### B. Subheading` for subsections.
> - If the document references images or diagrams, write them in markdown format like `![Fig. 1: Architecture](path/to/image.png)`. Immediately below the image markdown, include an italicized caption like `_Fig. 1. Description of the architecture._`
> - Extract all references to the bottom under a `## REFERENCES` header formatted strictly as `[1] Author, "Title," _Journal_, Year.`. Ensure all inline references correspond (e.g. `[1]`).
> - Keep the layout and markdown syntax entirely clean without arbitrary HTML.
