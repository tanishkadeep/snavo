from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.formatters import TextFormatter

def transcript_video(link):
    video_id = link.split("=")[1]
    
    transcript_list = YouTubeTranscriptApi.list_transcripts(video_id)
    
    languages = [] 
    for transcript in transcript_list:
        languages.append(transcript.language_code)
    
        
    if 'en' in languages:
        transcript = transcript_list.find_transcript(['en'])
    else:
        for transcript in transcript_list:
            if transcript.is_translatable:
                transcript = transcript.translate('en')
                break   
            
    
    formatted_transcript = text_formatter(transcript.fetch())
    
    return formatted_transcript

def text_formatter(text):
    formatter = TextFormatter()
    
    formatted_transcript = formatter.format_transcript(text)

    formatted_transcript = formatted_transcript.split("\n")
    formatted_transcript = " ".join(formatted_transcript)
    
    return formatted_transcript
