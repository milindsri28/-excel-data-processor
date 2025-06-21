import pandas as pd
import os
from datetime import datetime

def test_excel_file(filename):
    """Test if an Excel file is valid and can be read"""
    try:
        # Read the Excel file
        df = pd.read_excel(filename)
        
        # Basic validation
        row_count = len(df)
        col_count = len(df.columns)
        
        # Check for empty dataframe
        if row_count == 0:
            return False, f"File is empty: {filename}"
        
        # Check for empty columns
        empty_cols = df.columns[df.isnull().all()].tolist()
        
        # Get data types
        data_types = df.dtypes.to_dict()
        
        # Check for datetime columns
        datetime_cols = [col for col, dtype in data_types.items() if 'datetime' in str(dtype)]
        
        print(f"✅ {filename}")
        print(f"   📊 Rows: {row_count}, Columns: {col_count}")
        print(f"   📋 Columns: {list(df.columns)}")
        print(f"   📅 Datetime columns: {datetime_cols}")
        if empty_cols:
            print(f"   ⚠️  Empty columns: {empty_cols}")
        print()
        
        return True, {
            'rows': row_count,
            'columns': col_count,
            'column_names': list(df.columns),
            'data_types': data_types,
            'datetime_cols': datetime_cols,
            'empty_cols': empty_cols
        }
        
    except Exception as e:
        print(f"❌ Error reading {filename}: {str(e)}")
        return False, str(e)

def main():
    """Test all sample Excel files"""
    print("🧪 Testing Sample Excel Files")
    print("=" * 50)
    
    # List of expected sample files
    expected_files = [
        'sample_employee_data.xlsx',
        'sample_sales_data.xlsx', 
        'sample_inventory_data.xlsx',
        'sample_student_data.xlsx',
        'sample_customer_data.xlsx',
        'sample_weather_data.xlsx',
        'sample_simple_data.xlsx'
    ]
    
    results = {}
    total_files = len(expected_files)
    successful_files = 0
    
    for filename in expected_files:
        if os.path.exists(filename):
            success, result = test_excel_file(filename)
            results[filename] = result
            if success:
                successful_files += 1
        else:
            print(f"❌ File not found: {filename}")
            results[filename] = "File not found"
    
    # Summary
    print("=" * 50)
    print("📊 TEST SUMMARY")
    print("=" * 50)
    print(f"Total files: {total_files}")
    print(f"Successful: {successful_files}")
    print(f"Failed: {total_files - successful_files}")
    
    if successful_files == total_files:
        print("\n🎉 All sample files are valid and ready for testing!")
    else:
        print(f"\n⚠️  {total_files - successful_files} files have issues")
    
    # Detailed results
    print("\n📋 DETAILED RESULTS:")
    for filename, result in results.items():
        if isinstance(result, dict):
            print(f"✅ {filename}: {result['rows']} rows, {result['columns']} columns")
        else:
            print(f"❌ {filename}: {result}")
    
    # Data type analysis
    print("\n🔍 DATA TYPE ANALYSIS:")
    all_data_types = set()
    for filename, result in results.items():
        if isinstance(result, dict):
            for col, dtype in result['data_types'].items():
                all_data_types.add(str(dtype))
    
    print(f"Data types found: {sorted(all_data_types)}")
    
    # Recommendations
    print("\n💡 RECOMMENDATIONS:")
    if successful_files == total_files:
        print("• All files are ready for testing")
        print("• Try uploading different file types to test various scenarios")
        print("• Test the automatic data clearing functionality")
        print("• Verify sorting, searching, and pagination work correctly")
    else:
        print("• Fix any file issues before testing")
        print("• Regenerate problematic files using create_multiple_samples.py")
    
    return successful_files == total_files

if __name__ == "__main__":
    success = main()
    exit(0 if success else 1) 