import requests
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
import seaborn as sns
from typing import List, Dict, Tuple

class WeatherAnalyzer:
    """A class to analyze and visualize weather data."""
    
    def __init__(self, api_key: str = None):
        """Initialize the WeatherAnalyzer with an optional API key."""
        self.api_key = api_key or "YOUR_API_KEY"
        self.base_url = "https://api.openweathermap.org/data/2.5/forecast"
        self.data: List[Dict] = []
        
    def fetch_weather_forecast(self, city: str = "London") -> Dict:
        """Fetch 5-day weather forecast for a given city."""
        params = {
            "q": city,
            "appid": self.api_key,
            "units": "metric"
        }
        
        # Simulate API response for demo purposes
        self.data = self._generate_sample_data()
        return self.data
    
    def _generate_sample_data(self) -> List[Dict]:
        """Generate sample weather data for demonstration."""
        base_temp = 20
        data = []
        now = datetime.now()
        
        for i in range(40):  # 5 days * 8 measurements per day
            time = now + timedelta(hours=i*3)
            temp_variation = (i % 8) - 4  # Temperature variation through the day
            
            data.append({
                "datetime": time.isoformat(),
                "temperature": base_temp + temp_variation + (i % 3),
                "humidity": 60 + (i % 20),
                "wind_speed": 5 + (i % 10)
            })
        
        return data
    
    def analyze_temperature_trends(self) -> Tuple[float, float, float]:
        """Analyze temperature trends in the data."""
        temps = [d["temperature"] for d in self.data]
        return min(temps), max(temps), sum(temps)/len(temps)
    
    def visualize_data(self, save_path: str = "weather_analysis.png"):
        """Create a visualization of the weather data."""
        df = pd.DataFrame(self.data)
        df["datetime"] = pd.to_datetime(df["datetime"])
        
        # Create a figure with subplots
        fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 8))
        fig.suptitle("Weather Analysis Dashboard", fontsize=16)
        
        # Temperature plot
        sns.lineplot(data=df, x="datetime", y="temperature", ax=ax1)
        ax1.set_title("Temperature Over Time")
        ax1.set_xlabel("Date/Time")
        ax1.set_ylabel("Temperature (°C)")
        
        # Humidity vs Wind Speed scatter plot
        sns.scatterplot(data=df, x="humidity", y="wind_speed", ax=ax2)
        ax2.set_title("Humidity vs Wind Speed")
        ax2.set_xlabel("Humidity (%)")
        ax2.set_ylabel("Wind Speed (m/s)")
        
        plt.tight_layout()
        plt.savefig(save_path)
        plt.close()

def main():
    # Create analyzer instance
    analyzer = WeatherAnalyzer()
    
    # Fetch weather data
    print("Fetching weather data...")
    analyzer.fetch_weather_forecast("London")
    
    # Analyze trends
    min_temp, max_temp, avg_temp = analyzer.analyze_temperature_trends()
    print(f"\nTemperature Analysis:")
    print(f"Minimum Temperature: {min_temp:.1f}°C")
    print(f"Maximum Temperature: {max_temp:.1f}°C")
    print(f"Average Temperature: {avg_temp:.1f}°C")
    
    # Create visualization
    print("\nGenerating visualization...")
    analyzer.visualize_data()
    print("Visualization saved as 'weather_analysis.png'")

if __name__ == "__main__":
    main()