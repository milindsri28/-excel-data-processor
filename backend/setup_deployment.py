#!/usr/bin/env python3
"""
Helper script to extract Firebase credentials for deployment setup.
This script reads your local firebase-service-account.json file and
outputs the environment variables you need to set for deployment.
"""

import json
import os
import sys

def main():
    """Extract Firebase credentials for deployment"""
    
    # Check if service account file exists
    service_account_path = "firebase-service-account.json"
    if not os.path.exists(service_account_path):
        print("ERROR: firebase-service-account.json not found!")
        print("Please ensure the file exists in the current directory.")
        sys.exit(1)
    
    try:
        # Read the service account file
        with open(service_account_path, 'r') as f:
            service_account_data = json.load(f)
        
        # Extract project ID for database URL
        project_id = service_account_data.get('project_id')
        if not project_id:
            print("ERROR: Could not find project_id in service account file")
            sys.exit(1)
        
        # Create database URL
        database_url = f"https://{project_id}.firebaseio.com"
        
        # Convert service account to JSON string
        service_account_json = json.dumps(service_account_data)
        
        print("SUCCESS: Firebase credentials extracted successfully!")
        print("\n" + "="*60)
        print("ENVIRONMENT VARIABLES FOR DEPLOYMENT")
        print("="*60)
        print("\nSet these environment variables in your deployment platform:")
        print("\n1. FIREBASE_DATABASE_URL:")
        print(f"   {database_url}")
        print("\n2. FIREBASE_SERVICE_ACCOUNT:")
        print(f"   {service_account_json}")
        print("\n" + "="*60)
        print("IMPORTANT NOTES:")
        print("- Copy the entire JSON string for FIREBASE_SERVICE_ACCOUNT")
        print("- Make sure there are no line breaks in the JSON string")
        print("- Never commit these values to version control")
        print("="*60)
        
    except json.JSONDecodeError:
        print("ERROR: Invalid JSON in firebase-service-account.json")
        sys.exit(1)
    except Exception as e:
        print(f"ERROR: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main() 