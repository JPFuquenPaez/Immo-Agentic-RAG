# Temporary test script (test_imports.py)
import sys
print("Python Path:")
for p in sys.path:
    print(p)

try:
    from immo_rag.agent import AgentManager
    print("\nSUCCESS: Imports working!")
except ImportError as e:
    print(f"\nFAILURE: {str(e)}")