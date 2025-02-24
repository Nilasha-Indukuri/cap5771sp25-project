# cap5771sp25-project

  <h1>Movie Data Analysis Project</h1>
  <p>
    This project is designed to merge, clean, and analyze multiple movie datasets to create a comprehensive data source for further analysis, research, and machine learning applications.
  </p>

  <h2>Overview</h2>
  <p>
    The Python script provided in this project performs the following tasks:
  </p>
  <ul>
    <li>Importing necessary libraries.</li>
    <li>Loading three movie datasets: <code>movies.csv</code>, <code>IMDB TMDB Movie Metadata Big Dataset</code>, and <code>TMDB_movie_dataset_v11.csv</code>.</li>
    <li>Checking and printing dataset shapes and column names.</li>
    <li>Converting key numeric columns (<code>budget</code>, <code>revenue</code>, <code>runtime</code>, and <code>vote_count</code>) to the appropriate data type (<code>float64</code>).</li>
    <li>Merging datasets using outer joins based on common columns like <code>id</code> and <code>title</code>.</li>
    <li>Filling missing values by combining data from the merged datasets.</li>
    <li>Preprocessing data by handling missing values, detecting and removing outliers, and normalizing numeric features.</li>
    <li>Performing exploratory data analysis (EDA) with descriptive statistics and visualizations such as histograms, box plots, and correlation matrices.</li>
  </ul>

  <h2>Libraries Used</h2>
  <ul>
    <li><strong>pandas</strong>: Data manipulation and analysis.</li>
    <li><strong>numpy</strong>: Numerical operations.</li>
    <li><strong>matplotlib</strong> and <strong>seaborn</strong>: Data visualization.</li>
    <li><strong>plotly.express</strong>: Interactive plotting (if needed).</li>
    <li><strong>datetime</strong>: Date and time manipulation.</li>
    <li><strong>scipy</strong>: Statistical functions.</li>
    <li><strong>sklearn.preprocessing</strong>: Data scaling and normalization.</li>
  </ul>

  <h2>Usage Instructions</h2>
  <ol>
    <li>
      Ensure that the following CSV files are present and accessible in the specified paths:
      <ul>
        <li><code>movies.csv</code></li>
        <li><code>IMDB TMDB Movie Metadata Big Dataset (1M).csv</code></li>
        <li><code>TMDB_movie_dataset_v11.csv</code></li>
      </ul>
    </li>
    <li>
      Adjust the file paths in the script as necessary to point to the correct locations on your machine.
    </li>
    <li>
      Run the Python script in your development environment. The script will load the datasets, perform merging and cleaning operations, and display various outputs including dataset information and visualizations.
    </li>
    <li>
      After preprocessing, the merged dataset is saved as <code>merged_movies_dataset_full.csv</code> for future analysis.
    </li>
  </ol>

  <h2>Project Structure</h2>
  <ul>
    <li><strong>Data Loading:</strong> Imports CSV files and displays basic dataset information.</li>
    <li><strong>Data Merging:</strong> Merges datasets on common columns and fills missing data.</li>
    <li><strong>Data Cleaning:</strong> Handles missing values, removes outliers, and normalizes numerical data.</li>
    <li><strong>Exploratory Data Analysis:</strong> Generates descriptive statistics and visualizations.</li>
  </ul>

  <h2>Conclusion</h2>
  <p>
    This project provides a robust pipeline for integrating and analyzing movie data. The thorough data preprocessing and EDA steps ensure that the dataset is well-prepared for further exploration, predictive modeling, or machine learning tasks.
  </p>
  <p>
    For any questions or further improvements, please feel free to reach out or contribute to the project.
  </p>

  <h3>License</h3>
  <p>
    This project is open source and available under the MIT License.
  </p>
</body>
</html>
