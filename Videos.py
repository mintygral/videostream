import streamlit as st
import base64
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np
import matplotlib.pyplot as plt

def videoPlayback(video, loop, autostart):
    """Displays a video with playback controls and optional loop/autostart.

    Args:
        video (streamlit.uploadedfile.UploadedFile): The uploaded video file.
        loop (bool): Whether to loop the video playback.
        autostart (bool): Whether to automatically start video playback.

    Returns:
        None
    """

    video_bytes = video.read()
    video_base64 = base64.b64encode(video_bytes).decode('utf-8')

    video_html = f"""
    <video id="myVideo" controls style="max-width: 100%; height: auto;">
        <source src="data:video/{video.type};base64,{video_base64}" type="{video.type}">
        Your browser does not support the video tag.
    </video>
    """

    st.markdown(video_html, unsafe_allow_html=True)

    # JavaScript to handle timestamp clicks and video seeking
    script = """
    <script>
        const video = document.getElementById('myVideo');
        const timestamps = document.querySelectorAll('.timestamp');  // Select all timestamp elements

        timestamps.forEach(timestamp => {
            timestamp.addEventListener('click', () => {
                const timeString = timestamp.textContent.trim();
                const timeParts = timeString.split(':');
                const seconds = parseInt(timeParts[0]) * 60 + parseInt(timeParts[1]) + parseInt(timeParts[2]) / 60;

                // Validate timestamp within video duration (optional)
                if (seconds <= video.duration) {
                    video.currentTime = seconds;
                } else {
                    alert('Invalid timestamp. Please select a timestamp within the video duration.');
                }
            });
        });
    </script>
    """
    st.sidebar.markdown(script, unsafe_allow_html=True)

def session():

    st.title("Automatic Construction Site Monitoring: Advanced Video Analytics for Activity Detection")

    video = st.file_uploader('Upload the video', type=['.mp4'], accept_multiple_files=False)

    if video:
        st.write("Video uploaded successfully!")
        st.write("Uploaded Video:")
        videoPlayback(video, loop=True, autostart=True)

        if st.button("Analyze Video"):
            # Table with timestamps
            data = {
                'Event': ['Backfiling', 'Compaction', 'Strap Installation'],
                'Timestamp': [['00:00:00-00:02:40', '00:04:10-00:05:48'],
                              ['00:03:00-00:03:57'],
                              ['00:06:25-00:07:05']]
            }
            df = pd.DataFrame(data)


            st.write("Analysis Results:")
            st.dataframe(df, use_container_width=True)  # Ensure proper table width

            # Create figure
            fig = go.Figure()

            # Define color palette for events
            colors = ['blue', 'green', 'red']

            # Plot horizontal lines for each event
            for i, (event, timestamps) in enumerate(zip(data['Event'], data['Timestamp'])):
                for ts_range in timestamps:
                    start, end = ts_range.split('-')
                    start_sec = int(start.split(':')[1]) * 60 + int(start.split(':')[2])
                    end_sec = int(end.split(':')[1]) * 60 + int(end.split(':')[2])
                    fig.add_trace(go.Scatter(x=[start_sec, end_sec], y=[event, event],
                                             mode='lines',
                                             line=dict(color=colors[i], width=6),
                                             name=event,
                                             hoverinfo='text',
                                             text=[f'{event}: {start} - {end}']
                                            ))

            # Customize layout
            fig.update_layout(title='Event Timeline',
                              xaxis_title='Time (seconds)',
                              yaxis_title='',
                              template='plotly_white',
                              legend=dict(y=0.5, traceorder='reversed', font=dict(size=12)))

            # Show plot
            st.plotly_chart(fig, use_container_width=True, config={'displayModeBar': False})

    if st.button("Logout"):
            del st.session_state["logged_in"]
            st.experimental_rerun()


if __name__ == "__session__":
    session()
