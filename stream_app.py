import streamlit as st
import base64
import numpy as np 
def videoPlayback(video, loop, autostart):
    video_bytes = video.read()

    video_base64 = base64.b64encode(video_bytes).decode('utf-8')

    if loop == True and autostart == True:
        video_html = f"""
            <video loop autoplay controls style="max-width: 100%; height: auto;">
            <source src="data:video/{video.type};base64,{video_base64}" type="{video.type}">
            Your browser does not support the video tag.
            </video>
            """
    elif loop == True and autostart == False:
        video_html = f"""
        <video loop controls style="max-width: 100%; height: auto;">
            <source src="data:video/{video.type};base64,{video_base64}" type="{video.type}">
            Your browser does not support the video tag.
        </video>
        """
    elif autostart == True and loop == False:
        video_html = f"""
        <video autoplay controls style="max-width: 100%; height: auto;"> 
            <source src="data:video/{video.type};base64,{video_base64}" type="{video.type}">
            Your browser does not support the video tag.
        </video>
        """
    else: 
        return st.video(video)
    return st.markdown(video_html, unsafe_allow_html = True)
def videoInGrid(num_columns, videos, autostart, loop):
    num_columns = num_columns
    num_objects_per_column = int(np.ceil(len(videos) / num_columns))
    col = st.columns(num_columns)
    
    for i in range(num_columns):
        with col[i]:
            for j in range(i * num_objects_per_column, (i + 1) * num_objects_per_column):
                videoPlayback(video=videos[j], autostart=autostart, loop=loop)
def main():
    st.set_page_config(
        page_title="My Streamlit App",
        layout="wide",
        initial_sidebar_state="expanded"
    )
    st.title("Video Showing Test App")
    video = st.file_uploader('Upload the video', type =['.mp4'], accept_multiple_files=True)
    if video is not None:
        videoInGrid(
            num_columns = 2,
            videos = video,
            autostart=True,
            loop=True
        )
    
if __name__ =="__main__":
    main()
