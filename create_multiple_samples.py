import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

def create_employee_data():
    """Create employee data with various fields"""
    np.random.seed(42)
    
    data = {
        'Employee_ID': range(1, 51),
        'Name': [f'Employee_{i}' for i in range(1, 51)],
        'Department': np.random.choice(['IT', 'HR', 'Finance', 'Marketing', 'Sales'], 50),
        'Position': np.random.choice(['Manager', 'Senior', 'Junior', 'Intern'], 50),
        'Salary': np.random.randint(30000, 120000, 50),
        'Age': np.random.randint(22, 65, 50),
        'Experience_Years': np.random.randint(0, 20, 50),
        'Location': np.random.choice(['New York', 'London', 'Tokyo', 'Berlin', 'Sydney'], 50),
        'Hire_Date': [datetime.now() - timedelta(days=np.random.randint(0, 365*5)) for _ in range(50)],
        'Performance_Score': np.random.uniform(3.0, 5.0, 50).round(2),
        'Projects_Completed': np.random.randint(1, 25, 50),
        'Is_Active': np.random.choice([True, False], 50, p=[0.8, 0.2])
    }
    
    df = pd.DataFrame(data)
    df.to_excel('sample_employee_data.xlsx', index=False)
    print("✅ Created: sample_employee_data.xlsx (50 employee records)")

def create_sales_data():
    """Create sales data with financial fields"""
    np.random.seed(123)
    
    data = {
        'Order_ID': range(1001, 1101),
        'Customer_Name': [f'Customer_{i}' for i in range(1, 101)],
        'Product': np.random.choice(['Laptop', 'Phone', 'Tablet', 'Monitor', 'Keyboard'], 100),
        'Quantity': np.random.randint(1, 10, 100),
        'Unit_Price': np.random.uniform(100, 2000, 100).round(2),
        'Total_Amount': [],
        'Order_Date': [datetime.now() - timedelta(days=np.random.randint(0, 365)) for _ in range(100)],
        'Payment_Method': np.random.choice(['Credit Card', 'Debit Card', 'Cash', 'Bank Transfer'], 100),
        'Region': np.random.choice(['North', 'South', 'East', 'West'], 100),
        'Sales_Rep': [f'Sales_{i}' for i in np.random.randint(1, 11, 100)],
        'Status': np.random.choice(['Completed', 'Pending', 'Cancelled'], 100, p=[0.7, 0.2, 0.1])
    }
    
    # Calculate total amount
    data['Total_Amount'] = [data['Quantity'][i] * data['Unit_Price'][i] for i in range(100)]
    
    df = pd.DataFrame(data)
    df.to_excel('sample_sales_data.xlsx', index=False)
    print("✅ Created: sample_sales_data.xlsx (100 sales records)")

def create_inventory_data():
    """Create inventory data with stock management fields"""
    np.random.seed(456)
    
    data = {
        'Product_ID': range(2001, 2101),
        'Product_Name': [f'Product_{i}' for i in range(1, 101)],
        'Category': np.random.choice(['Electronics', 'Clothing', 'Books', 'Home', 'Sports'], 100),
        'Brand': np.random.choice(['Brand_A', 'Brand_B', 'Brand_C', 'Brand_D'], 100),
        'Stock_Quantity': np.random.randint(0, 500, 100),
        'Reorder_Level': np.random.randint(10, 50, 100),
        'Unit_Cost': np.random.uniform(5, 200, 100).round(2),
        'Selling_Price': [],
        'Supplier': [f'Supplier_{i}' for i in np.random.randint(1, 21, 100)],
        'Last_Updated': [datetime.now() - timedelta(days=np.random.randint(0, 30)) for _ in range(100)],
        'Location': np.random.choice(['Warehouse_A', 'Warehouse_B', 'Store_1', 'Store_2'], 100),
        'Status': []
    }
    
    # Calculate selling price (30-50% markup)
    for i in range(100):
        markup = np.random.uniform(0.3, 0.5)
        data['Selling_Price'].append(data['Unit_Cost'][i] * (1 + markup))
    
    # Set status based on stock level
    data['Status'] = ['Low Stock' if data['Stock_Quantity'][i] <= data['Reorder_Level'][i] else 'In Stock' for i in range(100)]
    
    df = pd.DataFrame(data)
    df.to_excel('sample_inventory_data.xlsx', index=False)
    print("✅ Created: sample_inventory_data.xlsx (100 inventory records)")

def create_student_data():
    """Create student data with academic fields"""
    np.random.seed(789)
    
    data = {
        'Student_ID': range(3001, 3101),
        'Name': [f'Student_{i}' for i in range(1, 101)],
        'Age': np.random.randint(16, 25, 100),
        'Grade': np.random.choice(['9th', '10th', '11th', '12th'], 100),
        'Subject': np.random.choice(['Math', 'Science', 'English', 'History', 'Art'], 100),
        'Test_Score': np.random.randint(50, 101, 100),
        'Assignment_Score': np.random.randint(60, 101, 100),
        'Participation': np.random.randint(70, 101, 100),
        'Attendance': np.random.randint(80, 101, 100),
        'Final_Grade': [],
        'Teacher': [f'Teacher_{i}' for i in np.random.randint(1, 11, 100)],
        'Parent_Contact': [f'+1-555-{np.random.randint(1000, 9999)}' for _ in range(100)],
        'Enrollment_Date': [datetime.now() - timedelta(days=np.random.randint(0, 365*2)) for _ in range(100)]
    }
    
    # Calculate final grade (weighted average)
    for i in range(100):
        final_grade = (data['Test_Score'][i] * 0.4 + 
                      data['Assignment_Score'][i] * 0.3 + 
                      data['Participation'][i] * 0.2 + 
                      data['Attendance'][i] * 0.1)
        data['Final_Grade'].append(round(final_grade, 1))
    
    df = pd.DataFrame(data)
    df.to_excel('sample_student_data.xlsx', index=False)
    print("✅ Created: sample_student_data.xlsx (100 student records)")

