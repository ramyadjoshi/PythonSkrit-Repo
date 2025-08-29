🕉️ PythonSkrit - Sanskrit Processing Tools

A collection of Python-based tools for computational Sanskrit linguistics. This repository combines modern programming with ancient Sanskrit grammar rules to create practical applications for Sanskrit scholars, students, and enthusiasts.
📋 Table of Contents

About Sanskrit & Computational Linguistics
Project Overview
Tools Included
Getting Started
Installation
Usage
Sanskrit Grammar Concepts
Technical Implementation
Educational Value
Contributing
Acknowledgments

🔍 About Sanskrit & Computational Linguistics
Sanskrit, one of the world's oldest languages, is renowned for its systematic grammar and mathematical precision. The language's structured nature makes it particularly suited for computational analysis and processing.
Why Sanskrit Computing?

Systematic Grammar: Panini's Ashtadhyayi provides rule-based grammar perfect for algorithms
Mathematical Structure: Sanskrit's logical construction aligns with programming principles
Digital Preservation: Technology helps preserve and analyze ancient texts
Educational Tools: Modern interfaces make Sanskrit learning accessible
Research Applications: Computational tools assist in linguistic research

Applications in Modern Context

Digital Humanities: Analyzing vast corpora of Sanskrit literature
Machine Translation: Developing Sanskrit-to-modern language translators
Educational Technology: Interactive learning tools for Sanskrit grammar
Text Processing: Automated analysis of classical texts
Linguistic Research: Computational approaches to historical linguistics

🚀 Project Overview
PythonSkrit bridges the gap between ancient Sanskrit grammar and modern computational tools. Each application implements specific Sanskrit grammar rules using Python, providing both educational value and practical utility for Sanskrit processing tasks.
Design Philosophy

Rule-Based Implementation: Direct translation of Sanskrit grammar rules into code
User-Friendly Interface: Intuitive GUI applications accessible to non-programmers
Educational Focus: Tools designed to teach Sanskrit grammar concepts
Accurate Processing: Faithful implementation of traditional grammar rules
Extensible Architecture: Easy to add new rules and features

🛠️ Tools Included
🔤 Ach Sandhi Processor

Purpose: Processes Sanskrit vowel sandhi (euphonic combinations)
Difficulty: Intermediate
Concepts: Phonetic transformations, rule-based processing
Features:

Multiple sandhi types (Savarna Deergha, Guna, Vruddhi, etc.)
Interactive GUI for word combination
Real-time sandhi rule identification
Error handling for invalid inputs



📏 Vrutta Analyzer

Purpose: Analyzes Sanskrit verse meters (chandas/vrutta)
Difficulty: Advanced
Concepts: Prosody analysis, pattern recognition
Features:

Guru-Laghu (heavy-light) syllable analysis
Identification of classical meters
Support for multiple vrutta types
Pattern visualization



🛠️ Technologies Used

Python 3.6+: Core programming language
Tkinter: GUI framework for user interfaces
String Processing: Advanced text manipulation techniques
Pattern Matching: Rule-based pattern recognition
Unicode Support: Proper handling of Devanagari and IAST text

📦 Installation
Prerequisites

Python 3.6 or higher
Tkinter (usually included with Python)
Unicode-capable text display

Setup Instructions

Clone the repository:
bashgit clone https://github.com/yourusername/pythonskrit.git
cd pythonskrit

Verify Python installation:
bashpython --version

Test Tkinter availability:
bashpython -c "import tkinter; print('Tkinter available')"

Run the applications:
bash# For Sandhi Processor
python "ach sandhi processor.py"

# For Vrutta Analyzer
python "vrutta analyzer.py"


💻 Usage
Each tool can be run independently with its own GUI interface:
Quick Start Guide

Choose Your Tool: Select based on your Sanskrit processing needs
Launch Application: Run the Python script
Input Text: Enter Sanskrit text in the provided fields
Process: Click the analyze/process button
Review Results: Examine the grammatical analysis and transformations

Input Formats Supported

IAST (International Alphabet of Sanskrit Transliteration)
Harvard-Kyoto: ASCII representation of Sanskrit
Devanagari: Unicode Sanskrit script (limited support)

📚 Sanskrit Grammar Concepts
Sandhi (Euphonic Combinations)
Sandhi rules govern how sounds change when words combine in continuous speech:
Types Implemented:

Savarna Deergha Sandhi: Similar vowels combine to form long vowels

Example: deva + indra → devendra


Guna Sandhi: Simple vowels combine with 'a' sounds

Example: deva + ish → devesh


Vruddhi Sandhi: Complex vowel transformations

Example: maha + ish → mahesh


Yan Sandhi: Semi-vowel insertions

Example: ati + anta → atyanta


Yanadesha Sandhi: Vowel-to-diphthong transformations

