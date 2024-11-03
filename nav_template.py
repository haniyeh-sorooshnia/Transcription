import gradio as gr
from apps.app1 import render as app1_interface 
from apps.app2 import render as app2_interface  
from apps.app3 import render as app3_interface

def create_navbar():
    with gr.Blocks() as demo:
        with gr.Tab("مبتنی بر قانون فونتیک"):
            try:
                app1_interface()  
            except Exception as e:
                gr.Error(f"Error loading the first app: {str(e)}")  

        with gr.Tab("مبتنی بر فهرست"):
            try:
                app2_interface()
            except Exception as e:
                gr.Error(f"Error loading the second app: {str(e)}")  

        with gr.Tab("مبتنی بر قانون و فهرست"):
            try:
                app3_interface()  
            except Exception as e:
                gr.Error(f"Error loading the third app: {str(e)}")  
    return demo  