def create_customer_data():
    """Create customer data with contact and preference fields"""
    np.random.seed(321)
    
    data = {
        'Customer_ID': range(4001, 4101),
        'First_Name': [f'John', 'Jane', 'Mike', 'Sarah', 'David', 'Lisa', 'Tom', 'Emma', 'Alex', 'Maria'] * 10,
        'Last_Name': [f'Smith', 'Johnson', 'Williams', 'Brown', 'Jones', 'Garcia', 'Miller', 'Davis', 'Rodriguez', 'Martinez'] * 10,
        'Email': [f'customer{i}@email.com' for i in range(1, 101)],
        'Phone': [f'+1-555-{np.random.randint(1000, 9999)}' for _ in range(100)],
        'Age': np.random.randint(18, 80, 100),
        'Gender': np.random.choice(['Male', 'Female', 'Other'], 100),
        'City': np.random.choice(['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix', 'Philadelphia', 'San Antonio', 'San Diego', 'Dallas', 'San Jose'], 100),
        'State': np.random.choice(['NY', 'CA', 'IL', 'TX', 'AZ', 'PA', 'FL', 'OH', 'GA', 'NC'], 100),
        'Zip_Code': [f'{np.random.randint(10000, 99999)}' for _ in range(100)],
        'Membership_Level': np.random.choice(['Bronze', 'Silver', 'Gold', 'Platinum'], 100, p=[0.4, 0.3, 0.2, 0.1]),
        'Total_Purchases': np.random.randint(0, 10000, 100),
        'Last_Purchase_Date': [datetime.now() - timedelta(days=np.random.randint(0, 365*2)) for _ in range(100)],
        'Is_Active': np.random.choice([True, False], 100, p=[0.8, 0.2])
    }
    
    df = pd.DataFrame(data)
    df.to_excel('sample_customer_data.xlsx', index=False)
    print("✅ Created: sample_customer_data.xlsx (100 customer records)")

def create_weather_data():
    """Create weather data with time series and numeric fields"""
    np.random.seed(654)
    
    # Generate 100 days of weather data
    start_date = datetime.now() - timedelta(days=100)
    dates = [start_date + timedelta(days=i) for i in range(100)]
    
    data = {
        'Date': dates,
        'Temperature_C': np.random.uniform(-10, 35, 100).round(1),
        'Temperature_F': [],
        'Humidity': np.random.randint(20, 95, 100),
        'Pressure': np.random.uniform(980, 1030, 100).round(1),
        'Wind_Speed': np.random.uniform(0, 50, 100).round(1),
        'Wind_Direction': np.random.choice(['N', 'NE', 'E', 'SE', 'S', 'SW', 'W', 'NW'], 100),
        'Precipitation': np.random.uniform(0, 50, 100).round(2),
        'UV_Index': np.random.randint(0, 11, 100),
        'Visibility': np.random.uniform(5, 25, 100).round(1),
        'Weather_Condition': np.random.choice(['Sunny', 'Cloudy', 'Rainy', 'Snowy', 'Foggy', 'Stormy'], 100),
        'Location': ['Weather Station A'] * 100
    }
    
    # Convert Celsius to Fahrenheit
    data['Temperature_F'] = [(temp * 9/5) + 32 for temp in data['Temperature_C']]
    
    df = pd.DataFrame(data)
    df.to_excel('sample_weather_data.xlsx', index=False)
    print("✅ Created: sample_weather_data.xlsx (100 weather records)")

def create_simple_data():
    """Create simple data with basic fields for testing"""
    np.random.seed(987)
    
    data = {
        'ID': range(1, 21),
        'Name': [f'Item_{i}' for i in range(1, 21)],
        'Value': np.random.randint(1, 100, 20),
        'Category': np.random.choice(['A', 'B', 'C'], 20),
        'Active': np.random.choice([True, False], 20)
    }
    
    df = pd.DataFrame(data)
    df.to_excel('sample_simple_data.xlsx', index=False)
    print("✅ Created: sample_simple_data.xlsx (20 simple records)")

if __name__ == "__main__":
    print("🎯 Creating multiple sample Excel files for testing...\n")
    
    create_employee_data()
    create_sales_data()
    create_inventory_data()
    create_student_data()
    create_customer_data()
    create_weather_data()
    create_simple_data()
    
    print("\n🎉 All sample files created successfully!")
    print("\n📁 Files created:")
    print("• sample_employee_data.xlsx - Employee management data")
    print("• sample_sales_data.xlsx - Sales and financial data")
    print("• sample_inventory_data.xlsx - Inventory management data")
    print("• sample_student_data.xlsx - Academic and student data")
    print("• sample_customer_data.xlsx - Customer relationship data")
    print("• sample_weather_data.xlsx - Time series weather data")
    print("• sample_simple_data.xlsx - Simple test data")
    
    print("\n🚀 Ready to test your Excel Data Processor with various data types!") 