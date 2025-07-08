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
│   └── 08_input-widget.py   # Interactive input widgets
├── data/                     # Sample data files
│   ├── sample.csv           # Time series sample data
│   └── sample_map.csv       # Geographic coordinates for mapping
├── .streamlit/              # Streamlit configuration
│   └── config.toml          # App configuration settings
└── README.md               # This file
```

## 🚀 Installation

### Prerequisites

- Python 3.7 or higher
- pip package manager

### Setup

1. **Clone the repository** (or navigate to the project directory):
   ```bash
   cd streamlit
   ```

2. **Install required dependencies**:
   ```bash
   pip install streamlit pandas numpy matplotlib
   ```

3. **Run the application**:
   ```bash
   streamlit run main_page.py
   ```

4. **Access the application**:
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
- **Usage**: Complex data display and potential future analytics features
- **Scope**: User activity data from Malaysia and Singapore regions

## ⚙️ Configuration

The application uses Streamlit's configuration file (`.streamlit/config.toml`) with the following settings:

- **Server**: Auto-reload on save enabled
- **Theme**: Light theme
- **Client**: Minimal toolbar mode
- **Runner**: Fast rebuild on file changes
- **Browser**: Usage statistics collection disabled
- **Layout**: Wide layout mode enabled

## 🤝 Contributing

To contribute to this project:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/new-feature`)
3. Make your changes
4. Test the application thoroughly
5. Commit your changes (`git commit -am 'Add new feature'`)
6. Push to the branch (`git push origin feature/new-feature`)
7. Create a Pull Request

### Development Guidelines

- Follow Python PEP 8 style guidelines
- Add comments for complex functionality
- Test all interactive components
- Ensure compatibility with the existing page structure
- Update this README when adding new features

## 📝 License

This project is for demonstration purposes. Please refer to your organization's licensing requirements.

---

**Note**: This application is designed for educational and demonstration purposes to showcase Streamlit's capabilities. It can be extended with additional features, custom styling, and more complex data processing as needed. 