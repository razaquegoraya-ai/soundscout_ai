# SoundScout AI

SoundScout AI is a music trend analysis platform that provides insights into emerging artists and tracks across different genres. It uses AI to predict trends and generate comprehensive reports.

## Features

- Genre-specific trend analysis
- Predictive analytics for track performance
- Artist spotlight features
- Creative inspiration suggestions
- Automated weekly report generation
- Streamlit-based interactive dashboard

## Setup

1. Install Python 3.9+ on your system
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Set up API credentials:
   - Get Spotify API credentials from [Spotify Developer Dashboard](https://developer.spotify.com/dashboard)
   - Get YouTube API key from [Google Cloud Console](https://console.cloud.google.com)
   - Update credentials in `fetch_data.py`

## Usage

### Local Development

1. Run the report generator:
   ```bash
   python generate_reports.py
   ```
   This will generate genre-specific reports and save them in the current directory.

2. Start the Streamlit app:
   ```bash
   streamlit run app.py
   ```
   Visit http://localhost:8501 to access the dashboard.

### Production Deployment

1. Upload the codebase to your server
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run Streamlit in production:
   ```bash
   nohup streamlit run app.py --server.port 8501 &
   ```
4. Set up automated report generation:
   ```bash
   crontab -e
   # Add the following line for Sunday 11 PM execution:
   0 23 * * 0 python3 /path/to/soundscout_ai/generate_reports.py
   ```

## File Structure

- `app.py`: Streamlit dashboard application
- `fetch_data.py`: API data collection module
- `generate_reports.py`: Automated report generation
- `logs/`: Directory for log files
- `*_data.py`: Genre-specific data files
- `requirements.txt`: Python dependencies

## API Integration

The platform currently integrates with:
- Spotify API for track data
- YouTube API for video metrics
- (Placeholder) TikTok API for social metrics
- (Placeholder) X (Twitter) API for social buzz

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.# soundscout_ai