Vrutta (Verse Meters)
Vrutta analysis involves identifying metrical patterns in Sanskrit poetry:
Meters Recognized:

Indravajra: Classical 11-syllable meter
Upendravajra: Variant of Indravajra
Vasanthatilaka: 14-syllable spring-themed meter
Malini: Complex 15-syllable pattern
Shardulavikriditam: Elaborate 19-syllable meter
Anushtup: Common 8-syllable sloka meter

Syllable Analysis:

Guru (Heavy): Long syllables or short syllables followed by consonant clusters
Laghu (Light): Short syllables in open positions

🧩 Technical Implementation
Architecture Overview
Sandhi Processor
python# Rule-based processing system
def process_sandhi(word1, word2):
    # 1. Identify final and initial sounds
    # 2. Apply appropriate sandhi rules
    # 3. Return transformed combination
Vrutta Analyzer
python# Pattern matching system
def analyze_meter(shloka):
    # 1. Extract syllables
    # 2. Determine guru-laghu pattern
    # 3. Match against known meters
Data Structures
Vowel Classifications
python# Short vowels (hrasva)
hrs = ['a','i','u','q','L']

# Long vowels (dirgha)  
dgs = ['A','I','U','Q','e','E','o','O']

# All vowels (swara)
swr = hrs + dgs
Meter Patterns
python# Indravajra pattern (11 syllables)
indravajra = ['g','g','l','g','g','l','l','g','l','g','g']
Algorithm Design

Text Preprocessing: Clean and normalize input
Pattern Recognition: Apply grammatical rules
Transformation Logic: Execute sound changes
Result Generation: Format output with explanations

🎯 Educational Value
For Sanskrit Students

Interactive Learning: Visual feedback for grammar rules
Rule Understanding: See exactly which rules apply
Practice Tool: Test knowledge with various inputs
Error Correction: Learn from mistakes with helpful feedback

For Programmers

String Processing: Advanced text manipulation techniques
Rule-Based Systems: Implementation of grammatical rules
Pattern Matching: Complex pattern recognition algorithms
GUI Development: Building educational interfaces

For Linguists

Computational Methods: Digital approaches to grammar analysis
Rule Formalization: Converting traditional rules to algorithms
Corpus Processing: Tools for analyzing large text collections
Research Applications: Automated analysis capabilities

🔬 Academic Applications
Research Areas

Historical Linguistics: Tracing language evolution
Comparative Grammar: Cross-linguistic analysis
Digital Humanities: Computer-assisted textual analysis
Computational Philology: Automated manuscript processing

Educational Integration

Classroom Tools: Interactive grammar demonstration
Student Assessment: Automated exercise checking
Curriculum Support: Visual learning aids
Distance Learning: Remote Sanskrit education tools

🚀 Future Enhancements
Planned Features

Extended Sandhi Rules: Complete coverage of all sandhi types
More Meters: Additional vrutta patterns and irregular meters
Batch Processing: Handle multiple texts simultaneously
Export Features: Save results in various formats
Web Interface: Browser-based tools for wider accessibility

Advanced Capabilities

Machine Learning Integration: AI-powered pattern recognition
Morphological Analysis: Complete word breakdown
Syntax Analysis: Sentence structure parsing
Semantic Processing: Meaning extraction and analysis

🤝 Contributing
We welcome contributions from Sanskrit scholars, programmers, and enthusiasts!
Ways to Contribute

Rule Additions: Implement additional grammar rules
Bug Fixes: Report and fix processing errors
Documentation: Improve explanations and examples
Testing: Provide test cases and validation
Translations: Multi-language interface support

Getting Started

Fork the repository
Create a feature branch
Implement your changes
Test thoroughly with Sanskrit examples
Submit a pull request with detailed description

📖 Learning Resources
Sanskrit Grammar

Panini's Ashtadhyayi: The foundational grammar text
Whitney's Sanskrit Grammar: Comprehensive modern reference
Macdonell's Sanskrit Grammar: Student-friendly introduction
Sanskrit Prosody Guides: Meter analysis references

Computational Linguistics

Natural Language Processing: Python NLTK documentation
Pattern Recognition: Algorithm design resources
Unicode Handling: Text processing best practices
GUI Development: Tkinter tutorials and examples

🌟 Acknowledgments
Sanskrit Tradition

Panini: For the systematic grammatical foundation
Classical Poets: Whose works provide test cases
Modern Scholars: For grammatical insights and explanations
Sanskrit Community: For feedback and suggestions

Technical Resources

Python Community: For excellent libraries and tools
Unicode Consortium: For Sanskrit character encoding
Open Source Projects: For inspiration and technical approaches


Preserving Ancient Wisdom Through Modern Technology 🕉️💻
"यत्र विश्वं भवत्येकनीडम्" - Where the world becomes one nest
