import pandas as pd

class DataPreprocessor:
    """Simple class to load, clean and export data"""
    
    def __init__(self):
        self.df = None
    
    def load_data(self, source):
        """Load data from CSV file or DataFrame"""
        if isinstance(source, str):
            # Load from CSV file
            self.df = pd.read_csv(source)
        else:
            # Load from DataFrame
            self.df = source.copy()
        
        print(f"Data loaded: {self.df.shape[0]} rows, {self.df.shape[1]} columns")
        return self.df
    
    def clean_data(self):
        """Remove null values and duplicates"""
        if self.df is None:
            print("Error: No data loaded. Please load data first.")
            return
            
        print(f"Before cleaning: {self.df.shape[0]} rows")
        
        # Remove null values
        self.df = self.df.dropna()
        
        # Remove duplicates
        self.df = self.df.drop_duplicates()
        
        print(f"After cleaning: {self.df.shape[0]} rows")
        return self.df
    
    def export_data(self, filepath):
        """Save cleaned DataFrame to CSV"""
        if self.df is None:
            print("Error: No data loaded. Please load data first.")
            return
            
        self.df.to_csv(filepath, index=False)
        print(f"Data saved to: {filepath}")

class DataAnalyzer(DataPreprocessor):
    """Extended class for data analysis"""
    
    def summary(self):
        """Show basic statistics for numeric variables"""
        if self.df is None:
            print("Error: No data loaded. Please load data first.")
            return
            
        print("=== STATISTICAL SUMMARY ===")
        
        # Select only numeric columns
        numeric_cols = self.df.select_dtypes(include=['number'])
        
        # Show basic statistics
        print("\nMean:")
        print(numeric_cols.mean().round(2))
        
        print("\nMaximum:")
        print(numeric_cols.max())
        
        print("\nMinimum:")
        print(numeric_cols.min())
        
        return numeric_cols.describe()
    
    def correlation(self):
        """Show correlation between numeric variables"""
        if self.df is None:
            print("Error: No data loaded. Please load data first.")
            return
            
        numeric_cols = self.df.select_dtypes(include=['number'])
        corr_matrix = numeric_cols.corr()
        print("\n=== CORRELATION MATRIX ===")
        print(corr_matrix.round(2))
        return corr_matrix