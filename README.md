# Streamlit Demo Application

A comprehensive Streamlit application demonstrating various Streamlit components, widgets, and data visualization capabilities.

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Pages Overview](#pages-overview)
- [Data Files](#data-files)
- [Configuration](#configuration)
- [Contributing](#contributing)

## 🎯 Overview

This Streamlit application serves as a comprehensive demo showcasing the various capabilities of Streamlit framework. It includes multiple pages demonstrating different aspects of Streamlit functionality including:

- Interactive widgets and user inputs
- Data visualization and charting
- Text formatting and display options
- Data tables and metrics
- Layout components (sidebar, columns)
- Progress indicators

## ✨ Features

- **Multi-page Application**: Organized into distinct pages for different functionalities
- **Interactive Widgets**: Buttons, sliders, checkboxes, radio buttons, selectboxes
- **Data Visualization**: Line charts, bar charts, maps, and matplotlib integration
- **Text Formatting**: Headers, markdown, code blocks, LaTeX support
- **Data Display**: DataFrames, tables, metrics with delta indicators
- **Layout Components**: Sidebar navigation, column layouts, progress bars
- **Real-time Updates**: Auto-refresh on file changes for development

## 📁 Project Structure

```
streamlit/
├── main_page.py              # Main application page with core demonstrations
├── pages/                    # Additional pages for specific features
│   ├── 05_text.py           # Text formatting and display components
│   ├── 06_data-display.py   # Data tables and metrics display
│   ├── 07_charting.py       # Charts and data visualization
│   ├── 08_input-widget.py   # Interactive input widgets
│   └── 09_user-activity-chart.py  # User activity analysis and visualization
├── data/                     # Sample data files
│   ├── sample.csv           # Time series sample data
│   └── sample_map.csv       # Geographic coordinates for mapping
├── .streamlit/              # Streamlit configuration
│   └── config.toml          # App configuration settings
├── pyproject.toml           # Modern Python project configuration
├── requirements.txt         # Python dependencies
└── README.md               # This file
```

## 🚀 Installation

### Prerequisites

- Python 3.8 or higher
- pip package manager (or poetry for advanced dependency management)

### Setup

#### Option 1: Using pip (Recommended)

1. **Clone the repository** (or navigate to the project directory):
   ```bash
   cd streamlit
   ```

2. **Create a virtual environment** (recommended):
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install required dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

#### Option 2: Using pip with pyproject.toml

```bash
pip install -e .
```

#### Option 3: Development Installation

For development with additional tools (code formatting, linting, testing):
```bash
pip install -e ".[dev]"
```

### Running the Application

```bash
streamlit run main_page.py
```

**Access the application**:
- The app will automatically open in your default browser
- If not, navigate to `http://localhost:8501`

## 💻 Usage

### Running the Application

```bash
streamlit run main_page.py
```

The application will start with the main page displaying various Streamlit components. Use the sidebar navigation to explore different pages.

### Development Mode

The application is configured for development with:
- Auto-reload on file changes
- Minimal toolbar mode
- Wide layout mode
- Usage statistics disabled

## 📄 Pages Overview

### Main Page (`main_page.py`)
The primary page demonstrating:
- **Data Display**: DataFrame creation and display
- **Interactive Widgets**: Selectbox, checkbox, sidebar components
- **Charts**: Line charts with random data
- **Layout**: Sidebar controls, column layouts
- **Progress Indicators**: Progress bars with real-time updates
- **Session State**: Name input with state management

### Text Page (`pages/05_text.py`)
Showcases text formatting capabilities:
- Page titles and headers (multiple levels)
- Markdown formatting (bold text, links, headers)
- Code block display
- LaTeX mathematical expressions
- Captions and dividers

### Data Display Page (`pages/06_data-display.py`)
Focuses on data presentation:
- DataFrame display using `st.dataframe()`
- Table display using `st.table()`
- Generic display using `st.write()`
- Metrics with delta indicators

### Charting Page (`pages/07_charting.py`)
Demonstrates data visualization:
- Geographic mapping with coordinate data
- Matplotlib integration for custom plots
- Sales data visualization with proper labeling
- Commented examples for various chart types (line, area, bar)

### Input Widgets Page (`pages/08_input-widget.py`)
Interactive input components:
- **Buttons**: Primary and secondary button types
- **Selection**: Radio buttons, selectboxes, multiselect
- **Input Fields**: Text input, number input, text areas
- **Controls**: Checkboxes, sliders with value ranges
- **Data Integration**: Dynamic column selection from CSV data

### User Activity Analysis Page (`pages/09_user-activity-chart.py`)
Comprehensive user activity analytics and visualization:
- **Interactive Dashboard**: Overview metrics with total users, active users, and country count
- **Top Users Analysis**: Configurable top N users per country with slider control
- **Country Breakdown**: Detailed tables showing top users by country with division information
- **Multiple Visualizations**: Streamlit bar charts and custom matplotlib charts
- **Statistical Insights**: Country-wise summaries with aggregated login metrics
- **Key Performance Indicators**: Most active country, user, and engagement statistics

## 📊 Data Files

### `sample.csv`
Time series data with yearly progression:
- **Columns**: year, col1, col2, col3
- **Usage**: Chart demonstrations and data display examples
- **Data Range**: 2018-2022 with increasing values

### `sample_map.csv`
Geographic coordinate data:
- **Columns**: latitude, longitude
- **Usage**: Map visualization demonstrations
- **Locations**: Major Canadian cities (Toronto, Vancouver, Calgary, Ottawa, Edmonton)

### `user_activity_summary.csv`
User activity analytics data:
- **Columns**: 22+ activity metrics including country, division, user details, and various count metrics
- **Key Fields**: country, fullName, division, logins, and various activity counters
- **Usage**: User activity analysis, login tracking, and performance analytics
- **Scope**: User activity data from Malaysia and Singapore regions
- **Analytics**: Powers the user activity dashboard with login count analysis by country

## ⚙️ Configuration

### Project Configuration

The project uses modern Python configuration standards:

#### `pyproject.toml`
Modern Python project configuration following PEP 518/621 standards:
- **Project metadata**: Name, version, description, authors
- **Dependencies**: Core requirements and optional development dependencies
- **Tool configurations**: Black (code formatting), Flake8 (linting), MyPy (type checking), Pytest (testing)
- **Build system**: Setuptools-based build configuration
- **Scripts**: Custom command entry points

#### `requirements.txt`
Traditional dependency file for simple pip installations:
- Core dependencies: Streamlit, Pandas, NumPy, Matplotlib
- Version pinning for reproducible environments

### Streamlit Configuration

The application uses Streamlit's configuration file (`.streamlit/config.toml`) with optimized settings:

- **Server**: Auto-reload on save enabled for development
- **Theme**: Light theme for consistent appearance
- **Client**: Minimal toolbar mode for cleaner UI
- **Runner**: Fast rebuild on file changes for rapid development
- **Browser**: Usage statistics collection disabled for privacy
- **Layout**: Wide layout mode for better data visualization

## 🛠️ Development

### Development Tools

The project includes configuration for modern Python development tools:

#### Code Formatting
```bash
# Install development dependencies
pip install -e ".[dev]"

# Format code with Black
black .

# Check code style with Flake8
flake8 .
```

#### Type Checking
```bash
# Run type checking with MyPy
mypy .
```

#### Testing
```bash
# Run tests with Pytest
pytest

# Run tests with coverage
pytest --cov=. --cov-report=html
```

#### Pre-commit Hooks
```bash
# Install pre-commit hooks
pre-commit install

# Run hooks manually
pre-commit run --all-files
```

## 🤝 Contributing

To contribute to this project:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/new-feature`)
3. Make your changes
4. Run code quality checks:
   ```bash
   black .
   flake8 .
   mypy .
   pytest
   ```
5. Test the application thoroughly
6. Commit your changes (`git commit -am 'Add new feature'`)
7. Push to the branch (`git push origin feature/new-feature`)
8. Create a Pull Request

### Development Guidelines

- Follow Python PEP 8 style guidelines (enforced by Black and Flake8)
- Add type hints where appropriate (checked by MyPy)
- Write tests for new functionality
- Add comments for complex functionality
- Test all interactive components
- Ensure compatibility with the existing page structure
- Update this README when adding new features

## 📝 License

This project is for demonstration purposes. Please refer to your organization's licensing requirements.

---

**Note**: This application is designed for educational and demonstration purposes to showcase Streamlit's capabilities. It can be extended with additional features, custom styling, and more complex data processing as needed. 