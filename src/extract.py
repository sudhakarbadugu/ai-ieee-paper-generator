import zipfile
import xml.etree.ElementTree as ET
import argparse
import os

def extract_text_from_docx(docx_path):
    try:
        with zipfile.ZipFile(docx_path) as z:
            xml_content = z.read('word/document.xml')
        tree = ET.XML(xml_content)
        text = []
        for paragraph in tree.iter('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}p'):
            p_text = ''.join(node.text for node in paragraph.iter('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}t') if node.text)
            if p_text:
                text.append(p_text)
        return '\n'.join(text)
    except Exception as e:
        return str(e)

def extract_text_from_pptx(pptx_path):
    try:
        text = []
        with zipfile.ZipFile(pptx_path) as z:
            slide_files = [f for f in z.namelist() if f.startswith('ppt/slides/slide') and f.endswith('.xml')]
            # Sort slides by number
            slide_files.sort(key=lambda x: int(x.replace('ppt/slides/slide', '').replace('.xml', '')))
            for slide_file in slide_files:
                text.append(f"--- Slide {slide_file} ---")
                xml_content = z.read(slide_file)
                tree = ET.XML(xml_content)
                for paragraph in tree.iter('{http://schemas.openxmlformats.org/drawingml/2006/main}p'):
                    p_text = ''.join(node.text for node in paragraph.iter('{http://schemas.openxmlformats.org/drawingml/2006/main}t') if node.text)
                    if p_text:
                        text.append(p_text)
                text.append("")
        return '\n'.join(text)
    except Exception as e:
        return str(e)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Extract text from DOCX and PPTX files.')
    parser.add_argument('-i', '--input', type=str, required=True, help='Path to the input DOCX or PPTX file.')
    parser.add_argument('-o', '--output', type=str, required=True, help='Path to the output text file.')
    
    args = parser.parse_args()
    
    input_lower = args.input.lower()
    
    with open(args.output, 'w', encoding='utf-8') as f:
        if input_lower.endswith('.docx'):
            f.write(extract_text_from_docx(args.input))
            print(f"Extracted DOCX text to {args.output}")
        elif input_lower.endswith('.pptx'):
            f.write(extract_text_from_pptx(args.input))
            print(f"Extracted PPTX text to {args.output}")
        else:
            print("Unsupported file format. Please provide a .docx or .pptx file.")

