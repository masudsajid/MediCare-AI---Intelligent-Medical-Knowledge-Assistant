#!/usr/bin/env python3
"""
Medical RAG Chatbot - Main Entry Point
"""

import os
import sys
from dotenv import load_dotenv

def check_environment():
    """Check if all required environment variables are set."""
    load_dotenv()
    
    required_vars = ["PINECONE_API_KEY", "GROQ_API_KEY"]
    missing_vars = []
    
    for var in required_vars:
        if not os.getenv(var):
            missing_vars.append(var)
    
    if missing_vars:
        print("❌ Missing required environment variables:")
        for var in missing_vars:
            print(f"   - {var}")
        print("\n📝 Please create a .env file with the following variables:")
        print("PINECONE_API_KEY=your_pinecone_api_key_here")
        print("GROQ_API_KEY=your_groq_api_key_here")
        return False
    
    return True

def check_pdf_file():
    """Check if the medical PDF file exists."""
    pdf_path = "data/Medical_book.pdf"
    if not os.path.exists(pdf_path):
        print(f"❌ Medical PDF file not found at: {pdf_path}")
        print("📝 Please ensure the PDF file is in the data/ directory")
        return False
    return True

def main():
    """Main entry point for the application."""
    print("🧠 Medical RAG Chatbot")
    print("=" * 50)
    
    # Check environment
    if not check_environment():
        sys.exit(1)
    
    # Check PDF file
    if not check_pdf_file():
        sys.exit(1)
    
    print("✅ Environment check passed!")
    print("\n🚀 To start the application:")
    print("1. First, set up the vector database:")
    print("   python vectore_store_db.py")
    print("\n2. Then start the Flask server:")
    print("   python app.py")
    print("\n3. Open your browser and go to: http://localhost:8080")

if __name__ == "__main__":
    main()
