import streamlit as st
import base64

def videoPlayback(video, loop, autostart):
    video_bytes = video.read()
    video_base64 = base64.b64encode(video_bytes).decode('utf-8')

    if loop and autostart:
        video_html = f"""
            <video loop autoplay controls style="max-width: 100%; height: auto;">
            <source src="data:video/{video.type};base64,{video_base64}" type="{video.type}">
            Your browser does not support the video tag.
            </video>
            """
    elif loop:
        video_html = f"""
        <video loop controls style="max-width: 100%; height: auto;">
            <source src="data:video/{video.type};base64,{video_base64}" type="{video.type}">
            Your browser does not support the video tag.
        </video>
        """
    elif autostart:
        video_html = f"""
        <video autoplay controls style="max-width: 100%; height: auto;"> 
            <source src="data:video/{video.type};base64,{video_base64}" type="{video.type}">
            Your browser does not support the video tag.
        </video>
        """
    else: 
        return st.video(video)
    
    st.markdown(video_html, unsafe_allow_html=True)

def main():
    st.set_page_config(
        page_title="Automatic Construction Site Monitoring: Advanced Video Analytics for Activity Detection",
        layout="wide",
        initial_sidebar_state="expanded"
    )
    st.title("Automatic Construction Site Monitoring: Advanced Video Analytics for Activity Detection")
    
    video = st.file_uploader('Upload the video', type=['.mp4'], accept_multiple_files=True)
    
    if video:
        st.write("Video uploaded successfully!")
        if len(video) > 0:  # Check if there's at least one video uploaded
            st.write("Uploaded Video:")
            videoPlayback(video[0], loop=True, autostart=True)
            st.button("Analyze Video")
    else:
        st.write("Upload a video")

    
if __name__ =="__main__":
    main()
